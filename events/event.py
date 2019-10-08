import abc


class Event(metaclass=abc.ABCMeta):
    def __init__(self, source):
        self._source = source

    @property
    def source(self):
        return self._source
