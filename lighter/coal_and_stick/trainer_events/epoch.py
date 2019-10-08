from .. import BaseTrainer
from . import TrainerEvent


class BeforeEpoch(TrainerEvent):
    def __init__(self, trainer: BaseTrainer, epoch: int):
        super().__init__(trainer)
        self._epoch = epoch

    @property
    def epoch(self):
        return self._epoch


class AfterEpoch(TrainerEvent):
    pass
