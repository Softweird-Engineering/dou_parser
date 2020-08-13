from pytest import fixture
from ..project.injectors import DB


@fixture
def db():
    return DB.instance()
