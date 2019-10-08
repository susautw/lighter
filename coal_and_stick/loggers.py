import abc
from typing import List
from .trainer_state import TrainerState
from lighter.lighters.lighter import Lighter


class BaseLogger(metaclass=abc.ABCMeta):
    lighters: List[Lighter] = []

    def attach(self, lighter: Lighter):
        self.lighters.append(lighter)

    def detach(self, lighter: Lighter):
        self.lighters.remove(lighter)

    def notify(self):
        for lighter in self.lighters:
            lighter.update(self)

    @property
    @abc.abstractmethod
    def log(self):
        pass

    @abc.abstractmethod
    def add_log(self, state: TrainerState):
        pass


class Logger(BaseLogger):
    _logs = []

    @property
    def log(self):
        return self._logs

    def add_log(self, log):
        self._logs.append(log)
        self.notify()


        # TODO move to lighter
        # if not state.is_last_state():
        #     self.data_count += state.data.shape[0]
        #     self.total_loss += state.loss
        #     self.correct += self.predict_to_correct(state.predict, state.target)
        # else:
        #     self.accuracy = self.correct / self.data_count
        #     self.avg_loss = self.total_loss / self.data_count

        # @staticmethod
        # def predict_to_correct(predict, target):
        #     return predict.eq(target).sum().item()

#  TODO remove logger class
