from sqlalchemy import select, asc

from app.models.database import database
from app.models.locations import locations_table
from app.schemas.location import LocationCreate, LocationUpdate


async def get_all():
    query = (
        select(
            [
                locations_table.c.id,
                locations_table.c.title,
                locations_table.c.longitude,
                locations_table.c.latitude
            ]
        ).order_by(asc(locations_table.c.id))
    )
    return await database.fetch_all(query)


async def get_one(location_id: int):
    query = (
        select(
            [
                locations_table.c.id,
                locations_table.c.title,
                locations_table.c.longitude,
                locations_table.c.latitude
            ]
        ).where(locations_table.c.id == location_id)
    )
    return await database.fetch_one(query)


async def create(location: LocationCreate):
    query = (
        locations_table.insert()
        .values(
            title=location.title,
            longitude=location.longitude,
            latitude=location.latitude
        )
    )

    location_id = await database.execute(query)
    return location_id


async def update(location_id: int, location: LocationUpdate):
    query = (
        locations_table.update()
        .where(locations_table.c.id == location_id)
        .values(
            title=location.title,
            longitude=location.longitude,
            latitude=location.latitude
        )
    )
    return await database.execute(query)
