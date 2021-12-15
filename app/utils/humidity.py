from sqlalchemy import select, asc

from app.models.database import database
from app.models.humidity_records import humidity_records_table
from app.schemas.humidity import HumidityRecord, HumidityRecordCreate, HumidityRecordUpdate


async def get_all_location_humidity_records(location_id: int):
    query = (
        select(
            [
                humidity_records_table.c.id,
                humidity_records_table.c.location_id,
                humidity_records_table.c.date,
                humidity_records_table.c.humidity
            ]
        ).where(humidity_records_table.c.location_id == location_id)
        .order_by(asc(humidity_records_table.c.id))
    )
    return await database.fetch_all(query)


async def get_one(humidity_record_id: int):
    query = (
        select(
            [
                humidity_records_table.c.id,
                humidity_records_table.c.location_id,
                humidity_records_table.c.date,
                humidity_records_table.c.humidity
            ]
        ).where(humidity_records_table.c.id == humidity_record_id)
    )
    return await database.fetch_one(query)


async def create(location_id: int, humidity_record: HumidityRecordCreate):
    query = (
        humidity_records_table.insert()
        .values(
            location_id=location_id,
            date=humidity_record.date,
            humidity=humidity_record.humidity
        )
    )

    humidity_record_id = await database.execute(query)
    return humidity_record_id


async def update(humidity_record_id: int, humidity_record: HumidityRecordUpdate):
    query = (
        humidity_records_table.update()
        .where(humidity_records_table.c.id == humidity_record_id)
        .values(
            location_id=humidity_record.location_id,
            date=humidity_record.date,
            humidity=humidity_record.humidity
        )
    )
    return await database.execute(query)
