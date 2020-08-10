import pytest


def test_check_health():
    from .echo_bot import bot
    assert bot
