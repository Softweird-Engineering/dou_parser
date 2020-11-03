from config import DATABASE_URL # noqa
#
# DB.instance(DATABASE_URL).init_db()
#
#
# def test_db():
#     assert DB.instance()


def test_dsn():
    from start import DSN # noqa
    assert DSN.get()
