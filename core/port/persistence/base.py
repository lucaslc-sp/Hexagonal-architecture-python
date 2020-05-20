from abc import ABC, abstractmethod
from typing import Any, List, Optional

from pydantic import BaseModel


class IBaseRepository(ABC):
    @abstractmethod
    async def list(
        self, limit: Optional[int], offset: Optional[int]
    ) -> List[BaseModel]:
        """ List all models """
        raise NotImplementedError()

    @abstractmethod
    async def get(self, id: Any) -> BaseModel:
        """ Get a single model by id """
        raise NotImplementedError()

    @abstractmethod
    async def create(self, model: BaseModel) -> BaseModel:
        """ Create a model """
        raise NotImplementedError()

    @abstractmethod
    async def update(self, model: BaseModel) -> BaseModel:
        """ Update a model """
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, model: BaseModel) -> None:
        """ Delete a model """
        raise NotImplementedError()
