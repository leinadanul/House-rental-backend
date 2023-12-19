from pydantic import BaseModel

class landlord(BaseModel):
    id: int
    firstName: str
    lastName: str
    email: str
    phoneNumber: int
    mobileNumber: int
    companyName: str
    picture: str
