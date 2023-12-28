from pydantic import BaseModel


class Landlord(BaseModel):
    id: int | None = None
    first_name: str
    last_name: str
    email: str
    phone_number: int
    mobile_number: int
    company_name: str
    picture: str
