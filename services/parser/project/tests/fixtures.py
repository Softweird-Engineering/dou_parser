from pytest import fixture
from .. import DB


@fixture
def db():
    return DB.instance()
