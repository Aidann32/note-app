from sqlalchemy import Table, Column, Integer, String, MetaData, Text, DateTime
from sqlalchemy.sql import func

meta = MetaData()

notes = Table(
    'notes', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('text', Text),
    Column('created_at', DateTime(timezone=True), server_default=func.now()),
    Column('updated_at', DateTime(timezone=True), onupdate=func.now()),
)