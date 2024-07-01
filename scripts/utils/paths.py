import os

from .constants import Constants


def get_config_json_path():
    """
    Returns the absolute path of the config.json file.
    """
    return _get_abs_path(Constants.REL_CONFIG_JSON_PATH)


def get_presets_dir_path():
    """
    Returns the absolute path of the presets directory.
    """
    return _get_abs_path(Constants.REL_PRESETS_DIR_PATH)


def _get_abs_path(path: str):
    """
    Returns the absolute path of the given relative path, staring from the scripts directory.
    """
    scripts_dir_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.abspath(os.path.join(scripts_dir_path, path))
