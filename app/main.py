from fastapi import FastAPI
from app.routes import api
import asyncio

app = FastAPI()

app.include_router(api.router, prefix="/api", tags=["API"])
