from src.product import Product


def test_logging_mixin(capsys):
    # Создаем продукт
    p = Product("Test", "Desc", 100, 5)

    # Перехватываем вывод
    captured = capsys.readouterr()

    # Проверяем вывод
    expected_output = (
        "Создан Product(name=Test, description=Desc, " "price=100, quantity=5)"
    )
    assert expected_output in captured.out
