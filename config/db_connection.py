from sqlalchemy import create_engine
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:toor@localhost:5432/house_rental"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
