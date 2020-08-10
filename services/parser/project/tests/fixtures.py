from pytest import fixture
from .. import DB


@fixture
def db():
    DB.instance().init_db()
    return DB.instance()
