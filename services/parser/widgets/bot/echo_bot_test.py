import pytest # noqa


def test_check_health():
    from .echo_bot import bot
    assert bot
