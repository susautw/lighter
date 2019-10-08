import abc
from lighter.events import EventListener


class Lighter(EventListener, metaclass=abc.ABCMeta):
    pass
