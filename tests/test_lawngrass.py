import pytest


def test_init_lawn_grass(lawn_grass_1):
    assert lawn_grass_1.name == "Трава_1"


def test_add_lawn_grass(lawn_grass_1, lawn_grass_2):
    assert lawn_grass_1 + lawn_grass_2 == 75300.0


def test_incorrect_add_1(lawn_grass_1):
    with pytest.raises(TypeError):
        res = lawn_grass_1 + "Не смартфон"


def test_incorrect_add_2(lawn_grass_1, smartphone_1):
    with pytest.raises(TypeError):
        res = lawn_grass_1 + smartphone_1
