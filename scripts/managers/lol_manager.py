import win32gui

from ..lol_data.event_data import EventData


class LolManager:

    @classmethod
    def is_lol_running(cls):
        """
        Checks if League of Legends is running.
        """
        game_start = EventData.get_events("GameStart")
        game_end = EventData.get_events("GameEnd")

        if game_start is None or game_end is None:
            return False

        if (
            len(game_start) == 1
            and len(game_end) == 0
            and win32gui.IsWindow(cls._get_hwnd())
        ):
            return True

        return False

    @classmethod
    def is_lol_foreground(cls):
        """
        Checks if the League of Legends window is in the foreground.
        """
        return win32gui.GetForegroundWindow() == cls._get_hwnd()

    @classmethod
    def _get_hwnd(cls):
        return win32gui.FindWindow("RiotWindowClass", "League of Legends (TM) Client")
