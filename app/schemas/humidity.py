from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    calories: int
    proteins: int
    fats: int
    carbs: int


class ProductUpdate(BaseModel):
    name: str
    calories: int
    proteins: int
    fats: int
    carbs: int


class ProductModel(BaseModel):
    id: int
    name: str
    calories: int
    proteins: int
    fats: int
    carbs: int
