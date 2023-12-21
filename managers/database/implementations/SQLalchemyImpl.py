from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from models.Landlord import Landlord
from managers.database.implementations.models.Landlord import LandlordRecords
from managers.database.db_manager import DatabaseManager


class SqlalchemyDBManager(DatabaseManager):
    def __init__(self):
        SQLALCHEMY_DATABASE_URL = "postgresql://postgres:toor@localhost:5432/house_rental"
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL)


    def upsertLandlord(self, landlord: Landlord) -> Landlord:

        with Session(self.engine) as session:

            existing_landlord = session.query(LandlordRecords).get(landlord.id)
            if existing_landlord:
                existing_landlord.id = landlord.id  
            else:
                new_landlord = LandlordRecords(
                    id=landlord.id,
                    first_name=landlord.firstName,
                    last_name=landlord.lastName,
                    email=landlord.email,
                    phone_number=landlord.phoneNumber,
                    mobile_number=landlord.mobileNumber,
                    company_name=landlord.companyName,
                    picture=landlord.picture
                )
                session.add(new_landlord)
            session.commit()
        return landlord
