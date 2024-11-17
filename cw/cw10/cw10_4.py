# если запихнуть некорректную длину выкидывать ошибку
class NegativeValueError(Exception):
    def __str__(self):
        return f"уходите. Значение отрицательное"


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __setattr__(self, key, value):
        if key == "radius":
            if not isinstance(value, int):
                raise TypeError
            elif value <= 0:
                raise NegativeValueError
        super().__setattr__(key, value)


if __name__ == "__main__":
    cir = Circle(-1)
    print(cir)
