import abc
from typing import Type
from . import Event
from ..method_descriptor import MethodDescriptor, with_descriptor


class EventHandler(MethodDescriptor):
    def __init__(self, event_handler, event_type):
        super().__init__(event_handler)
        self._event_type = event_type

    @property
    def event_type(self):
        return self._event_type


class EventListener(metaclass=abc.ABCMeta):

    def __init__(self):
        self._handler_map = {}
        self._register_handler()

    def _register_handler(self):
        listeners = EventHandler.get_instance_methods(self)

        for listener in listeners:
            self.add_handler(listener.event_type, listener)

    def add_handler(self, event_type: Event, listener):
        if event_type in self._handler_map:
            self._handler_map[event_type].append(listener)
        else:
            self._handler_map[event_type] = [listener]

    def on_event(self, event: Event):
        for handler in self._handler_map[event.__class__]:
            handler(event)


def on(event_type: Type[Event]):
    return with_descriptor(EventHandler, event_type)
