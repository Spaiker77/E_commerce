import pytest
from src.product import Product
from src.category import Category


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category._all_products = set()
    Category.product_count = 0


@pytest.fixture
def sample_products():
    return [
        Product("Product 1", "Desc 1", 100.0, 5),
        Product("Product 2", "Desc 2", 200.0, 3),
    ]


def test_category_str(sample_products):
    cat = Category("Test", "Desc", sample_products)
    assert str(cat) == "Test, количество продуктов: 8 шт."


def test_category_iteration(sample_products):
    cat = Category("Test", "Desc", sample_products)
    assert [product.name for product in cat] == ["Product 1", "Product 2"]
