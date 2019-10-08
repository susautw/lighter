import abc
from ..events import EventListener


class Lighter(EventListener, metaclass=abc.ABCMeta):
    pass
