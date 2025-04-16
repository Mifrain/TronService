from fastapi import FastAPI

from app.tron.router import router as tron_router

app = FastAPI()

app.include_router(tron_router)