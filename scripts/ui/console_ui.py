import os
import subprocess
import time
import msvcrt
import webbrowser

from ..lol_data.lol_live_client_data import LolLiveClientData
from ..managers.lol_manager import LolManager
from ..managers.chat_manager import ChatManager
from ..managers.config_manager import ConfigManager
from ..utils.new_preset import NewPreset
from ..utils.constants import Constants
from ..utils import paths


class ConsoleUi:
    """
    This class provides the console UI.
    """

    current_menu = Constants.MAIN_MENU

    @classmethod
    def get_input(cls):
        """
        Gets the input from the user.
        """
        # init input value default
        input_value = ""

        # gets the input for the main menu
        if cls.current_menu == Constants.MAIN_MENU:
            cls._write_default_input_section()
            input_value = input("Change/select option: ").strip()

        # gets the input for the toggle events settings
        elif cls.current_menu == Constants.TOGGLE_EVENTS_MENU:
            cls._write_default_input_section()
            input_value = input("Change option: ").strip()

        # gets the input for the preset menu
        elif cls.current_menu == Constants.PRESET_MENU:
            cls._write_default_input_section()
            input_value = input("Select option: ").strip()

        # gets the input for the waiting menu
        elif cls.current_menu == Constants.WAITING_MENU:
            # wait for the game to start or if enter is pressed
            while not LolManager.is_lol_running():
                if msvcrt.kbhit():
                    if msvcrt.getch() == b"\r":
                        input_value = "b"
                        break
                time.sleep(0.1)
            input_value = "s"

        # gets the input for the in game menu
        elif cls.current_menu == Constants.IN_GAME_MENU:
            # wait for the game to end or if enter is pressed
            while LolManager.is_lol_running():
                if msvcrt.kbhit():
                    if msvcrt.getch() == b"\r":
                        break
                time.sleep(0.1)

        return input_value.lower()

    @classmethod
    def handle_input(cls, input_value):
        """
        Handles the user input.
        """
        # load config
        config = ConfigManager.load()

        # handle general input
        if input_value == "h":
            config[Constants.SHOW_HELP] = not ConfigManager.show_help
            ConfigManager.save(config)
            cls.load_current_menu()

        # handle main menu input
        elif cls.current_menu == Constants.MAIN_MENU:
            if input_value == "s" and cls._preset_exists(
                ConfigManager.current_preset_name
            ):
                LolLiveClientData.start()
                cls.current_menu = Constants.WAITING_MENU
            elif input_value == "1":
                config[Constants.REMOVE_USED_MESSAGES] = (
                    not ConfigManager.remove_used_messages
                )
                ConfigManager.save(config)
                cls.current_menu = Constants.MAIN_MENU
            elif input_value == "2":
                config[Constants.USE_ALL_CHAT] = not ConfigManager.use_all_chat
                ConfigManager.save(config)
                cls.current_menu = Constants.MAIN_MENU
            elif input_value == "3":
                cls.current_menu = Constants.TOGGLE_EVENTS_MENU
            elif input_value == "4":
                cls.current_menu = Constants.PRESET_MENU
            else:
                cls.current_menu = Constants.MAIN_MENU

        # handle toggle events settings input
        elif cls.current_menu == Constants.TOGGLE_EVENTS_MENU:
            if input_value == "b":
                cls.current_menu = Constants.MAIN_MENU
            elif input_value == "1":
                config[Constants.ENABLE_ALLY_DEATH] = (
                    not ConfigManager.enable_ally_death
                )
                ConfigManager.save(config)
                cls.current_menu = Constants.TOGGLE_EVENTS_MENU
            elif input_value == "2":
                config[Constants.ENABLE_ALLY_KILL] = not ConfigManager.enable_ally_kill
                ConfigManager.save(config)
                cls.current_menu = Constants.TOGGLE_EVENTS_MENU
            elif input_value == "3":
                config[Constants.ENABLE_SELF_DEATH] = (
                    not ConfigManager.enable_self_death
                )
                ConfigManager.save(config)
                cls.current_menu = Constants.TOGGLE_EVENTS_MENU
            elif input_value == "4":
                config[Constants.ENABLE_SELF_KILL] = not ConfigManager.enable_self_kill
                ConfigManager.save(config)
                cls.current_menu = Constants.TOGGLE_EVENTS_MENU
            else:
                cls.current_menu = Constants.TOGGLE_EVENTS_MENU

        # handle preset menu input
        elif cls.current_menu == Constants.PRESET_MENU:
            # get preset directories
            preset_directories = cls._get_presets_names()

            if input_value == "b":
                cls.current_menu = Constants.MAIN_MENU
            elif input_value == "n":
                new_preset_path = NewPreset.create()
                subprocess.Popen(["explorer", new_preset_path])
                cls.current_menu = Constants.PRESET_MENU
            elif input_value == "g":
                webbrowser.open(
                    "https://github.com/lukasmesserschmidt/LoL-Auto-Chat/blob/main/CreatingPresetsGuide.md"
                )
            elif input_value == "p":
                subprocess.Popen(["explorer", paths.get_presets_dir_path()])
                cls.current_menu = Constants.PRESET_MENU
            elif input_value.isdigit() and 0 < int(input_value) <= len(
                preset_directories
            ):
                config[Constants.CURRENT_PRESET_NAME] = preset_directories[
                    int(input_value) - 1
                ]
                ConfigManager.save(config)
                cls.current_menu = Constants.MAIN_MENU
            else:
                cls.current_menu = Constants.PRESET_MENU

        # handle waiting menu input
        elif cls.current_menu == Constants.WAITING_MENU:
            if input_value == "s":
                ChatManager.start()
                cls.current_menu = Constants.IN_GAME_MENU
            elif input_value == "b":
                LolLiveClientData.stop()
                cls.current_menu = Constants.MAIN_MENU

        # handle in game menu input
        elif cls.current_menu == Constants.IN_GAME_MENU:
            ChatManager.stop()
            LolLiveClientData.stop()
            cls.current_menu = Constants.MAIN_MENU

    @classmethod
    def load_current_menu(cls):
        """
        Loads the current menu.
        """
        if cls.current_menu == Constants.MAIN_MENU:
            cls._main_menu()
        elif cls.current_menu == Constants.TOGGLE_EVENTS_MENU:
            cls._toggle_events_menu()
        elif cls.current_menu == Constants.PRESET_MENU:
            cls._preset_menu()
        elif cls.current_menu == Constants.WAITING_MENU:
            cls._waiting_menu()
        elif cls.current_menu == Constants.IN_GAME_MENU:
            cls._in_game_menu()

    @classmethod
    def _main_menu(cls):
        """
        Loads the main menu.
        """
        # clear and write header
        os.system("cls" if os.name == "nt" else "clear")
        cls._write_header("Main Menu")
        print("(s) Start\n\n")

        # check if current preset exists and set current preset name
        current_preset_name = ConfigManager.current_preset_name
        current_preset_name = (
            current_preset_name
            if cls._preset_exists(current_preset_name)
            else "!!! No preset selected, cant start without preset !!!"
        )

        # write general settings
        cls._write_header("General Settings")
        print(
            f"(1) Temporarily remove used messages: {ConfigManager.remove_used_messages}\n"
        )
        print(
            f'(2) Write all messages in "/all" chat: {ConfigManager.use_all_chat}\n\n'
        )

        # write other settings
        cls._write_header("Other Settings")
        print("(3) Toggle Events Settings\n")
        print(f"(4) Message Presets Settings ({current_preset_name})\n\n")

        # write help
        if ConfigManager.show_help:
            cls._write_header("Help")
            print(
                'To change/select an option, type the symbol shown in the "()" and press Enter.\n'
            )
            print('Type "q" and press Enter to exit the program.\n\n')

    @classmethod
    def _toggle_events_menu(cls):
        """
        Loads the toggle events settings.
        """
        # clear and write header
        os.system("cls" if os.name == "nt" else "clear")
        cls._write_header("Toggle Events Settings")

        print(f'(1) Enable "ally death" event: {ConfigManager.enable_ally_death}\n')
        print(f'(2) Enable "ally kill" event: {ConfigManager.enable_ally_kill}\n')
        print(f'(3) Enable "self death" event: {ConfigManager.enable_self_death}\n')
        print(f'(4) Enable "self kill" event: {ConfigManager.enable_self_kill}\n\n')

        # write help
        if ConfigManager.show_help:
            cls._write_header("Help")
            print(
                'To change an option, type the number shown in the "()" and press Enter.\n'
            )
            print('Type "b" and press Enter to go back to the main menu.\n\n')

    @classmethod
    def _preset_menu(cls):
        """
        Loads the preset menu.
        """
        # get preset directories
        preset_directories = cls._get_presets_names()

        # clear and write header
        os.system("cls" if os.name == "nt" else "clear")
        cls._write_header("Message Preset Settings")

        # check if current preset exists and set current preset name
        current_preset_name = ConfigManager.current_preset_name
        current_preset_name = (
            current_preset_name
            if cls._preset_exists(current_preset_name)
            else "No preset selected"
        )

        # write current preset
        print(f"Current preset: {current_preset_name}\n\n")

        # write presets and option to create new preset
        for i, directory in enumerate(preset_directories):
            print(f"({i + 1}) {directory}\n")
        print("(n) Create new preset\n\n")

        # write help
        if ConfigManager.show_help:
            cls._write_header("Help")
            print(
                'To select a preset, type the number shown in the "()" and press Enter.\n'
            )
            print('Type "n" and press Enter to create a new preset.\n')
            print(
                'Type "g" and press Enter to open a guide on how to create presets.\n'
            )
            print('Type "p" and press Enter to open the presets folder.\n')
            print('Type "b" and press Enter to return to the main menu.\n')
            print('Type "q" and press Enter to exit the program.\n\n')

    @classmethod
    def _waiting_menu(cls):
        """
        Loads the waiting menu.
        """
        # clear and write waiting header
        os.system("cls" if os.name == "nt" else "clear")
        cls._write_header("Waiting for game to start...")
        print('Press "Enter" to stop the program and return to the main menu.')

    @classmethod
    def _in_game_menu(cls):
        """
        Loads the in-game menu.
        """
        # clear and write in-game header
        os.system("cls" if os.name == "nt" else "clear")
        cls._write_header("Game is running")
        print('Press "Enter" to stop the program and return to the main menu.')

    @classmethod
    def _write_header(cls, header: str):
        """
        Writes a header to the console and fills the rest of the line with dashes.
        """
        print(f"-- {header} " + "-" * (45 - len(header) - 4) + "\n")

    @classmethod
    def _write_default_input_section(cls):
        """
        Writes the Input header and the Help command to the console.
        """
        cls._write_header("Input")
        print('To show/hide "-- Help --", type "h" and press Enter.\n')

    @classmethod
    def _get_presets_names(cls):
        """
        Returns the preset directories.
        """
        presets_dir_path = paths.get_presets_dir_path()
        return [
            preset_name
            for preset_name in os.listdir(presets_dir_path)
            if os.path.isdir(os.path.join(presets_dir_path, preset_name))
        ]

    @classmethod
    def _preset_exists(cls, preset_name: str):
        """
        Checks if a preset exists.
        """
        return os.path.exists(os.path.join(paths.get_presets_dir_path(), preset_name))
