import pytest

from src.products import Category, Product


def test_product_init(product):
    assert product.name == "Lenovo Legion 5"
    assert product.description == "Ryzen 7, Черный цвет, 1 Tb"
    assert product.price == 140000.0
    assert product.quantity == 3


def test_category_init(category):
    assert category.name == "Ноутбуки"
    assert category.description == "Ноутбуки отлично подходят для работы и досуга и их всегда можно взять с собой"
    assert category.category_count == 1
    assert category.product_count == 1


def test_category_product_1(category_1):
    assert category_1.products == ""


def test_category_product_2(category_1):
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [],
    )
    product = Product("Xiaomi Redmi Note 11", "Фоновая подсветка", 123000.0, 7)
    category.add_product(product)
    assert category.products == "Xiaomi Redmi Note 11, 123000.0 руб. Остаток: 7 шт.\n"


def test_new_product():
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5

    new_product.price = 800.0
    assert new_product.price == 800.0

    new_product.price = -10
    assert new_product.price == 800.0

    new_product.price = 0.0
    assert new_product.price == 800.0


def test_str(product, category):
    assert str(product) == "Lenovo Legion 5, 140000.0 руб. Остаток: 3 шт."
    assert str(category) == "Ноутбуки, количество продуктов: 3 шт."


def test_add_product(product_1, product_2):
    assert product_1 + product_2 == 1240000.0


def test_iterator(iterator):
    assert iterator.point == 0
    assert next(iterator).name == "Lenovo Legion 5"
    with pytest.raises(StopIteration):
        next(iterator)


def test_incorrect_product(incorrect_product):
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [],
    )
    product = "Не продукт"
    with pytest.raises(TypeError):
        category.add_product(product)
