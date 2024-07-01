import time
import threading


class ThreadBase:
    """
    This class is the base class for all classes that use threads.
    """

    # thread variables
    _terminate_flag = False
    _loop_thread = None

    @classmethod
    def start(cls):
        """
        Starts the loop thread, if it is not already running.
        """
        if cls._loop_thread is None:
            cls._terminate_flag = False
            cls._loop_thread = threading.Thread(target=cls._loop, daemon=True)
            cls._loop_thread.start()

    @classmethod
    def stop(cls):
        """
        Stops the loop thread, if it is running.
        """
        if cls._loop_thread is not None:
            cls._terminate_flag = True
            cls._loop_thread.join()
            cls._loop_thread = None

    @classmethod
    def wait(cls, wait_time: int | float):
        """
        Waits for the specified amount of time or until the thread is terminated.
        """
        end_time = time.time() + wait_time

        while time.time() < end_time and not cls._terminate_flag:
            time.sleep(0.01)

    @classmethod
    def _loop(cls):
        raise NotImplementedError
