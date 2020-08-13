from widgets.project.injectors import DB # noqa
from config import DATABASE_URL # noqa

DB.instance(DATABASE_URL).init_db()


def test_db():
    assert DB.instance()
