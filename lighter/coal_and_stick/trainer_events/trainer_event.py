from .. import BaseTrainer
from ...events import Event


class TrainerEvent(Event):
    def __init__(self, trainer: BaseTrainer):
        super().__init__(trainer)
