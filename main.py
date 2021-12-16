from fastapi import FastAPI

from app.models.database import database
from app.routers import temperature, pressure, locations, humidity, plots, predict

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(temperature.router)
app.include_router(pressure.router)
app.include_router(locations.router)
app.include_router(humidity.router)
app.include_router(plots.router)
app.include_router(predict.router)
