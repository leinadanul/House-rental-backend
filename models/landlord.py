from pydantic import BaseModel


class Landlord(BaseModel):
    id: int | None = None
    first_name: str
    last_name: str
    email: str
    phone_number: int
    company_number: int | None = None
    company_name: str | None = None
    picture: str | None = None
