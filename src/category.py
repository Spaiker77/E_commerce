from src.exceptions import ZeroQuantityError


class Category:
    """Класс категории товаров"""

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

    def middle_price(self) -> float:
        """Средняя цена товаров в категории"""
        try:
            total = sum(product.price for product in self.products)
            return total / len(self.products)
        except ZeroDivisionError:
            return 0

    def add_product(self, product):
        """Добавление товара с обработкой исключений"""
        try:
            if product.quantity <= 0:
                raise ZeroQuantityError()
            self.products.append(product)
            print(f"Товар {product.name} успешно добавлен")
        except ZeroQuantityError as e:
            print(f"Ошибка: {e}")
        finally:
            print("Обработка добавления товара завершена")
