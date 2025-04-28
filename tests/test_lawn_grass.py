import pytest
from src.lawn_grass import LawnGrass


@pytest.fixture
def sample_lawn_grass():
    return LawnGrass(
        "Premium Grass", "High quality lawn", 500.0, 20, "USA", "14 days", "Dark Green"
    )


def test_lawn_grass_initialization(sample_lawn_grass):
    """Проверка инициализации газонной травы"""
    assert sample_lawn_grass.name == "Premium Grass"
    assert sample_lawn_grass.price == 500.0
    assert sample_lawn_grass.country == "USA"
    assert sample_lawn_grass.germination_period == "14 days"


def test_lawn_grass_add(sample_lawn_grass):
    """Проверка сложения газонных трав"""
    g2 = LawnGrass("Standard Grass", "", 300.0, 15, "RU", "7d", "Green")
    total = sample_lawn_grass + g2
    assert total == (500.0 * 20) + (300.0 * 15)


def test_lawn_grass_invalid_add(sample_lawn_grass):
    """Проверка ошибки при сложении с неподходящим типом"""
    from src.smartphone import Smartphone

    phone = Smartphone("Phone", "", 100000.0, 2, 90.0, "X", 128, "Black")
    with pytest.raises(TypeError):
        sample_lawn_grass + phone
