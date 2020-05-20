from abc import ABC, abstractmethod
from core.port.persistence.base import IBaseRepository

class IDemandRepository(IBaseRepository):

    @abstractmethod
    def specific_method():
        raise NotImplementedError