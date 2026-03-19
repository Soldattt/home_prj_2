import pytest

from src.products import Category, Product


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
