from sqlalchemy import (
    MetaData, Table, Column, Integer, String, BIGINT
)

from .injectors import DSN

from aiopg.sa import create_engine
import sqlalchemy as sa


meta = MetaData()

user = Table(
    'user', meta,
    Column('id', Integer, primary_key=True),
    Column('user_id', BIGINT, unique=True, nullable=False)
)

job = Table(
    'job', meta,
    Column('id', Integer, primary_key=True),
    Column('link', String, unique=True)
)


def create_tables():
    engine = sa.create_engine(DSN.get())
    meta.drop_all(bind=engine, tables=[job, user], checkfirst=True)
    meta.create_all(bind=engine, tables=[job, user], checkfirst=True)
    return engine


async def get_all_user_ids():
    async with create_engine(DSN.get()) as engine:
        async with engine.acquire() as conn:
            users_proxy = await conn.execute(user.select())
            users = await users_proxy.fetchall()
            if len(users) > 0:
                return list(map(lambda x: x.user_id, users))
            else:
                return []


async def is_new_user(user_id: int) -> bool:
    async with create_engine(DSN.get()) as engine:
        async with engine.acquire() as conn:
            user_instance = await conn.execute(user.select().where(user.c.user_id == user_id))
            if user_instance.rowcount == 1:
                return False
            else:
                await conn.execute(sa.insert(user).values(user_id=user_id))
                return True


async def is_new_job(job_link: str) -> bool:
    async with create_engine(DSN.get()) as engine:
        async with engine.acquire() as conn:
            job_instance = await conn.execute(job.select().where(job.c.link == job_link))
            if job_instance.rowcount == 1:
                return False
            else:
                await conn.execute(sa.insert(job).values(link=job_link))
                return True
