from sqlalchemy import create_engine, MetaData
from databases import Database

DB_URL = "sqlite:///./mysql/users.db"

database = Database(DB_URL)
metadata = MetaData()
engine = create_engine(DB_URL)
