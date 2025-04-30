from src.base_product import BaseProduct
from src.logging_mixin import LoggingMixin


class Product(LoggingMixin, BaseProduct):
    """Класс продукта с миксином"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        # Правильный порядок вызова super()
        super().__init__(
            name=name, description=description, price=price, quantity=quantity
        )

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        if type(self) != type(other):
            raise TypeError("Нельзя складывать разные типы товаров")
        return (self.price * self.quantity) + (other.price * other.quantity)
