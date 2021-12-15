from fastapi import APIRouter, HTTPException

from app.schemas.temperature import TemperatureRecord, TemperatureRecordCreate, TemperatureRecordUpdate
from app.utils import humidity as measure_utils

router = APIRouter()


@router.get("/measures")
async def measures_index():
    return await measure_utils.get_measures()


@router.post("/locations", response_model=TemperatureRecord, status_code=201)
async def measures_store(measure: TemperatureRecordCreate):
    measure_id = await measure_utils.create_measure(measure)

    return await measure_utils.find_measure(measure_id)


@router.get("/locations/{measure_id}", response_model=TemperatureRecord)
async def measures_show(measure_id: int):
    measure = await measure_utils.find_measure(measure_id)
    if measure:
        return measure
    else:
        raise HTTPException(status_code=404, detail="Measure not found")


@router.put("/locations/{measure_id}", response_model=TemperatureRecord)
async def measures_update(measure_id: int, measure_data: TemperatureRecordUpdate):
    measure = await measure_utils.find_measure(measure_id)
    if measure:
        await measure_utils.update_measure(measure_id, measure_data)
        return await measure_utils.find_measure(measure_id)
    else:
        raise HTTPException(status_code=404, detail="Measure not found")