import pytest
from src.product import Product


@pytest.fixture
def sample_product():
    return Product("Test", "Desc", 100.0, 5)


def test_product_str(sample_product):
    assert str(sample_product) == "Test, 100.0 руб. Остаток: 5 шт."


def test_product_add():
    p1 = Product("A", "", 100, 2)
    p2 = Product("B", "", 200, 3)
    assert p1 + p2 == 100 * 2 + 200 * 3
