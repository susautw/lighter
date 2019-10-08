from . import BatchInfo
from .. import BaseTrainer
from . import TrainerEvent


class BeforeTrainBatch(TrainerEvent):
    def __init__(self, trainer: BaseTrainer, number_of_batches: int):
        super().__init__(trainer)
        self._number_of_batches = number_of_batches

    @property
    def number_of_batches(self):
        return self._number_of_batches


class TrainingBatch(TrainerEvent):
    def __init__(self, trainer: BaseTrainer, batch_info: BatchInfo):
        super().__init__(trainer)
        self._batch_info = batch_info

    @property
    def batch_info(self):
        return self._batch_info


class AfterTrainBatch(TrainerEvent):
    pass
