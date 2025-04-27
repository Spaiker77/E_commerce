class Product:
    """Базовый класс товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных типов")
        return (self.price * self.quantity) + (other.price * other.quantity)
