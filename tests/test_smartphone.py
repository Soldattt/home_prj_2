import pytest


def test_init_smart(smartphone_1):
    assert smartphone_1.name == "Samsung Galaxy S23 Ultra"


def test_add_smart(smartphone_1, smartphone_2):
    assert smartphone_1 + smartphone_2 == 390000.0


def test_incorrect_add_1(smartphone_1):
    with pytest.raises(TypeError):
        res = smartphone_1 + "Не смартфон"


def test_incorrect_add_2(smartphone_1, lawn_grass_1):
    with pytest.raises(TypeError):
        res = smartphone_1 + lawn_grass_1
