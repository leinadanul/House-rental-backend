from models.property import Property
from managers.database.db_manager import DatabaseManager


class PropertyService:
    def __init__(self, database_manager: DatabaseManager):
        self.database_manager = database_manager


    def add_property(self, property: Property):
        return self.database_manager.add_property(property)
