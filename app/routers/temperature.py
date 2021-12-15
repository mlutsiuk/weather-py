from fastapi import APIRouter, HTTPException

from app.schemas.pressure import ProfileModel, ProfileCreate, ProfileUpdate
from app.utils import temperature as profile_utils

router = APIRouter()


@router.get("/profiles")
async def profiles_index():
    return await profile_utils.get_profiles()
    # return {"message": "profiles:index"}


@router.post("/profiles", response_model=ProfileModel, status_code=201)
async def profiles_store(profile: ProfileCreate):
    profile_id = await profile_utils.create_profile(profile)

    return await profile_utils.find_profile(profile_id)


@router.get("/profiles/{profile_id}", response_model=ProfileModel)
async def profiles_show(profile_id: int):
    profile = await profile_utils.find_profile(profile_id)
    if profile:
        return profile
    else:
        raise HTTPException(status_code=404, detail="Profile not found")


@router.put("/profiles/{profile_id}", response_model=ProfileModel)
async def profiles_update(profile_id: int, profile_data: ProfileUpdate):
    profile = await profile_utils.find_profile(profile_id)
    if profile:
        await profile_utils.update_profile(profile_id, profile_data)
        return await profile_utils.find_profile(profile_id)
    else:
        raise HTTPException(status_code=404, detail="Profile not found")


@router.delete("/profiles/{profile_id}")
async def profiles_destroy(profile_id: int):
    return {"message": "profiles:destroy"}
