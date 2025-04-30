from src.product import Product


class Category:
    """Класс категории товаров"""

    category_count = 0
    product_count = 0
    _all_products = set()

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = []

        Category.category_count += 1
        if products:
            for product in products:
                self.add_product(product)

    @property
    def products(self):
        return [str(p) for p in self.__products]

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только продукты")
        self.__products.append(product)
        Category._all_products.add((product.name, product.price))
        Category.product_count = len(Category._all_products)

    def __str__(self) -> str:
        total = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total} шт."
