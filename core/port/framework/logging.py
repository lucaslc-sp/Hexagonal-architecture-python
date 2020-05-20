from abc import ABC, abstractmethod

class Logging(ABC):

    @abstractmethod
    def info(msg):
        raise NotImplementedError
    
    @abstractmethod
    def debug(msg):
        raise NotImplementedError
    