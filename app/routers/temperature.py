from fastapi import APIRouter, HTTPException

from app.schemas.temperature import TemperatureRecord, TemperatureRecordCreate, TemperatureRecordUpdate
from app.utils import temperature as temperature_utils
from app.utils import location as location_utils

router = APIRouter()


@router.get("/locations/{location_id}/temperature-records")
async def location_temperature_records_index(location_id: int):
    location = await location_utils.get_one(location_id)
    if location:
        return await temperature_utils.get_all_location_temperature_records(location_id)
    else:
        raise HTTPException(status_code=404, detail="Location not found")


@router.post("/locations/{location_id}/temperature-records", response_model=TemperatureRecord, status_code=201)
async def temperature_records_store(location_id: int, temperature_record: TemperatureRecordCreate):
    temperature_record_id = await temperature_utils.create(location_id, temperature_record)

    return await temperature_utils.get_one(temperature_record_id)


@router.get("/temperature-records/{temperature_record_id}", response_model=TemperatureRecord)
async def temperature_records_show(temperature_record_id: int):
    temperature_record = await temperature_utils.get_one(temperature_record_id)
    if temperature_record:
        return temperature_record
    else:
        raise HTTPException(status_code=404, detail="Temperature record not found")


@router.put("/temperature-records/{temperature_record_id}", response_model=TemperatureRecord)
async def temperature_records_update(temperature_record_id: int, data: TemperatureRecordUpdate):
    temperature_record = await temperature_utils.get_one(temperature_record_id)
    if temperature_record:
        await temperature_utils.update(temperature_record_id, data)
        return await temperature_utils.get_one(temperature_record_id)
    else:
        raise HTTPException(status_code=404, detail="Temperature record not found")
