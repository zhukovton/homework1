# прямоугольник
class Rectangle:
    def __init__(self, length, wide=None):
        self.length = length
        self.wide = wide
        if wide is None:
            self.wide = length
        else:
            self.wide = wide

    def area(self):
        area_rectangle = self.length * self.wide
        return area_rectangle

    def perimetr(self):
        perimetr_rectangle = 2 * (self.length + self.wide)
        return perimetr_rectangle


rec = Rectangle(3, 7)

print(rec.area())
print(rec.perimetr())
