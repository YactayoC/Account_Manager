from sqlalchemy import Table, Column, UniqueConstraint
from sqlalchemy.sql.sqltypes import Integer, String, Boolean

from config.db import meta, engine

users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("uid", String(255)),
    Column("fullname", String(255), nullable=False),
    Column("email", String(255), nullable=False, unique=True),
    Column("password", String(255), nullable=False),
    Column("keyConfirm", String(255)),
    Column("isConfirmed", Boolean, default=False),
    UniqueConstraint("email"),
)

meta.create_all(engine)
