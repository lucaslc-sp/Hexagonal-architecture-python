import inject

from core.port.persistence.demand import IDemandRepository
from core.domain.entities import Demand

class Demand:

    @inject.autoparams()
    def __init__(self, database: IDemandRepository):
        self.__database = database
    
    def save(self, demand):
        # :: If demand exists, update, otherwise, create.
        exists = self.__database.get()
        self.__database.update(demand) if exists else self.__database.create(demand)
        
        return self.__database.create(demand)

    def search(self) -> Demand:
        return self.__database.list()

    def grouped_search(self):
        return self.__database.list()
