__all__ = ['StickModel', 'BaseTrainer', 'CoalTrainer']

StickModel = BaseTrainer = CoalTrainer = object.__class__

from .stick_model import StickModel
from .base_trainer import BaseTrainer
from .coal_trainer import CoalTrainer

