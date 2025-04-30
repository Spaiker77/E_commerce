class LoggingMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs):
        # инициализируем родительские классы
        super().__init__(*args, **kwargs)
        # логируем параметры
        params = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        print(f"Создан {self.__class__.__name__}({params})")
