from src.exceptions import ZeroQuantityError


class Product:
    """Класс товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity <= 0:
            raise ZeroQuantityError()
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product({self.name}, {self.price}, {self.quantity})"
