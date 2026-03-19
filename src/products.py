class Product:
    """Класс для описания продукта"""

    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
        Category.product_count = len(self.__products)
        Category.category_count += 1

    def add_product(self, new_product: Product):
        """Метод добавляет новый товар в категорию"""
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер выводит список товаров в виде строк"""
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

        return product_str
