import pytest
from src.product import Product


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 100.0, 5)


def test_product_initialization(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 5


def test_product_str(sample_product):
    assert str(sample_product) == "Test Product, 100.0 руб. Остаток: 5 шт."


def test_product_add():
    p1 = Product("A", "", 100, 2)
    p2 = Product("B", "", 200, 3)
    assert p1 + p2 == 100 * 2 + 200 * 3
