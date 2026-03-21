from src.products import Product


class Smartphone(Product):
    """Дочерний класс от Products, описывающий смартфоны"""
    efficiency = float
    model = str
    memory = int
    color = str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color,):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Метод выводит сумму цен на продукты, если они являются классом Smartphone"""
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError