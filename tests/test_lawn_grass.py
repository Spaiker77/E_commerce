from src.lawn_grass import LawnGrass
from src.product import Product


def test_lawn_grass_initialization():
    g = LawnGrass("Grass", "Desc", 500, 10, "RU", "7d", "Green")
    assert g.country == "RU"
    assert g.germination_period == "7d"


def test_lawn_grass_inheritance():
    g = LawnGrass("G", "", 300, 5, "US", "5d", "Blue")
    assert isinstance(g, LawnGrass)
    assert isinstance(g, Product)
