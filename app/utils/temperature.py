from sqlalchemy import select, asc

from app.models.database import database
from app.models.temperature_records import temperature_records_table
from app.schemas.temperature import TemperatureRecordCreate, TemperatureRecordUpdate


async def get_all_location_temperature_records(location_id: int):
    query = (
        select(
            [
                temperature_records_table.c.id,
                temperature_records_table.c.location_id,
                temperature_records_table.c.date,
                temperature_records_table.c.temperature
            ]
        ).where(temperature_records_table.c.location_id == location_id)
        .order_by(asc(temperature_records_table.c.id))
    )
    return await database.fetch_all(query)


async def get_one(temperature_record_id: int):
    query = (
        select(
            [
                temperature_records_table.c.id,
                temperature_records_table.c.location_id,
                temperature_records_table.c.date,
                temperature_records_table.c.temperature
            ]
        ).where(temperature_records_table.c.id == temperature_record_id)
    )
    return await database.fetch_one(query)


async def create(location_id: int, temperature_record: TemperatureRecordCreate):
    query = (
        temperature_records_table.insert()
        .values(
            location_id=location_id,
            date=temperature_record.date,
            temperature=temperature_record.temperature
        )
    )

    temperature_record_id = await database.execute(query)
    return temperature_record_id


async def update(temperature_record_id: int, temperature_record: TemperatureRecordUpdate):
    query = (
        temperature_records_table.update()
        .where(temperature_records_table.c.id == temperature_record_id)
        .values(
            location_id=temperature_record.location_id,
            date=temperature_record.date,
            temperature=temperature_record.temperature
        )
    )
    return await database.execute(query)
