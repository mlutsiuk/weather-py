from pydantic import BaseModel


class ProfileCreate(BaseModel):
    name: str
    target_calories: int
    target_proteins: int
    target_fats: int
    target_carbs: int


class ProfileUpdate(BaseModel):
    name: str
    target_calories: int
    target_proteins: int
    target_fats: int
    target_carbs: int


class ProfileModel(BaseModel):
    id: int
    name: str
    target_calories: int
    target_proteins: int
    target_fats: int
    target_carbs: int
