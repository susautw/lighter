import abc
from typing import List

from . import EventListener
from . import Event


class EventSource(metaclass=abc.ABCMeta):
    def __init__(self):
        self._listeners: List[EventListener] = []
        self._event = None

    def add_event_listener(self, event_listener: EventListener):
        self._listeners.append(event_listener)

    def remove_event_listener(self, event_listener: EventListener):
        self._listeners.remove(event_listener)

    def _notify(self):
        for listener in self._listeners:
            listener.on_event(self._event)

    def dispatch(self, event: Event):
        self._event = event
        self._notify()
