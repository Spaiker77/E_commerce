from abc import ABC, abstractmethod
from src.product import Product


class BaseOrder(ABC):
    """Абстрактный класс заказа"""

    @abstractmethod
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    @property
    @abstractmethod
    def total_price(self) -> float:
        pass


class Order(BaseOrder):
    """Класс заказа"""

    def __init__(self, product: Product, quantity: int):
        if quantity > product.quantity:
            raise ValueError("Недостаточно товара на складе")
        super().__init__(product, quantity)
        product.quantity -= quantity  # Уменьшаем остаток

    @property
    def total_price(self) -> float:
        return self.product.price * self.quantity

    def __repr__(self):
        return f"Order({self.product.name}, {self.quantity}, total={self.total_price})"
