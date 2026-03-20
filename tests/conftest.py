import pytest

from src.products import Category, Iterator, Product


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
