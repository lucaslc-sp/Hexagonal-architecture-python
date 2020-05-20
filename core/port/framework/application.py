from abc import ABC, abstractmethod

class IApplication(ABC):
    
    @abstractmethod
    def start(config):
        raise NotImplementedError
    
    @abstractmethod
    def logging():
        raise NotImplementedError
    
    @abstractmethod
    def router():
        raise NotImplementedError