from abc import ABC
from typing import List

from models.Landlord import Landlord

class DatabaseManager (ABC):


    def upsertLandlord(self, landlord: Landlord)->Landlord:
        pass