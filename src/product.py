class Product:
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data, products=None):
        """Создает новый продукт, проверяя на дубликаты."""
        if products is None:
            return cls(**product_data)

        # Поиск дубликатов
        for existing_product in products:
            if existing_product.name.lower() == product_data["name"].lower():
                # Объединяем количество
                existing_product.quantity += product_data["quantity"]
                # Выбираем максимальную цену
                if product_data["price"] > existing_product.price:
                    existing_product.price = product_data["price"]
                return existing_product

        return cls(**product_data)

    @property
    def price(self):
        """Возвращает цену продукта."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Устанавливает новую цену с проверкой."""
        if new_price > 0:
            if hasattr(self, "_Product__price") and new_price < self.__price:
                confirmation = input("Вы уверены, что хотите понизить цену? (y/n): ")
                if confirmation.lower() != "y":
                    print("Изменение цены отменено")
                    return
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")
