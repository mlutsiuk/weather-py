from sqlalchemy import select, asc, cast, Date
from sqlalchemy import func

from app.models.database import database
from app.models.locations import locations_table
from app.models.humidity_records import humidity_records_table
from app.schemas.location import LocationCreate, LocationUpdate


async def get_lunches():
    query = (
        select(
            [
                locations_table.c.id,
                locations_table.c.profile_id,
                locations_table.c.product_id,
                locations_table.c.date,
                locations_table.c.amount
            ]
        ).order_by(asc(locations_table.c.id))
    )
    return await database.fetch_all(query)


async def get_lunches_for_plot(profile_id: int):
    query = (
        select(
            [
                func.sum(humidity_records_table.c.calories * locations_table.c.amount / 100).label('calories'),
                func.sum(humidity_records_table.c.proteins * locations_table.c.amount / 100).label('proteins'),
                func.sum(humidity_records_table.c.fats * locations_table.c.amount / 100).label('fats'),
                func.sum(humidity_records_table.c.carbs * locations_table.c.amount / 100).label('carbs'),
                locations_table.c.date.cast(Date)
            ]
        ).join(humidity_records_table, locations_table.c.product_id == humidity_records_table.c.id)
        .where(locations_table.c.profile_id == profile_id)
        .group_by(locations_table.c.date.cast(Date))
        .order_by(asc(locations_table.c.date.cast(Date)))
    )
    return await database.fetch_all(query)


async def get_profile_lunches(profile_id: int):
    query = (
        select(
            [
                locations_table.c.id,
                locations_table.c.profile_id,
                locations_table.c.product_id,
                locations_table.c.date,
                locations_table.c.amount
            ]
        ).where(locations_table.c.profile_id == profile_id)
            .order_by(asc(locations_table.c.id))
    )
    return await database.fetch_all(query)


async def find_lunch(lunch_id: int):
    query = (
        select(
            [
                locations_table.c.id,
                locations_table.c.profile_id,
                locations_table.c.product_id,
                locations_table.c.date,
                locations_table.c.amount
            ]
        ).where(locations_table.c.id == lunch_id)
    )
    return await database.fetch_one(query)


async def create_lunch(lunch: LocationCreate):
    query = (
        locations_table.insert()
            .values(
            profile_id=lunch.profile_id,
            product_id=lunch.product_id,
            date=lunch.date,
            amount=lunch.amount
        )
    )

    lunch_id = await database.execute(query)
    return lunch_id


async def update_lunch(lunch_id: int, lunch: LocationUpdate):
    query = (
        locations_table.update()
            .where(locations_table.c.id == lunch_id)
            .values(
            profile_id=lunch.profile_id,
            product_id=lunch.product_id,
            date=lunch.date,
            amount=lunch.amount
        )
    )
    return await database.execute(query)
