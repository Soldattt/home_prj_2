import pytest

from src.lawngrass import LawnGrass
from src.products import Category, Iterator, Product
from src.smartphone import Smartphone


@pytest.fixture
def product():
    return Product(name="Lenovo Legion 5", description="Ryzen 7, Черный цвет, 1 Tb", price=140000.0, quantity=3)


@pytest.fixture
def category():
    return Category(
        name="Ноутбуки",
        description="Ноутбуки отлично подходят для работы и досуга и их всегда можно взять с собой",
        products=[
            Product(name="Lenovo Legion 5", description="Ryzen 7, Черный цвет, 1 Tb", price=140000.0, quantity=3)
        ],
    )


@pytest.fixture
def category_1():
    return Category(
        name="Ноутбуки",
        description="Ноутбуки отлично подходят для работы и досуга и их всегда можно взять с собой",
        products=[],
    )


@pytest.fixture
def product_1():
    return Product(name="Lenovo Legion 5", description="Ryzen 7, Черный цвет, 1 Tb", price=140000.0, quantity=5)


@pytest.fixture
def product_2():
    return Product(name="Lenovo Legion 7", description="Ryzen 7, Черный цвет, 1 Tb", price=180000.0, quantity=3)


@pytest.fixture
def iterator(category):
    return Iterator(category)

@pytest.fixture
def lawn_grass_1():
    return LawnGrass(name="Трава_1", description="Не для курения", price=150.0, quantity=2, country="Россия", germination_period="7 дней", color="Зеленая")

@pytest.fixture
def lawn_grass_2():
    return LawnGrass(name="Трава_2", description="для курения", price=15000.0, quantity=5, country="Афганистан", germination_period="3 дня", color="Зеленая")

@pytest.fixture
def smartphone_1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 1, 95.5,
                         "S23 Ultra", 256, "Серый")

@pytest.fixture
def smartphone_2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 1, 98.2, "15", 512, "Gray space")

@pytest.fixture
def incorrect_product():
    return TypeError