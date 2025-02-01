import uvicorn
from fastapi import FastAPI
from sqlalchemy import MetaData, inspect, Table, select

from core.models import db_helper

app = FastAPI()
engine = db_helper.get_engine()

metadata_obj = MetaData()

async with engine.connect() as conn:
    async_result = await conn.stream(select(t1))

    async for row in async_result:
        print("row: %s" % (row,))

if __name__ == '__main__':
    uvicorn.run("test:app")
