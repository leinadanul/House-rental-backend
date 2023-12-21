from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String



class Base(DeclarativeBase):
    pass

class LandlordRecords(Base):
    __tablename__ = 'landlord'

    id: Mapped[int] = mapped_column(primary_key=True,  nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    phone_number: Mapped[int] = mapped_column(nullable=False,)
    mobile_number: Mapped[int]
    company_name: Mapped[str] = mapped_column(String(100), nullable=False)
    picture: Mapped[str] = mapped_column(String(255), nullable=False)

