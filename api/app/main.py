from typing import List

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://0.0.0.0:8080",
]

DATABASE_URL = "postgresql://username:secret@db:5432/database"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

flow_records = sqlalchemy.Table(
    "nl_de_flow",
    metadata,
    sqlalchemy.Column("index", sqlalchemy.DateTime(timezone=True), primary_key=True),
    sqlalchemy.Column("value", sqlalchemy.Numeric),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)


class FlowRecord(BaseModel):
    index: datetime
    value: int = None


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/", response_model=List[FlowRecord])
async def read_notes(start: str, end: str):
    query = flow_records.select().where(
        flow_records.c.index.between(datetime.fromisoformat(start), datetime.fromisoformat(end)))
    return await database.fetch_all(query)
