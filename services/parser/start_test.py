from config import Config # noqa


def test_dsn():
    from start import DSN # noqa
    assert DSN.get()
