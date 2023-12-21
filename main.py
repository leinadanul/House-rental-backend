from fastapi import FastAPI
from managers.database.implementations.SQLalchemyImpl import SqlalchemyDBManager
from services.LandlordServices import LandlordServices
from routes.landlord_routes import LandlordRoutesManager

app = FastAPI()

database_impl = SqlalchemyDBManager()

landLordService = LandlordServices(database_impl) 

landlordRouter = LandlordRoutesManager(landLordService)

app.include_router(landlordRouter.get_router())







