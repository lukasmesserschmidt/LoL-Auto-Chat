from .lol_live_client_data import LolLiveClientData
from .all_player_data import AllPlayerData


class ActivePlayerData:
    """
    This class provides the active player data from the live client data.
    """

    @classmethod
    def _get_active_player_data(cls):
        all_data = LolLiveClientData.all_data

        if all_data is None:
            return None

        return all_data.get("activePlayer")

    @classmethod
    def get_active_player_name(cls):
        """
        Returns the name of the active player.
        """
        active_player_data = cls._get_active_player_data()

        if active_player_data is None:
            return None

        return active_player_data.get("riotIdGameName")

    @classmethod
    def get_team_player_names(cls, is_ally: bool):
        """
        Returns the names of the players in the specified team.
        """
        active_player_name = cls.get_active_player_name()
        teams_player_names = AllPlayerData.get_teams_player_names()

        if active_player_name is None or teams_player_names is None:
            return None

        for team in teams_player_names:
            if (is_ally and active_player_name in team) or (
                not is_ally and active_player_name not in team
            ):
                return team

        return None
