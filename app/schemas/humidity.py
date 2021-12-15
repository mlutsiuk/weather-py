from datetime import datetime

from pydantic import BaseModel


class HumidityRecordCreate(BaseModel):
    location_id: int
    date: datetime
    humidity: int


class HumidityRecordUpdate(BaseModel):
    location_id: int
    date: datetime
    humidity: int


class HumidityRecord(BaseModel):
    id: int
    location_id: int
    date: datetime
    humidity: int
