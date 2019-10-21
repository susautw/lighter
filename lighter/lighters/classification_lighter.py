from ..events import on
from ..coal_and_stick.trainer_events import *
from . import Lighter


class ClassificationVerboseLighter(Lighter):  # TODO fix this things
    def __init__(self):
        self.epoch = None

    @on(BeforeFit)
    def _remember_fit(self, event: BeforeFit):
        self.epochs = event.epochs

    @on(BeforeTrainBatch)
    def _remember_epoch(self, event: BeforeTrainBatch):
        self.epoch = event.epoch

    @on(TrainingBatch)
    def _rendering(self, event: TrainingBatch):
        if self._should_render():
            print('\rloss : %.4f  (%d / %d)' % (
                event.batch_info.loss,
                event.batch_info.batch_id,
                self.epochs
            ), end='')

    def _should_render(self):
        return self.epoch % 100 == 0

    @on(AfterTrainBatch)
    def _end_rendering(self):
        print()
