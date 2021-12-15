from sqlalchemy import select, asc

from app.models.database import database
from app.models.humidity_records import humidity_records_table
from app.schemas.products import ProductCreate, ProductUpdate


async def get_products():
    query = (
        select(
            [
                humidity_records_table.c.id,
                humidity_records_table.c.name,
                humidity_records_table.c.calories,
                humidity_records_table.c.proteins,
                humidity_records_table.c.fats,
                humidity_records_table.c.carbs
            ]
        ).order_by(asc(humidity_records_table.c.id))
    )
    return await database.fetch_all(query)


async def find_product(product_id: int):
    query = (
        select(
            [
                humidity_records_table.c.id,
                humidity_records_table.c.name,
                humidity_records_table.c.calories,
                humidity_records_table.c.proteins,
                humidity_records_table.c.fats,
                humidity_records_table.c.carbs
            ]
        ).where(humidity_records_table.c.id == product_id)
    )
    return await database.fetch_one(query)


async def create_product(product: ProductCreate):
    query = (
        humidity_records_table.insert()
            .values(
            name=product.name,
            calories=product.calories,
            proteins=product.proteins,
            fats=product.fats,
            carbs=product.carbs
        )
    )

    product_id = await database.execute(query)
    return product_id


async def update_product(product_id: int, product: ProductUpdate):
    query = (
        humidity_records_table.update()
            .where(humidity_records_table.c.id == product_id)
            .values(
            name=product.name,
            calories=product.calories,
            proteins=product.proteins,
            fats=product.fats,
            carbs=product.carbs
        )
    )
    return await database.execute(query)
