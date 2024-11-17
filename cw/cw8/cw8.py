import random

# public, protected, private
class User:
    def __init__(self, name, age, birthday):
        self.name = name
        self.age = age # public переменная
        self.__id = random.randint(100, 999) # __ - означает приватный атрибут.
        # Чтобы снаружи доступа для него не было, чтобы не ломал логику никто
        self._birthday = birthday  #protected (с одним подчеркиванием) можно достать снаружи

        # Методы тоже могут быть приватными
        # def _rename(self, name):
        #     self.name = name

user = User("Lon", 25, "10.10.2010")
print(user._User__id)   # user._User__id таким образом можно вывсети id
print(user._birthday)

