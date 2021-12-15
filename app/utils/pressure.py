from sqlalchemy import select, asc

from app.models.database import database
from app.models.pressure_records import pressure_records_table
from app.schemas.pressure import PressureRecordCreate, PressureRecordUpdate


async def get_all_location_pressure_records(location_id: int):
    query = (
        select(
            [
                pressure_records_table.c.id,
                pressure_records_table.c.location_id,
                pressure_records_table.c.date,
                pressure_records_table.c.pressure
            ]
        ).where(pressure_records_table.c.location_id == location_id)
        .order_by(asc(pressure_records_table.c.id))
    )
    return await database.fetch_all(query)


async def get_one(pressure_record_id: int):
    query = (
        select(
            [
                pressure_records_table.c.id,
                pressure_records_table.c.location_id,
                pressure_records_table.c.date,
                pressure_records_table.c.pressure
            ]
        ).where(pressure_records_table.c.id == pressure_record_id)
    )
    return await database.fetch_one(query)


async def create(location_id: int, pressure_record: PressureRecordCreate):
    query = (
        pressure_records_table.insert()
        .values(
            location_id=location_id,
            date=pressure_record.date,
            pressure=pressure_record.pressure
        )
    )

    pressure_record_id = await database.execute(query)
    return pressure_record_id


async def update(pressure_record_id: int, pressure_record: PressureRecordUpdate):
    query = (
        pressure_records_table.update()
        .where(pressure_records_table.c.id == pressure_record_id)
        .values(
            location_id=pressure_record.location_id,
            date=pressure_record.date,
            pressure=pressure_record.pressure
        )
    )
    return await database.execute(query)
