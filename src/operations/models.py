# создание таблиц от пользователя пользовательские эндоинта 
# models table операции 

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData

metadata = MetaData() # акумулирует информацию о созданных обьектов и алембик сопоставляет разницу с бд

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quantity", String),
    Column("figi", String),
    Column("instrument_type", String, nullable=True),
    Column("date", TIMESTAMP),
    Column("type", String),
)