class PrintMixin:
    """Класс для описания продуктов"""
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        """Метод для описания продукта строкой с указанием класса"""
        return f"{self.__class__.__name__}, {self.name}, {self.description}, {self.price}, {self.quantity}"