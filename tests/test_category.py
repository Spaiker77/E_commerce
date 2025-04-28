import pytest
from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category._all_products = set()
    Category.product_count = 0


@pytest.fixture
def sample_product():
    return Product("Test", "Desc", 100.0, 5)


def test_category_initialization(sample_product):
    cat = Category("Test", "Desc", [sample_product])
    assert cat.name == "Test"
    assert len(cat.products) == 1


def test_category_counters(sample_product):
    initial_categories = Category.category_count
    Category("New", "Desc", [sample_product])
    assert Category.category_count == initial_categories + 1
