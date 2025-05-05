from src.category import Category
from src.product import Product


def test_middle_price():
    p1 = Product("A", "", 100, 1)
    p2 = Product("B", "", 200, 1)
    cat = Category("Test", "Desc", [p1, p2])
    assert cat.middle_price() == 150


def test_empty_category():
    cat = Category("Test", "Desc", [])
    assert cat.middle_price() == 0
