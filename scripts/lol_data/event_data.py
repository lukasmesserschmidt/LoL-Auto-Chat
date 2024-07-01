from .lol_live_client_data import LolLiveClientData


class EventData:
    """
    This class provides the event data from the live client data.
    """

    @classmethod
    def _get_event_data(cls):
        all_data = LolLiveClientData.all_data

        if all_data is None:
            return None

        return all_data.get("events", {}).get("Events")

    @classmethod
    def get_events(cls, event_name: str):
        """
        Returns the events with the given event name.
        """
        event_data = cls._get_event_data()

        if event_data is None:
            return None

        return [event for event in event_data if event.get("EventName") == event_name]

    @classmethod
    def get_all_events(cls):
        """
        Returns all events.
        """
        return cls._get_event_data()
