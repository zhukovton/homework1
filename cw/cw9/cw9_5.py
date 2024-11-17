# класс прямоугольник, метод определения площади, метод сравнения и сложения и вычитания
from cw.cw10.cw10_4 import NegativeValueError


class IncorrectRectangleException(Exception):
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2

    def __str__(self):
        return f"Нельзя сложить {self.r1} и {self.r2}"


class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        if width is None:
            self.width = length
        else:
            self.width = width

    def __setattr__(self, key, value):
        self.__validate_atr(key, value)
        super().__setattr__(key, value)

    def __validate_atr(self, key, value):
        if key in ("length", "width"):
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError
            elif value <= 0:
                raise NegativeValueError

    def area(self):
        area = self.length * self.width
        return area

    # метод сравнения
    def __eq__(self, other: "Rectangle"):
        return self.area() == other.area()

    # новая длина будет сумма двух передыдущих, а ширина сумма площадей поделенная на новую длину
    def __add__(self, other: "Rectangle"):
        conditions = [
            self.length == other.length,
            self.length == other.width,
            self.width == other.width,
            self.width == other.length
        ]

        if not any(conditions):  # any - между всеми объектами делает or
            raise IncorrectRectangleException(self, other)
        if self.length == other.length or self.length == other.width:
            new_length = self.length
            new_width = (self.area() + other.area()) / new_length
        else:
            new_width = self.width
            new_length = (self.area() + other.area()) / new_width
        return Rectangle(new_length, new_width)

    def __repr__(self):
        return f"Rectangle({self.length}, {self.width})"


rec = Rectangle(5, 2)
rec1 = Rectangle(3)
print(rec + rec1)
print(rec == rec1)
