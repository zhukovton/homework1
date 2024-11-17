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

class Employee(User):
    def __init__(self, age, name, sirname, patronymic, salary):
        super().__init__(age, name, sirname, patronymic)
        self.__salary = salary

    def salary_manage(self, percent):
        self.__salary *= percent

    def show_salary(self):
        return f"{self.name} {self.sirname} {self.__salary}"






user = User(35, "Ivan", "Frolov", "Vasilievich")
# print(user)

# print(user.fullname())
# user.birthday() # вызов без return
# print(user.age)
worker = Employee(35, "Ivan", "Frolov", "Vasilievich", 10_000)

worker.salary_manage(1.5)
print(worker.show_salary())
