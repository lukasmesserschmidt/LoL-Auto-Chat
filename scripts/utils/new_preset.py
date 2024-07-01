import os

from .constants import Constants
from . import paths


class NewPreset:
    """
    This class creates a new preset.
    """

    @classmethod
    def create(cls):
        """
        Creates a new preset folder with txt files, if it does not exist.
        """
        # get new preset path
        new_preset_path = os.path.join(
            paths.get_presets_dir_path(), Constants.NEW_PRESET_NAME
        )

        # create new preset if it does not exist
        if not os.path.exists(new_preset_path):
            # creates the new preset folder
            os.makedirs(new_preset_path, exist_ok=True)

            # get pahts to new txt files
            new_self_kill_txt = os.path.join(
                new_preset_path, f"{Constants.SELF_KILL}.txt"
            )
            new_self_death_txt = os.path.join(
                new_preset_path, f"{Constants.SELF_DEATH}.txt"
            )
            new_ally_kill_txt = os.path.join(
                new_preset_path, f"{Constants.ALLY_KILL}.txt"
            )
            new_ally_death_txt = os.path.join(
                new_preset_path, f"{Constants.ALLY_DEATH}.txt"
            )

            # create new txt files
            with open(new_self_kill_txt, "w", encoding="utf-8") as file:
                file.write("")

            with open(new_self_death_txt, "w", encoding="utf-8") as file:
                file.write("")

            with open(new_ally_kill_txt, "w", encoding="utf-8") as file:
                file.write("")

            with open(new_ally_death_txt, "w", encoding="utf-8") as file:
                file.write("")

        return new_preset_path
