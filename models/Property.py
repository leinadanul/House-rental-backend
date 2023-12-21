from pydantic import BaseModel

class Property(BaseModel):
    Name: str
    propertyType: str
    location: str
    capacity: int
    propertyDistribution: str
    hostInfo: str
    characteristics: str
    description: str
    features:str
    unavailableDays: str
    price: int
    additionalFees: str