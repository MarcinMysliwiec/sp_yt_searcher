from abc import abstractmethod
from .SpAuth import SpAuth


class Sp(SpAuth):
    def __init__(self):
        super(Sp, self).__init__()
        self.obj = dict()
        self.generic_data = dict()

        self.search()
        self.to_generic()

    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def to_generic(self):
        pass
