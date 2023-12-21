from models.Landlord import Landlord
from managers.database.db_manager import DatabaseManager

class LandlordServices():
    def __init__(self, databaseManager: DatabaseManager  ):
        self.databaseManager = databaseManager


    def create_landlord(self, landlord: Landlord):
        self.databaseManager.upsertLandlord(landlord)
        return landlord
