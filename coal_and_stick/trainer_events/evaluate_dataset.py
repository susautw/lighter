from .. import BaseTrainer
from . import TrainerEvent, BatchInfo


class BeforeEvaluateDataSet(TrainerEvent):

    def __init__(self, trainer: BaseTrainer, number_of_batches: int, dataset_length: int):
        super().__init__(trainer)
        self._number_of_batches = number_of_batches
        self._dataset_length = dataset_length

    @property
    def number_of_batches(self):
        return self._number_of_batches

    @property
    def dataset_length(self):
        return self._dataset_length


class EvaluatingDataset(TrainerEvent):
    def __init__(self, trainer: BaseTrainer, batch_info: BatchInfo):
        super().__init__(trainer)
        self._batch_info = batch_info

    @property
    def batch_info(self):
        return self._batch_info


class AfterEvaluateDataSet(TrainerEvent):
    pass
