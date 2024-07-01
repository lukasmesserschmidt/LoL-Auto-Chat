from scripts.lol_data.lol_live_client_data import LolLiveClientData
from scripts.managers.chat_manager import ChatManager
from scripts.ui.console_ui import ConsoleUi
from scripts.managers.config_manager import ConfigManager


def main():
    """
    Calls the main menu function of the ConsoleUi class.
    """
    # init config
    config = ConfigManager.load()
    ConfigManager.update_current_config_values(config)

    # init console ui
    ConsoleUi.load_current_menu()

    while True:
        # get user input
        input_value = ConsoleUi.get_input()

        # handle user input
        if input_value == "q":
            break
        ConsoleUi.handle_input(input_value)

        # load/update current menu
        ConsoleUi.load_current_menu()

    # stop threads if they are running
    ChatManager.stop()
    LolLiveClientData.stop()


if __name__ == "__main__":
    main()
