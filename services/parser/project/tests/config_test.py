from ..config import Config


def test_config_works():
    params = {"dsn": "postgresql://lorem:lorem@db:5432/lorem",
              "admin_id": 123,
              "bot_token": "lorem"}
    assert Config(**params)


def config_exception_handler(params: dict):
    try:
        _ = Config(**params)
        return False
    except ValueError as e:
        return True


def test_config_fails():

    params1 = {"dsn": "postgresql://:lorem@db:5432/lorem",
               "admin_id": 123,
               "bot_token": "lorem"}
    assert config_exception_handler(params1)
    params2 = {"dsn": "postgresql://lorem:lorem@db:5432/lorem",
               "admin_id": "123",
               "bot_token": "lorem"}
    assert config_exception_handler(params2)
