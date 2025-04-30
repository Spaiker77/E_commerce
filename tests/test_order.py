import pytest
from src.order import Order
from src.product import Product


def test_order_creation():
    p = Product("Test", "", 100, 10)
    o = Order(p, 3)
    assert o.total_price == 300
    assert p.quantity == 7  # Проверка уменьшения остатка


def test_order_insufficient_stock():
    p = Product("Test", "", 100, 2)
    with pytest.raises(ValueError):
        Order(p, 3)
