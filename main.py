from fastapi import FastAPI

from app.models.database import database
from app.routers import temperature, pressure, locations, humidity, plots

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(profiles.router)
app.include_router(products.router)
app.include_router(measures.router)
app.include_router(lunches.router)
app.include_router(plots.router)
