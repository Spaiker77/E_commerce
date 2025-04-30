from src.smartphone import Smartphone
from src.product import Product


def test_smartphone_initialization():
    s = Smartphone("S23", "Desc", 100000, 5, 95.0, "Ultra", 256, "Black")
    assert s.memory == 256
    assert s.color == "Black"


def test_smartphone_inheritance():
    s = Smartphone("X", "", 50000, 2, 90.0, "Basic", 128, "White")
    assert isinstance(s, Smartphone)
    assert isinstance(s, Product)
