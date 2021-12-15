import sqlalchemy

from app.models.locations import locations_table

metadata = sqlalchemy.MetaData()

temperature_records_table = sqlalchemy.Table(
    "temperature_records",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("location_id", sqlalchemy.ForeignKey(locations_table.c.id)),
    sqlalchemy.Column("date", sqlalchemy.DateTime()),
    sqlalchemy.Column("temperature", sqlalchemy.Float)
)
