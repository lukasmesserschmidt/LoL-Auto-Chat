import warnings
from contextlib import suppress
import requests

from ..utils.thread_base import ThreadBase
from ..utils.constants import Constants


class LolLiveClientData(ThreadBase):
    """
    This class requests the live client data from League of Legends.
    """

    # url for the live client data
    _url = "https://127.0.0.1:2999/liveclientdata/allgamedata"

    # current live client data
    all_data: dict = None

    # thread control
    @classmethod
    def stop(cls):
        """
        Stops the request loop thread, if it is running.
        """
        super().stop()
        cls.all_data = None

    # request loop thread
    @classmethod
    def _loop(cls):
        warnings.simplefilter("ignore")

        while not cls._terminate_flag:
            with suppress(Exception):
                response = requests.get(cls._url, verify=False, timeout=1)
                cls.all_data = response.json()

            cls.wait(Constants.INTERVAL)
