from fastapi import APIRouter, HTTPException

from app.schemas.measures import MeasureModel, MeasureCreate, MeasureUpdate
from app.utils import measures as measure_utils
from app.utils import plots as plot_utils
from app.utils import profiles as profile_utils

router = APIRouter()


@router.get("/measures")
async def measures_index():
    return await measure_utils.get_measures()


@router.get("/profile/{profile_id}/measures")
async def profile_measures(profile_id: int):
    profile = await profile_utils.find_profile(profile_id)
    if profile:
        return await measure_utils.get_profile_measures(profile_id)
    else:
        raise HTTPException(status_code=404, detail="Profile not found")


@router.post("/measures", response_model=MeasureModel, status_code=201)
async def measures_store(measure: MeasureCreate):
    measure_id = await measure_utils.create_measure(measure)

    return await measure_utils.find_measure(measure_id)


@router.get("/measures/{measure_id}", response_model=MeasureModel)
async def measures_show(measure_id: int):
    measure = await measure_utils.find_measure(measure_id)
    if measure:
        return measure
    else:
        raise HTTPException(status_code=404, detail="Measure not found")


@router.put("/measures/{measure_id}", response_model=MeasureModel)
async def measures_update(measure_id: int, measure_data: MeasureUpdate):
    measure = await measure_utils.find_measure(measure_id)
    if measure:
        await measure_utils.update_measure(measure_id, measure_data)
        return await measure_utils.find_measure(measure_id)
    else:
        raise HTTPException(status_code=404, detail="Measure not found")


@router.delete("/measures/{measure_id}")
async def measures_destroy(measure_id: int):
    return {"message": "measures:destroy"}
