from fastapi import FastAPI
from managers.database.implementations.sqlalchemy_impl import SqlalchemyDBManager
from services.landlord_services import LandlordServices
from routes.landlord_routes import LandlordRoutesManager

app = FastAPI()

database_impl = SqlalchemyDBManager()

landLord_service = LandlordServices(database_impl) 

landlord_router = LandlordRoutesManager(landLord_service)

app.include_router(landlord_router.get_router())







