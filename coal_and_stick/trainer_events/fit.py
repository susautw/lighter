from . import TrainerEvent
from .. import BaseTrainer
from .. import StickModel


class BeforeFit(TrainerEvent):
    def __init__(self, trainer: BaseTrainer, model: StickModel, epochs: int):
        super().__init__(trainer)
        self._model = model
        self._epochs = epochs

    @property
    def model(self):
        return self._model

    @property
    def epochs(self):
        return self._epochs


class AfterFit(TrainerEvent):
    pass
