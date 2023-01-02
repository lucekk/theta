from abc import ABC, abstractclassmethod

class Method(ABC):

    @abstractclassmethod
    def _caluclations(self):
        pass

    @abstractclassmethod
    def get_method_data(self):
        pass