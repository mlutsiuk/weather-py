from fastapi import APIRouter, HTTPException

from app.schemas.location import Location, LocationCreate, LocationUpdate
from app.utils import location as location_utils

router = APIRouter()


@router.get("/locations")
async def locations_index():
    return await location_utils.get_all()


@router.post("/locations", response_model=Location, status_code=201)
async def locations_store(location: LocationCreate):
    location_id = await location_utils.create(location)

    return await location_utils.get_one(location_id)


@router.get("/locations/{location_id}", response_model=Location)
async def locations_show(location_id: int):
    location = await location_utils.get_one(location_id)
    if location:
        return location
    else:
        raise HTTPException(status_code=404, detail="Location not found")


@router.put("/locations/{location_id}", response_model=Location)
async def locations_update(location_id: int, data: LocationUpdate):
    measure = await location_utils.get_one(location_id)
    if measure:
        await location_utils.update(location_id, data)
        return await location_utils.get_one(location_id)
    else:
        raise HTTPException(status_code=404, detail="Location not found")
