from abc import ABC
from typing import List

from models.landlord import Landlord
from models.property import Property


class DatabaseManager(ABC):
    def insert_landlord(self, landlord: Landlord) -> Landlord:
        pass

    def add_property(self, property : Property) -> Property:
        pass