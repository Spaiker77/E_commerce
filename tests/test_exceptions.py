import pytest
from src.category import Category
from src.product import Product


def test_add_zero_quantity_product():
    p = Product("Test", "Desc", 100, 1)
    p.quantity = 0  # Изменяем количество после создания
    cat = Category("Test", "Desc", [])
    cat.add_product(p)
    assert len(cat.products) == 0
