"""
    All the entities that we should have in the domain
"""
from datetime import datetime

from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Customer(BaseModel):
    def __init__(self, id: str, zipcode: Optional[str]):
        self.id = id,
        self.zipcode = zipcode

class Demand(BaseModel):
    def __init__(self,
            product: Product,
            customer: Customer,
            branch: Branch,
            date: datetime,
            status: str = "VIEW"):
        self.product = product
        self.customer = customer
        self.date = date
        self.status = status
