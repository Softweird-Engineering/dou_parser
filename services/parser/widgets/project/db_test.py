from .db import *

from pytest import fixture
import asyncio


@fixture
def user_id():
    return 1231231231231


@fixture
def job_link():
    return 1231231231231


def test_table_create():
    assert create_tables()


def test_is_new_user(user_id):
    assert create_tables()

    async def assert_is_new_user(uid):
        assert await is_new_user(uid)
        assert not await is_new_user(uid)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(assert_is_new_user(user_id))


def test_is_new_job(job_link):
    # assert create_tables()

    async def assert_is_new_user(link):
        assert await is_new_user(link)
        assert not await is_new_user(link)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(assert_is_new_user(job_link))


def test_get_all(user_id):
    async def assert_get_all():
        assert (await get_all_user_ids()) == [user_id]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(assert_get_all())
