from src.product import Product


class Category:
    """Класс категории с итерацией"""

    category_count = 0
    product_count = 0
    _all_products = set()

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category._all_products.update({(p.name, p.price) for p in self.__products})
        Category.product_count = len(Category._all_products)

    @property
    def products(self):
        return [str(product) for product in self.__products]

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self):
        return CategoryIterator(self.__products)


class CategoryIterator:
    """Итератор для категории"""

    def __init__(self, products: list):
        self.products = products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            result = self.products[self.index]
            self.index += 1
            return result
        raise StopIteration
