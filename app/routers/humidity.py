from fastapi import APIRouter, HTTPException

from app.schemas.profile import LunchModel, LunchCreate, LunchUpdate
from app.utils import location as lunch_utils
from app.utils import temperature as profile_utils

router = APIRouter()


@router.get("/lunches")
async def lunches_index():
    return await lunch_utils.get_lunches()


@router.get("/profiles/{profile_id}/lunches")
async def profile_lunches(profile_id: int):
    profile = await profile_utils.find_profile(profile_id)
    if profile:
        return await lunch_utils.get_profile_lunches(profile_id)
    else:
        raise HTTPException(status_code=404, detail="Profile not found")


@router.post("/lunches", response_model=LunchModel, status_code=201)
async def lunches_store(lunch: LunchCreate):
    lunch_id = await lunch_utils.create_lunch(lunch)

    return await lunch_utils.find_lunch(lunch_id)


@router.get("/lunches/{lunch_id}", response_model=LunchModel)
async def lunches_show(lunch_id: int):
    lunch = await lunch_utils.find_lunch(lunch_id)
    if lunch:
        return lunch
    else:
        raise HTTPException(status_code=404, detail="Lunch not found")


@router.put("/lunches/{lunch_id}", response_model=LunchModel)
async def lunches_update(lunch_id: int, lunch_data: LunchUpdate):
    lunch = await lunch_utils.find_lunch(lunch_id)
    if lunch:
        await lunch_utils.update_lunch(lunch_id, lunch_data)
        return await lunch_utils.find_lunch(lunch_id)
    else:
        raise HTTPException(status_code=404, detail="Lunch not found")


@router.delete("/lunches/{lunch_id}")
async def lunches_destroy(lunch_id: int):
    return {"message": "lunches:destroy"}
