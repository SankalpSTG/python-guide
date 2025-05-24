from email import message
from typing import Union

from dto.dto import ResponseType
from fastapi import FastAPI
from modules.auth.router import auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/", response_model=ResponseType[None])
def home():
    return ResponseType[None](status=200, message="Hello World")