from datetime import datetime

from pydantic import BaseModel


class MeasureCreate(BaseModel):
    profile_id: int
    date: datetime
    weight: float
    height: int


class MeasureUpdate(BaseModel):
    profile_id: int
    date: datetime
    weight: float
    height: int


class MeasureModel(BaseModel):
    id: int
    profile_id: int
    date: datetime
    weight: float
    height: int
