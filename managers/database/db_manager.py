from abc import ABC
from typing import List

from models.landlord import Landlord

class DatabaseManager (ABC):


    def insert_landlord(self, landlord: Landlord)->Landlord:
        pass