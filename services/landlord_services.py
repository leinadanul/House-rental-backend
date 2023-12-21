from models.landlord import Landlord
from managers.database.db_manager import DatabaseManager

class LandlordServices():
    def __init__(self, database_manager: DatabaseManager  ):
        self.database_manager = database_manager


    def create_landlord(self, landlord: Landlord):
        self.database_manager.upsert_landlord(landlord)
        return landlord
