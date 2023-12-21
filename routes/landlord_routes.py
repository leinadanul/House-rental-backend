from fastapi import APIRouter
from services.LandlordServices import LandlordServices

class LandlordRoutesManager():
    def __init__(self, service: LandlordServices):
        self.service = service
    
    def get_router(self):
        router = APIRouter()
        router.add_api_route(
            path="/landlord", 
            methods=["POST"],
            endpoint=self.service.create_landlord
        )
        return router