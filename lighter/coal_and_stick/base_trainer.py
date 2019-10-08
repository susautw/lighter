import abc
from torch.utils.data import DataLoader
from ..events import EventSource
from . import StickModel


class BaseTrainer(EventSource, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def fit(
            self,
            model: StickModel,
            epochs: int,
            data_loader: DataLoader,
            test_loader: DataLoader
    ):
        pass

    @abc.abstractmethod
    def evaluate(
            self,
            model: StickModel,
            data_loader: DataLoader
    ):
        pass

