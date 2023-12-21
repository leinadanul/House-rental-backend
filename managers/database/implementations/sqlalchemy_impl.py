from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from models.landlord import Landlord
from managers.database.implementations.models.landlord import LandlordRecords
from managers.database.db_manager import DatabaseManager


class SqlalchemyDBManager(DatabaseManager):
    def __init__(self):
        SQLALCHEMY_DATABASE_URL = "postgresql://postgres:toor@localhost:5432/house_rental"
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL)


    def upsert_landlord(self, landlord: Landlord) -> Landlord:

        with Session(self.engine) as session:

            existing_landlord = session.query(LandlordRecords).get(landlord.id)
            if existing_landlord:
                existing_landlord.id = landlord.id  
            else:
                new_landlord = LandlordRecords(
                    id=landlord.id,
                    first_name=landlord.first_name,
                    last_name=landlord.last_name,
                    email=landlord.email,
                    phone_number=landlord.phone_number,
                    mobile_number=landlord.mobile_number,
                    company_name=landlord.company_name,
                    picture=landlord.picture
                )
                session.add(new_landlord)
                session.commit()
        return landlord
