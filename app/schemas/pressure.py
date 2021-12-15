from datetime import datetime

from pydantic import BaseModel


class PressureRecordCreate(BaseModel):
    location_id: int
    date: datetime
    pressure: int


class PressureRecordUpdate(BaseModel):
    location_id: int
    date: datetime
    pressure: int


class PressureRecord(BaseModel):
    id: int
    location_id: int
    date: datetime
    pressure: int
