from fastapi import FastAPI
from managers.database.implementations.psycopg2_sql_impl import PsycopgDBManagerImpl

# from managers.database.implementations.sqlalchemy_impl import SqlalchemyDBManager
from services.landlord_services import LandlordServices
from services.property_services import PropertyService
from routes.landlord_routes import LandlordRoutesManager
from routes.property_routes import PropertyRoutesManager


app = FastAPI()

database_impl = PsycopgDBManagerImpl()
# database_impl = SqlalchemyDBManager()

landLord_service = LandlordServices(database_impl)
landlord_router = LandlordRoutesManager(landLord_service)
app.include_router(landlord_router.post_router())

property_service = PropertyService(database_impl)
property_router = PropertyRoutesManager(property_service)
app.include_router(property_router.post_router())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=5000)
