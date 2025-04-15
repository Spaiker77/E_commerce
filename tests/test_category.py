import pytest
from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_counters():
    """Сбрасываем счетчики перед каждым тестом"""
    Category.category_count = 0
    Category._all_products = set()
    Category.product_count = 0


@pytest.fixture
def sample_products():
    return [
        Product("Product 1", "Desc 1", 100.0, 5),
        Product("Product 2", "Desc 2", 200.0, 3)
    ]


@pytest.fixture
def sample_category(sample_products):
    return Category("Test Category", "Test Description", sample_products)


def test_category_initialization(sample_category):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Description"
    assert len(sample_category.products) == 2


def test_category_counters(sample_products):
    # Первая категория
    Category("Cat1", "Desc", sample_products)
    assert Category.category_count == 1
    assert Category.product_count == 2  # 2 уникальных продукта

    # Вторая категория с новым продуктом
    Category("Cat2", "Desc", [Product("New", "Desc", 300.0, 1)])
    assert Category.category_count == 2
    assert Category.product_count == 3  # 2 старых + 1 новый


def test_unique_products_counter():
    p1 = Product("Unique", "Desc", 100.0, 1)
    p2 = Product("Unique", "Desc", 200.0, 2)  # Дубликат по имени

    Category("Cat1", "Desc", [p1])
    assert Category.product_count == 1

    Category("Cat2", "Desc", [p2])
    assert Category.product_count == 1  # Имя не уникальное