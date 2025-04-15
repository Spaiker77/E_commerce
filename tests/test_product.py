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