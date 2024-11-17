# Класс, который будет дополнять класс родителя
class Koshka:
    def __init__(self, name, color, age):
        self.name = name
        self.age = age
        self.color = color

    def make_sound(self):
        return print("meow")

class LysayaKoshka(Koshka):
    def __init__(self, name, color, age, fur: bool):
        super().__init__(name, color, age) # Тоже самое, что:
        # .name = name
        # self.age = age
        # self.color = color
        self.fur = fur

    def make_sound(self):
        start = super().make_sound() # почему у меня не работает
        return print(f'{start} + "r-r-r-r-r"')

cat = Koshka("Vasya", "black", 3)
lscat = LysayaKoshka("Sphinx", "pink", 2, False)
lscat.make_sound()
lscat.make_sound()
# lscat.name

# Создайте классы для представления структуры магазина техники.

# Требования:

# Базовый класс Device, который будет представлять общие атрибуты
# для любой техники:

# атрибуты: brand, model, price.
# метод get_info(), который возвращает строку с кратким описанием устройства.
# Дочерние классы:

# Laptop с дополнительными атрибутами ram и storage.
# Smartphone с атрибутами camera_megapixels и battery_capacity.

# Каждый из классов должен переопределить метод get_info()
# для включения специфичной информации.
# Создайте класс Store, содержащий список устройств:

# Метод add_device(device), который добавляет устройство в магазин.
# Метод list_devices(), который выводит информацию обо всех устройствах.