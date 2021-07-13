from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):

    @abstractmethod
    def findAll(self):
        pass

    @abstractmethod
    def findById(self,id):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def update(self,id):
        pass

    @abstractmethod
    def delete(self,id):
        pass