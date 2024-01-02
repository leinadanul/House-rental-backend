from typing import List
from pydantic import BaseModel

class Fees(BaseModel):
    id: int | None = None
    name: str
    description: str
    price: int

class Distributions(BaseModel):
    id: int | None = None
    name: str
    description: str
    quantity: int

class Features(BaseModel):
    id: int | None = None
    name: str
    icon: str


class Host(BaseModel):
    id: int | None = None
    name: str
    phone_number: int
    email: str 

class PropertyTypes(BaseModel):
    id: int | None = None
    name: str
    description: str



class Property(BaseModel):

    id: int | None = None
    name: str
    country: str
    state: str
    city: str
    address: str
    capacity: int
    unavailable_days: str
    description: str
    price: int 
    host: Host 
    landlord_id: int
    fees: List[Fees]
    features: list[Features]
    distributions: list[Distributions]
    property_type: PropertyTypes 

