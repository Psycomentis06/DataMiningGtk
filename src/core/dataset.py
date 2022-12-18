from abc import ABC, abstractmethod

class Dataset(ABC):

    def __init__(self, name: str,**kwargs) -> None:
        super().__init__()

    def loadModel() -> object:
        pass

    def saveModel() -> None:
        pass

    @abstractmethod
    def getColumns() -> list:
        pass