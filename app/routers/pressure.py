from fastapi import APIRouter, HTTPException

from app.schemas.pressure import PressureRecord, PressureRecordCreate, PressureRecordUpdate
from app.utils import pressure as pressure_utils
from app.utils import location as location_utils

router = APIRouter()


@router.get("/locations/{location_id}/pressure-records")
async def location_pressure_records_index(location_id: int):
    location = await location_utils.get_one(location_id)
    if location:
        return await pressure_utils.get_all_location_pressure_records(location_id)
    else:
        raise HTTPException(status_code=404, detail="Location not found")


@router.post("/locations/{location_id}/pressure-records", response_model=PressureRecord, status_code=201)
async def pressure_records_store(location_id: int, pressure_record: PressureRecordCreate):
    pressure_record_id = await pressure_utils.create(location_id, pressure_record)

    return await pressure_utils.get_one(pressure_record_id)


@router.get("/pressure-records/{pressure_record_id}", response_model=PressureRecord)
async def pressure_records_show(pressure_record_id: int):
    pressure_record = await pressure_utils.get_one(pressure_record_id)
    if pressure_record:
        return pressure_record
    else:
        raise HTTPException(status_code=404, detail="Pressure record not found")


@router.put("/pressure-records/{pressure_record_id}", response_model=PressureRecord)
async def pressure_records_update(pressure_record_id: int, data: PressureRecordUpdate):
    pressure_record = await pressure_utils.get_one(pressure_record_id)
    if pressure_record:
        await pressure_utils.update(pressure_record_id, data)
        return await pressure_utils.get_one(pressure_record_id)
    else:
        raise HTTPException(status_code=404, detail="Pressure record not found")
