from .category import Category


def test_create_right():
    assert Category("sdfsdfsdfsdfs", "sdfsdf90909_000_BHDHSb")


def test_create_wrong():
    try:
        Category("sdfsdf", "skdfhsdfhsdf*()&*&^")
    except NameError as ne:
        assert str(ne)