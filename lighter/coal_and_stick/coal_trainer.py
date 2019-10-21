import torch
from torch.utils.data import DataLoader

from lighter.coal_and_stick.trainer_events import *
from . import StickModel
from . import BaseTrainer


class CoalTrainer(BaseTrainer):

    def fit(
            self,
            model: StickModel,
            epochs: int,
            data_loader: DataLoader,
            test_loader: DataLoader
    ):
        # before fit(model, epochs)
        self.dispatch(BeforeFit(self, model, epochs))

        for epoch in range(epochs):
            # before epoch(epoch)
            self.dispatch(BeforeEpoch(self, epoch))

            # before training batch(length of batches)
            self.dispatch(BeforeTrainBatch(self, len(data_loader)))
            for batch_info in self._train_one_epoch(model, data_loader):
                # training batch(batch_info)
                self.dispatch(TrainingBatch(self, batch_info))
            # after train batch
            self.dispatch(AfterTrainBatch(self))

            # before evaluating train_data(length of test_batch, length of test_dataset)
            self.dispatch(BeforeEvaluateTrainSet(self, len(data_loader), len(data_loader.dataset)))
            for batch_info in model.evaluate(data_loader):
                self.dispatch(EvaluatingTrainSet(self, batch_info))  # evaluating train_data(batch_info)
            # after evaluating train_data
            self.dispatch(AfterEvaluateTrainSet(self))

            # before evaluating test_data(length of test_batch, length of test_dataset)
            self.dispatch(BeforeEvaluateTestSet(self, len(data_loader), len(data_loader.dataset)))
            for batch_info in model.evaluate(test_loader):
                self.dispatch(EvaluatingTestSet(self, batch_info))  # evaluating test_data(batch_info)
            # after evaluating test_data
            self.dispatch(AfterEvaluateTestSet(self))

            # after epoch
            self.dispatch(AfterEpoch(self))

        # after fit
        self.dispatch(AfterFit(self))

    @torch.no_grad()
    def evaluate(
            self,
            model: StickModel,
            data_loader: DataLoader
    ):
        model.eval()

        for batch_id, (data, target) in enumerate(data_loader):
            data, target = data.to(model.device), target.to(model.device)
            predict = model(data)
            loss = model.loss_fn(predict, target)
            yield BatchInfo(batch_id, data, predict, loss, target)

    @staticmethod
    def _train_one_epoch(
                model: StickModel,
                data_loader: DataLoader
    ):
        model.train()
        for batch_id, (data, target) in enumerate(data_loader):
            data, target = data.to(model.device), target.to(model.device)

            model.optimizer.zero_grad()

            predict = model(data)
            loss = model.loss_fn(predict, target)
            loss.backward()

            model.optimizer.step()
            yield BatchInfo(batch_id, data, predict, loss, target)
