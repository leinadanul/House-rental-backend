from abc import ABC
from typing import List

from models.landlord import Landlord

class DatabaseManager (ABC):


    def upsert_landlord(self, landlord: Landlord)->Landlord:
        pass