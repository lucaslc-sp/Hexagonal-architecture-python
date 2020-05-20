from infra.persistence.base_repository import BaseRepository
from core.port.persistence.demand import IDemandRepository

class DemandRepository(BaseRepository, IDemandRepository):

    def specific_method(self):
        print('Only a specific method example')
    
    def get(self, )