"""
    Template Method is a behavioral design pattern that defines the skeleton of an algorithm in 
    the superclass but lets subclasses override specific steps of the algorithm without changing 
    its structure.

    https://refactoring.guru/design-patterns/template-method
"""
from backend.server import app
from core.port.persistence.base import IBaseRepository

# :: MongoDB Implementation
class BaseRepository(IBaseRepository):

    database: Database = inject.attr(Database)
    collection: AsyncIOMotorCollection

    async def list(
        self, limit: Optional[int], offset: Optional[int]
    ) -> List[BaseModel]:
        result = await self.collection.find().skip(offset).limit(limit).to_list(limit)
        return result

    async def get(self, id: Any) -> BaseModel:
        result = await self.collection.find_one({"_id": id})
        return result

    async def create(self, model: BaseModel) -> BaseModel:
        result = await self.collection.insert_one(model.dict())
        return result

    async def update(self, id: Any, model: BaseModel) -> BaseModel:
        result = await self.collection.find_one_and_update({"_id": id}, {"$set": model.dict()}, return_document=True)
        return result

    async def delete(self, id: Any) -> None:
        await self.collection.delete_one({"_id": id})
