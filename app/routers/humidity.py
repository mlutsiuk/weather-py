from fastapi import APIRouter, HTTPException

from app.schemas.humidity import HumidityRecord, HumidityRecordCreate, HumidityRecordUpdate
from app.utils import humidity as humidity_utils
from app.utils import location as location_utils

router = APIRouter()


@router.get("/locations/{location_id}/humidity-records")
async def location_humidity_records_index(location_id: int):
    location = await location_utils.get_one(location_id)
    if location:
        return await humidity_utils.get_all_location_humidity_records(location_id)
    else:
        raise HTTPException(status_code=404, detail="Location not found")


@router.post("/locations/{location_id}/humidity-records", response_model=HumidityRecord, status_code=201)
async def humidity_records_store(location_id: int, humidity_record: HumidityRecordCreate):
    humidity_record_id = await humidity_utils.create(location_id, humidity_record)

    return await location_utils.get_one(humidity_record_id)


@router.get("/humidity-records/{humidity_record_id}", response_model=HumidityRecord)
async def humidity_records_show(humidity_record_id: int):
    humidity_record = await humidity_utils.get_one(humidity_record_id)
    if humidity_record:
        return humidity_record
    else:
        raise HTTPException(status_code=404, detail="Humidity record not found")


@router.put("/humidity-records/{humidity_record_id}", response_model=HumidityRecord)
async def humidity_records_update(humidity_record_id: int, data: HumidityRecordUpdate):
    humidity_record = await humidity_utils.get_one(humidity_record_id)
    if humidity_record:
        await humidity_utils.update(humidity_record_id, data)
        return await humidity_utils.get_one(humidity_record_id)
    else:
        raise HTTPException(status_code=404, detail="Humidity record not found")
