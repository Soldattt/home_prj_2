from src.products import Product


class LawnGrass(Product):
    """Дочерний класс от Products, описывающий смартфоны"""
    country = str
    germination_period = str
    color = str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


    def __add__(self, other):
        """Метод выводит сумму цен на продукты, если они являются классом LawnGrass"""
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError