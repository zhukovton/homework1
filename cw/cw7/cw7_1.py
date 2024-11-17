# информация о хранении о человеке.
# birthday - увеличивает возраст на год
# fullname - возвращает полное ФИО

class User:
    def __init__(self, age, name, sirname, patronymic):
        self.name = name
        self.sirname = sirname
        self.patronymic = patronymic
        self.age = age

    def birthday(self):
        self.age += 1

    def fullname(self):
        return f"{self.name} {self.sirname} {self.patronymic}"

user = User(35, "Ivan", "Frolov", "Vasilievich")
# print(user)

print(user.fullname())
user.birthday() # вызов без return
print(user.age)
