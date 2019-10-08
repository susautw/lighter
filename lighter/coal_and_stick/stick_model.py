import torch
from torch import cuda
from torch.nn import Module
from torch.optim.optimizer import Optimizer
from torch.utils.data.dataloader import DataLoader
from . import BaseTrainer


class StickModel(Module):

    def __init__(
            self,
            model: Module,
            loss_fn,
            optimizer: Optimizer,
            trainer: BaseTrainer,
            device: torch.device = torch.device("cuda" if cuda.is_available() else "cpu")
    ):
        super().__init__()

        self.model = model
        self.loss_fn = loss_fn
        self.optimizer = optimizer
        self.trainer = trainer
        self.device = device

        self.model.to(device)

    def forward(self, x):
        return self.model(x)

    def fit(self, epochs, data_loader, test_loader):
        self.trainer.fit(self, epochs, data_loader, test_loader)

    def evaluate(self, data_loader):
        self.trainer.evaluate(self, data_loader)


def data_loader_factory(
        dataset, test_dataset, epochs=20, batch_size=1, shuffle=False, sampler=None,
        batch_sampler=None, num_workers=0, collate_fn=None,
        pin_memory=False, drop_last=False, timeout=0,
        worker_init_fn=None, multiprocessing_context=None
):
    loader_config = {'batch_size': batch_size,
                     'shuffle': shuffle,
                     'sampler': sampler,
                     'batch_sampler': batch_sampler,
                     'num_workers': num_workers,
                     'collate_fn': collate_fn,
                     'pin_memory': pin_memory,
                     'drop_last': drop_last,
                     'timeout': timeout,
                     'worker_init_fn': worker_init_fn,
                     'multiprocessing_context': multiprocessing_context
                     }
    data_loader = DataLoader(dataset=dataset, **loader_config)
    test_loader = DataLoader(dataset=test_dataset, **loader_config)

    return epochs, data_loader, test_loader
