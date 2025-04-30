from src.product import Product


def test_product_creation():
    p = Product("Test", "Desc", 100.0, 5)
    assert p.name == "Test"
    assert p.price == 100.0


def test_product_str():
    p = Product("Телефон", "Смартфон", 50000, 3)
    assert str(p) == "Телефон, 50000 руб. Остаток: 3 шт."


def test_product_add():
    p1 = Product("A", "", 100, 2)
    p2 = Product("B", "", 200, 3)
    assert p1 + p2 == 100 * 2 + 200 * 3
