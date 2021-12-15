from datetime import datetime

from pydantic import BaseModel


class LunchCreate(BaseModel):
    profile_id: int
    product_id: int
    date: datetime
    amount: int


class LunchUpdate(BaseModel):
    profile_id: int
    product_id: int
    date: datetime
    amount: int


class LunchModel(BaseModel):
    id: int
    profile_id: int
    product_id: int
    date: datetime
    amount: int
