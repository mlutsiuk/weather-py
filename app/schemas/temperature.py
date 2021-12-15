from datetime import datetime

from pydantic import BaseModel


class TemperatureRecordCreate(BaseModel):
    date: datetime
    temperature: int


class TemperatureRecordUpdate(BaseModel):
    location_id: int
    date: datetime
    temperature: int


class TemperatureRecord(BaseModel):
    id: int
    location_id: int
    date: datetime
    temperature: int
