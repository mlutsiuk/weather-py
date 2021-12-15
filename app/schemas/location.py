from datetime import datetime

from pydantic import BaseModel


class LocationCreate(BaseModel):
    title: str
    longitude: float
    latitude: float


class LocationUpdate(BaseModel):
    title: str
    longitude: float
    latitude: float


class Location(BaseModel):
    id: int
    title: str
    longitude: float
    latitude: float
