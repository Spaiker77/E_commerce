import pytest
from src.product import Product


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 100.0, 5)


def test_product_initialization(sample_product):
    # Проверка корректности инициализации
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 5


def test_product_attributes_types(sample_product):
    # Проверка типов данных
    assert isinstance(sample_product.name, str)
    assert isinstance(sample_product.description, str)
    assert isinstance(sample_product.price, float)
    assert isinstance(sample_product.quantity, int)


def test_private_price_attribute(sample_product):
    """Проверяем, что price стал приватным"""
    with pytest.raises(AttributeError):
        sample_product.__price


def test_price_property(sample_product):
    """Тестируем property price"""
    assert sample_product.price == 100.0


def test_price_setter_positive(sample_product, monkeypatch):
    """Тестируем сеттер price с положительным значением"""
    sample_product.price = 150.0
    assert sample_product.price == 150.0


def test_price_setter_negative(sample_product, capsys):
    """Тестируем сеттер price с отрицательным значением"""
    sample_product.price = -50.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 100.0  # Цена не изменилась


def test_price_setter_zero(sample_product, capsys):
    """Тестируем сеттер price с нулевым значением"""
    sample_product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 100.0  # Цена не изменилась


def test_price_decrease_confirmation(sample_product, monkeypatch, capsys):
    """Тестируем подтверждение понижения цены"""
    # Эмулируем ввод 'y' (согласие)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    sample_product.price = 50.0
    assert sample_product.price == 50.0

    # Эмулируем ввод 'n' (отказ)
    monkeypatch.setattr("builtins.input", lambda _: "n")
    sample_product.price = 30.0
    captured = capsys.readouterr()
    assert "Изменение цены отменено" in captured.out
    assert sample_product.price == 50.0  # Цена не изменилась


def test_new_product_classmethod():
    """Тестируем класс-метод new_product"""
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 100.0,
        "quantity": 5,
    }
    product = Product.new_product(product_data)
    assert isinstance(product, Product)
    assert product.name == "Test Product"
    assert product.price == 100.0


def test_new_product_with_duplicates():
    """Тестируем обработку дубликатов в new_product"""
    existing_products = [Product("Existing Product", "Desc", 100.0, 5)]

    # Дубликат по имени
    product_data = {
        "name": "Existing Product",
        "description": "New Desc",
        "price": 150.0,
        "quantity": 3,
    }

    product = Product.new_product(product_data, existing_products)
    assert product.quantity == 8  # Количества сложились
    assert product.price == 150.0  # Выбрана более высокая цена
    assert len(existing_products) == 1  # Новый продукт не добавлен
