from sqlalchemy import select, asc

from app.models.database import database
from app.models.temperature_records import temperature_records_table
from app.schemas.temperature import TemperatureRecordCreate, TemperatureRecordUpdate


async def get_measures():
    query = (
        select(
            [
                temperature_records_table.c.id,
                temperature_records_table.c.profile_id,
                temperature_records_table.c.date,
                temperature_records_table.c.height,
                temperature_records_table.c.weight
            ]
        ).order_by(asc(temperature_records_table.c.id))
    )
    return await database.fetch_all(query)


async def get_profile_measures(profile_id: int):
    query = (
        select(
            [
                temperature_records_table.c.id,
                temperature_records_table.c.profile_id,
                temperature_records_table.c.date,
                temperature_records_table.c.height,
                temperature_records_table.c.weight
            ]
        ).where(temperature_records_table.c.profile_id == profile_id)
            .order_by(asc(temperature_records_table.c.id))
    )
    return await database.fetch_all(query)


async def find_measure(measure_id: int):
    query = (
        select(
            [
                temperature_records_table.c.id,
                temperature_records_table.c.profile_id,
                temperature_records_table.c.date,
                temperature_records_table.c.height,
                temperature_records_table.c.weight
            ]
        ).where(temperature_records_table.c.id == measure_id)
    )
    return await database.fetch_one(query)


async def create_measure(measure: TemperatureRecordCreate):
    query = (
        temperature_records_table.insert()
            .values(
            profile_id=measure.profile_id,
            date=measure.date,
            weight=measure.weight,
            height=measure.height
        )
    )

    measure_id = await database.execute(query)
    return measure_id


async def update_measure(measure_id: int, measure: TemperatureRecordUpdate):
    query = (
        temperature_records_table.update()
            .where(temperature_records_table.c.id == measure_id)
            .values(
            profile_id=measure.profile_id,
            date=measure.date,
            height=measure.height,
            weight=measure.weight
        )
    )
    return await database.execute(query)
