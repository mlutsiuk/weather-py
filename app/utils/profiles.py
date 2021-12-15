from sqlalchemy import select, asc

from app.models.database import database
from app.models.pressure_records import pressure_records_table
from app.schemas.profiles import ProfileCreate, ProfileUpdate


async def get_profiles():
    query = (
        select(
            [
                pressure_records_table.c.id,
                pressure_records_table.c.name,
                pressure_records_table.c.target_calories,
                pressure_records_table.c.target_proteins,
                pressure_records_table.c.target_fats,
                pressure_records_table.c.target_carbs
            ]
        ).order_by(asc(pressure_records_table.c.id))
    )
    return await database.fetch_all(query)


async def find_profile(profile_id: int):
    query = (
        select(
            [
                pressure_records_table.c.id,
                pressure_records_table.c.name,
                pressure_records_table.c.target_calories,
                pressure_records_table.c.target_proteins,
                pressure_records_table.c.target_fats,
                pressure_records_table.c.target_carbs
            ]
        ).where(pressure_records_table.c.id == profile_id)
    )
    return await database.fetch_one(query)


async def create_profile(profile: ProfileCreate):
    query = (
        pressure_records_table.insert()
            .values(
            name=profile.name,
            target_calories=profile.target_calories,
            target_proteins=profile.target_proteins,
            target_fats=profile.target_fats,
            target_carbs=profile.target_carbs
        )
    )

    profile_id = await database.execute(query)
    return profile_id


async def update_profile(profile_id: int, profile: ProfileUpdate):
    query = (
        pressure_records_table.update()
            .where(pressure_records_table.c.id == profile_id)
            .values(
            name=profile.name,
            target_calories=profile.target_calories,
            target_proteins=profile.target_proteins,
            target_fats=profile.target_fats,
            target_carbs=profile.target_carbs
        )
    )
    return await database.execute(query)
