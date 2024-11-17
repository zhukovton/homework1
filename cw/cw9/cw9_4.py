# класс Circle, есть радиус, методы сравнения и сложения


class Circle:
    def __init__(self, radius):
        self.radius = radius

    # проверка равенства
    def __eq__(self, other: "Circle"):
        return self.radius == other.radius

    # проверка на меньше
    def __lt__(self, other: "Circle"):
        return self.radius < other.radius

    # # проверка на больше (не обязательно)
    # def __gt__(self, other: "Circle"):
    #     return self.radius > other.radius

    # Сложение
    def __add__(self, other: "Circle"):
        return Circle(self.radius + other.radius)

    def __sub__(self, other: "Circle"):
        return Circle(self.radius - other.radius)

    def __repr__(self):
        return f"Circle({self.radius})"

    # С помощью этих методов можно контролировать присваивание и получение атрибутов
    def __getattribute__(self, name):
        if name == "length":
            return "Нет длины"
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if name == "radius" and not isinstance(value, int):  # isinstance - соответсвтвие типа
            raise TypeError  # Принудительный вызов ошибки
        return super().__setattr__(name, value)


circle = Circle(7)
circle1 = Circle(15)
# print(circle.length)
# print(circle + circle1)
print(circle.radius)
