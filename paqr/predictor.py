from abc import ABC, abstractmethod


class PredictorInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def predict(self):
        """
        The main prediction method the model should implement to generate
        a single prediction. The inputs to this method will vary so are left unspecified
        """
