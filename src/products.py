


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
    def new_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @pr




class Category:
    """Класс для описания категории списка продуктов"""

    name = str
    description = str
    products = list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1

    @property
    def products(self):
        product_str = ""
        for x in self.__products:
            product_str += f"{x.name}, {x.price} руб. Остаток: {x.quantity} шт.\n"
        return product_str


    def add_product(self, x: Product):
        self.__products.append(x)
        Category.product_count += 1








