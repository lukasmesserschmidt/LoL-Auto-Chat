import os
import time
from random import randint
import keyboard
import pyautogui

from ..utils.thread_base import ThreadBase
from ..lol_data.active_player_data import ActivePlayerData
from ..lol_data.all_player_data import AllPlayerData
from ..lol_data.event_data import EventData
from .lol_manager import LolManager
from .config_manager import ConfigManager
from ..utils.constants import Constants
from ..utils import paths


class ChatManager(ThreadBase):
    """
    This class manages the chat.
    """

    # contains the current preset message lists for the events
    current_preset = {
        Constants.ALLY_KILL: [],
        Constants.ALL_DEATH: [],
    }

    # thread control
    @classmethod
    def stop(cls):
        """
        Stops the chat event loop and clears the current preset, if it is running.
        """
        super().stop()
        for message_list in cls.current_preset.values():
            message_list.clear()

    # chat event loop thread
    @classmethod
    def _loop(cls):
        # init event count variables
        current_event_count = len(EventData.get_all_events())
        last_event_count = current_event_count

        # fill current preset dict with the current preset messages
        cls._fill_current_preset()

        while not cls._terminate_flag:
            # get a list of all events
            all_events = EventData.get_all_events()

            # set get current event count
            current_event_count = (
                len(all_events) if all_events is not None else current_event_count
            )

            # check if there are new events
            if all_events is not None and current_event_count > last_event_count:
                for current_event in all_events[last_event_count:]:
                    current_event_name = current_event.get("EventName")

                    # check if the event is a champion kill
                    if current_event_name == "ChampionKill":
                        cls._champion_kill_event(current_event)

                last_event_count = current_event_count

            cls.wait(Constants.INTERVAL)

    # event handlers
    @classmethod
    def _champion_kill_event(cls, current_event: dict):
        """
        Handles the champion kill events.
        """
        # get the killer and victim names
        killer_name = current_event.get("KillerName")
        victim_name = current_event.get("VictimName")

        if killer_name is None or victim_name is None:
            return

        # get the ally team
        ally_team = ActivePlayerData.get_team_player_names(True)

        if ally_team is not None:
            # send ally kill message
            if killer_name in ally_team:
                message = cls._get_messages_from_preset(
                    Constants.ALLY_KILL, killer_name
                )

                if message is not None:
                    cls._write_to_chat(message)

            # send ally death message
            elif victim_name in ally_team:
                message = cls._get_messages_from_preset(
                    Constants.ALL_DEATH, victim_name
                )

                if message is not None:
                    cls._write_to_chat(message)

    # message managers
    @classmethod
    def _get_messages_from_preset(
        cls,
        event_name: str,
        player_name: str,
    ):
        """
        Gets the messages from the preset and replace the placeholders with the champion name.
        """
        # get the name of the currently selected preset
        current_preset_name = ConfigManager.current_preset_name

        if current_preset_name is None:
            return None

        # contains the current preset messages for the events
        event_message_list = cls.current_preset.get(event_name)

        # fill the event message list if it is empty
        if len(event_message_list) == 0:
            cls._fill_event_message_list(event_name)
            event_message_list = cls.current_preset.get(event_name)

        if len(event_message_list) > 0:
            # get a random message index
            random_message = randint(0, len(event_message_list) - 1)

            # get the random message with the random index
            if ConfigManager.remove_used_messages:
                # get and remove the message from the list
                message = event_message_list.pop(random_message)
            else:
                # get the random message
                message = event_message_list[random_message]

            # get the champion name from the player name
            champion_name = AllPlayerData.get_player_champion_name(player_name)

            if champion_name is None:
                return None

            # replace the placeholders with the champion name
            message = message.replace("|CN?|", champion_name)

            return message

        return None

    @classmethod
    def _write_to_chat(cls, message: str):
        """
        Writes the given message to the chat/allchat.
        """
        # write the message if League of Legends is in the foreground
        if LolManager.is_lol_foreground():
            # use all chat if it is enabled
            if ConfigManager.use_all_chat:
                keyboard.press_and_release("shift+enter")
            else:
                keyboard.press_and_release("enter")
            time.sleep(0.05)
            keyboard.write(message)
            time.sleep(0.02)
            pyautogui.press("enter")

    # preset managers
    @classmethod
    def _fill_event_message_list(cls, event_name: str):
        """
        Fills the current preset event message list,
        with the given event name, with the event messages from the txt file.
        """
        # get the name of the currently selected preset
        current_preset_name = ConfigManager.current_preset_name

        if current_preset_name is None:
            return

        # get the path of the txt file with the event name
        file_path = os.path.join(
            paths.get_presets_dir_path(), current_preset_name, f"{event_name}.txt"
        )

        if not os.path.exists(file_path):
            return

        # fills the current preset event message list with the event messages from the txt file
        with open(file_path, "r", encoding="utf-8") as file:
            cls.current_preset[event_name] = file.readlines()

    @classmethod
    def _fill_current_preset(cls):
        """
        Fills the current preset dict, with all event message lists from the txt files.
        """
        # get the name of the currently selected preset
        current_preset_name = ConfigManager.current_preset_name

        if current_preset_name is None:
            return

        # fills the current preset dict with all event message lists from the txt files
        for event_name in cls.current_preset:
            cls._fill_event_message_list(event_name)
