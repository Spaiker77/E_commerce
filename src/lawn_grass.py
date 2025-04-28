from src.product import Product


class LawnGrass(Product):
    """Класс для газонной травы"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self):
        return (
            f"LawnGrass({self.name}, {self.price}, {self.quantity}, "
            f"{self.country}, {self.germination_period}, {self.color})"
        )
