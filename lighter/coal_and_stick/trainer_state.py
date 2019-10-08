# TODO change State separate from type
# i.e. EndState, TrainerState, EpochState,...
# make a closure ,
# it can check the type of state, and execute the function if the type is correct.
# i.e. @on(EndState) # maybe implement it at lighter.
#      def end_state: ...


class TrainerState:

    def __init__(
            self,
            data=None,
            predict=None,
            loss=None,
            target=None,
            is_last_state=False
    ):
        self._data = data
        self._predict = predict
        self._loss = loss
        self._target = target
        self._is_last_state = is_last_state

    @staticmethod
    def last_state():
        return TrainerState(is_last_state=True)

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

    def is_last_state(self):
        return self._is_last_state

