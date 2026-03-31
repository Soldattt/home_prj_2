from abc import ABC, abstractmethod

from src.print_mixin import PrintMixin


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass

    @abstractmethod
    def __add__(self, *args, **kwargs):
        pass


class Product(BaseProduct, PrintMixin):
    """Класс для описания продукта"""

    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity != 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен.")
        super().__init__()

    def __str__(self):
        """Метод выводит описание товара в виде строки"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод выводит сумму цен на продукты"""
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, new_product: dict):
        """Метод принимает на вход параметры товара в словаре и возвращает созданный объект класса"""
        name, description, price, quantity = new_product.values()
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер возвращает значение приватного атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Сеттер принимает новую цену продукта, только, если значение новой цены больше нуля
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


class Category:
    """Класс для описания категории списка продуктов"""

    name = str
    description = str
    products = list[Product]
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.product_count += len(products)
        Category.category_count += 1

    def __str__(self):
        """Метод выводит описание категории в виде строки с количеством товаров в категории"""
        product_quantity_count = 0
        for i in self.__products:
            product_quantity_count += i.quantity
        return f"{self.name}, количество продуктов: {product_quantity_count} шт."

    def add_product(self, new_product: Product):
        """Метод добавляет новый товар в категорию"""
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError

    def middle_price(self):
        try:
            return sum([product.price for product in self.__products]) / Category.product_count
        except ZeroDivisionError:
            return 0

    @property
    def products(self):
        """Геттер выводит список товаров в виде строк"""
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def products_list(self):
        return self.__products


class Iterator:
    """Класс для перебора продуктов"""

    def __init__(self, category_obj):
        self.category = category_obj
        self.point = 0

    def __iter__(self):
        self.point = 0
        return self

    def __next__(self):
        if self.point < len(self.category.products_list):
            i = self.category.products_list[self.point]
            self.point += 1
            return i
        else:
            raise StopIteration
