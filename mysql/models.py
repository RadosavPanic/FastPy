from sqlalchemy import Table, Column, Integer, String
from mysql.db import metadata

users = Table("users", 
              metadata, 
              Column("id", Integer, primary_key=True), 
              Column("username", String(50), unique=True, nullable=False, index=True),
              Column("password", String)
              )