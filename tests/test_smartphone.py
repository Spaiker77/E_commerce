import pytest
from src.smartphone import Smartphone


@pytest.fixture
def sample_smartphone():
    return Smartphone(
        "Samsung S23", "Flagship smartphone", 180000.0, 5, 95.5, "S23", 256, "Black"
    )


def test_smartphone_initialization(sample_smartphone):
    """Проверка инициализации смартфона"""
    assert sample_smartphone.name == "Samsung S23"
    assert sample_smartphone.price == 180000.0
    assert sample_smartphone.efficiency == 95.5
    assert sample_smartphone.memory == 256


def test_smartphone_add(sample_smartphone):
    """Проверка сложения смартфонов"""
    s2 = Smartphone("iPhone 15", "", 200000.0, 3, 98.0, "15", 512, "White")
    total = sample_smartphone + s2
    assert total == (180000.0 * 5) + (200000.0 * 3)


def test_smartphone_invalid_add(sample_smartphone):
    """Проверка ошибки при сложении с неподходящим типом"""
    from src.lawn_grass import LawnGrass

    grass = LawnGrass("Grass", "", 500.0, 10, "RU", "7d", "Green")
    with pytest.raises(TypeError):
        sample_smartphone + grass
