from abc import abstractmethod

from .SpAuth import SpAuth


class Sp(SpAuth):
    def __init__(self):
        super(Sp, self).__init__()
        self.data = self.search()

    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def to_generic(self):
        pass
