__all__ = ['Event', 'EventHandler', 'EventListener', 'EventSource', 'on']

Event = EventListener = EventHandler = EventSource = on = object.__class__

from .event import Event
from .event_listener import EventHandler, EventListener, on
from .event_source import EventSource
