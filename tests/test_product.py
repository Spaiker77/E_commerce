import pytest
from src.product import Product
from src.exceptions import ZeroQuantityError


def test_product_creation():
    p = Product("Test", "Desc", 100.0, 1)
    assert p.quantity == 1


def test_zero_quantity():
    with pytest.raises(ZeroQuantityError):
        Product("Test", "Desc", 100.0, 0)
