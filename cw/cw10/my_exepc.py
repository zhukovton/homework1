# Добавили свое исключение. Наследуемся от Exception
class MyException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyException вы криво накодили, уходите. Значение {self.value}"


# raise вызвать исключение
raise MyException(4)
