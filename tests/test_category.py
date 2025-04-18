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
        Product("Product 2", "Desc 2", 200.0, 3),
    ]


@pytest.fixture
def sample_category(sample_products):
    return Category("Test Category", "Test Description", sample_products)


def test_category_initialization(sample_category):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Description"
    assert len(sample_category.products.split("\n")) == 2


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


def test_private_products_attribute(sample_category):
    """Проверяем, что products стал приватным"""
    with pytest.raises(AttributeError):
        sample_category.__products


def test_add_product_method(sample_category):
    """Тестируем метод add_product"""
    new_product = Product("New Product", "Desc", 300.0, 2)
    initial_count = len(sample_category.products.split("\n"))

    sample_category.add_product(new_product)
    assert len(sample_category.products.split("\n")) == initial_count + 1
    assert "New Product, 300.0 руб. Остаток: 2 шт." in sample_category.products


def test_add_product_invalid_type(sample_category):
    """Проверяем обработку неверного типа в add_product"""
    with pytest.raises(
        TypeError, match="Можно добавлять только объекты класса Product"
    ):
        sample_category.add_product("not a product")


def test_products_property_format(sample_category):
    """Проверяем формат вывода products property"""
    output = sample_category.products
    assert "Product 1, 100.0 руб. Остаток: 5 шт." in output
    assert "Product 2, 200.0 руб. Остаток: 3 шт." in output
    assert output.count("\n") == 1  # Проверяем количество переносов строк
