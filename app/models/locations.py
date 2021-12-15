import sqlalchemy

metadata = sqlalchemy.MetaData()

locations_table = sqlalchemy.Table(
    "locations",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(50)),
    sqlalchemy.Column("longitude", sqlalchemy.Float),
    sqlalchemy.Column("latitude", sqlalchemy.Float)
)
