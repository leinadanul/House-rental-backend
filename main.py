from typing import Union

from fastapi import FastAPI
from models import landlord

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/landlord_registred")
def create_landlord(landlord: landlord):
    return landlord
