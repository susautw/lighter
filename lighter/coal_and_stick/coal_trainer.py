import torch
from torch.utils.data import DataLoader
from . import StickModel
from . import BaseTrainer


class CoalTrainer(BaseTrainer):  # TODO replace logger with Events

    def fit(
            self,
            model: StickModel,
            epochs: int,
            data_loader: DataLoader,
            test_loader: DataLoader
    ):
        # before fit (model, epochs)
        for epoch in range(epochs):
            # before epoch(epoch)

            # before train batch(length of train_batch)
            for batch_info in self._train_one_epoch(model, data_loader):
                pass  # train batch (batch_info)
            # after train batch

            # before evaluating train_data(length of train_batch, length of train_dataset)
            for batch_info in model.evaluate(data_loader):
                pass  # evaluating train_data(batch_info)
            # after evaluating train_data

            # before evaluating test_data(length of test_batch, length of test_dataset)
            for batch_info in model.evaluate(test_loader):
                pass  # evaluating test_data(batch_info)
            # after evaluating test_data

            # after epoch

        # after fit

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
            yield batch_id, data, predict, loss, target  # TODO refactor with class "BatchInfo"

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
            yield batch_id, data, predict, loss, target
