class BatchInfo:
    def __init__(
            self,
            batch_id: int,
            data,
            predict,
            loss,
            target
    ):
        self._batch_id = batch_id
        self._data = data
        self._predict = predict
        self._loss = loss
        self._target = target

    @property
    def batch_id(self):
        return self._batch_id

    @property
    def data(self):
        return self._data

    @property
    def predict(self):
        return self._predict

    @property
    def loss(self):
        return self._loss

    @property
    def target(self):
        return self._target
