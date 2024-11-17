# класс круг. метод вычисления площади и длины. Атрибут - радиус
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area_circle = 3.14 * self.radius ** 2
        return area_circle

    def length(self):
        length_circle = 2 * 3.14 * self.radius
        return length_circle


circle = Circle(15)
print(circle.area())
print(circle.length())
