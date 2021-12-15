import databases

DB_USER = "root"
DB_PASS = "root"
DB_NAME = "weather-py"
DB_HOST = "127.0.0.1"
DB_PORT = "3306"

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

database = databases.Database(SQLALCHEMY_DATABASE_URL)
