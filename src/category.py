from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    category_count = 0
    product_count = 0
    _all_products = set()

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        # Обновляем счетчики
        Category.category_count += 1
        unique_products = {p.name for p in self.__products}
        Category._all_products.update(unique_products)
        Category.product_count = len(Category._all_products)

    def add_product(self, product):
        """Добавляет продукт в категорию."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category._all_products.add(product.name)
            Category.product_count = len(Category._all_products)
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    @property
    def products(self):
        """Возвращает строковое представление списка продуктов."""
        products_str = []
        for product in self.__products:
            products_str.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            )
        return "\n".join(products_str)
