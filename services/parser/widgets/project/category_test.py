import asyncio

from .category import Category
from .db import create_tables


def test_create_right():
    assert Category("https://jobs.dou.ua/vacancies/feeds/?exp=0-1&category=Front%20End1", "sample_name_tag")


def test_create_wrong():
    try:
        Category("https://jobs.dou.ua/vacancies^^%&B/feeds/?exp=0-1&category=Front%20", "sample_name_&*&")
    except NameError as ne:
        assert str(ne)


def test_attributes():
    category = Category("https://jobs.dou.ua/vacancies/feeds/?exp=0-1&category=Front%20End1", "lorem_ipsum")
    assert category.attributes["link"] == "https://jobs.dou.ua/vacancies/feeds/?exp=0-1&category=Front%20End1"
    assert category.attributes["tag"] == "lorem_ipsum"


def test_create():
    create_tables(drop_all=True)
    category = Category("https://jobs.dou.ua/vacancies/feeds/?exp=0-1&category=Front%20End1", "lorem_ipsum")

    async def wrapper():
        assert (await category.create()) == "OK"

    asyncio.get_event_loop().run_until_complete(wrapper())


def test_get_all():
    create_tables(drop_all=True)
    category_1 = Category("https://jobs.dou.ua/vacancies/feeds/?exp=0-1&category=Front%20End1", "lorem_ipsum")
    category_2 = Category("https://jobs.dou.ua/vacancies/feeds/?exp=0-1&category=Front%20End2", "lorem_ipsum2")

    async def wrapper():
        assert (await category_1.create()) == "OK"
        assert (await category_2.create()) == "OK"
        categories = await Category.get_all()
        assert len(categories) == 2

    asyncio.get_event_loop().run_until_complete(wrapper())


def test_delete():
    create_tables(drop_all=True)
    category_1 = Category("https://jobs.dou.ua/vacancies/feeds/?exp=0-1&category=Front%20End1", "lorem_ipsum")
    category_2 = Category("https://jobs.dou.ua/vacancies/feeds/?exp=0-1&category=Front%20End2", "lorem_ipsum2")

    async def wrapper():
        assert (await category_1.create()) == "OK"
        assert (await category_2.create()) == "OK"
        categories = await Category.get_all()
        assert len(categories) == 2

        assert (await category_1.delete()) == "OK"
        assert (await Category.get_all())[0].tag == category_2.tag

    asyncio.get_event_loop().run_until_complete(wrapper())
