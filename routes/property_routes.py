from fastapi import APIRouter
from services.property_services import PropertyService


class PropertyRoutesManager:
    def __init__(self, service: PropertyService):
        self.service = service

    def post_router(self):
        router = APIRouter()
        router.add_api_route(
            path="/property", methods=["POST"], endpoint=self.service.add_property
        )
        return router