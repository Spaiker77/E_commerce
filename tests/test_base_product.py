import pytest
from src.base_product import BaseProduct
from src.product import Product


def test_base_product_is_abstract():
    """Проверка, что BaseProduct нельзя инстанцировать"""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Desc", 100, 5)


def test_product_implements_abstract_methods():
    """Проверка реализации абстрактных методов в Product"""
    p = Product("Test", "Desc", 100, 5)

    # Проверка обязательных методов
    assert hasattr(p, "__str__")
    assert hasattr(p, "__add__")

    # Проверка корректности реализации
    assert str(p) == "Test, 100 руб. Остаток: 5 шт."
    p2 = Product("Test2", "", 200, 2)
    assert p + p2 == 100 * 5 + 200 * 2
