from .lol_live_client_data import LolLiveClientData


class AllPlayerData:
    """
    This class provides the all players data from the live client data.
    """

    @classmethod
    def _get_all_players_data(cls):
        all_data = LolLiveClientData.all_data

        if all_data is None:
            return None

        return all_data.get("allPlayers")

    @classmethod
    def get_teams_player_names(cls):
        """
        Returns the player names of the players for each team.
        """
        all_players_data = cls._get_all_players_data()

        if all_players_data is None:
            return None

        teams_player_names = [[] for _ in range(2)]

        for player_data in all_players_data:
            team = player_data.get("team")
            player_name = player_data.get("riotIdGameName")

            if team == "ORDER":
                teams_player_names[0].append(player_name)
            elif team == "CHAOS":
                teams_player_names[1].append(player_name)

        return teams_player_names

    @classmethod
    def get_player_champion_name(cls, player_name: str):
        """
        Returns the champion name of the player with the given player name.
        """
        all_players_data = cls._get_all_players_data()

        if all_players_data is None:
            return None

        for player_data in all_players_data:
            if (
                player_data.get("riotIdGameName") == player_name
                or player_data.get("summonerName") == player_name
            ):
                return player_data.get("championName")

        return None
