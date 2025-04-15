class Category:
    """Класс для представления категории товаров."""
    category_count = 0
    product_count = 0
    _all_products = set()

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        # Обновляем счетчики
        Category.category_count += 1
        unique_products = {p.name for p in self.products}
        Category._all_products.update(unique_products)
        Category.product_count = len(Category._all_products)