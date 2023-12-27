"""from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine, engine, Table, MetaData, Column, Integer, String

from sqlalchemy import String



class Base(DeclarativeBase):

        landlord_table = Table(
            'landlord', metadata,
            Column('id', Integer, primary_key=True),
            Column('first_name', String, nullable= False),
            Column('last_name', String, nullable=False),
            Column('email', String, nullable=False),
            Column('phone_number', Integer, nullable=False),
            Column('mobile_number', Integer),
            Column('company_name', String, nullable=False),
            Column('picture', String, nullable=False)
        )




class LandlordRecords(Base):
    __tablename__ = 'landlord'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    phone_number: Mapped[int] = mapped_column(nullable=False,)
    mobile_number: Mapped[int]
    company_name: Mapped[str] = mapped_column(String(100), nullable=False)
    picture: Mapped[str] = mapped_column(String(255), nullable=False)

"""
