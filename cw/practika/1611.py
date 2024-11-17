# Создайте класс Employee (сотрудник), который имеет:
# name – имя сотрудника;
# age – возраст;
# salary – оклад;
# bonus – премия.
# Класс Employee должен иметь следующие методы:
# get_name()– возвращает имя сотрудника;
# get_age()– возвращает возраст;
# get_salary() – возвращает зарплату сотрудника;
# set_bonus(bonus) – устанавливает свойство bonus;
# get_bonus() – возвращает бонус для сотрудника;
# get_total_salary() – возвращает общую зарплату сотрудника (оклад + бонус).


class Employee:
    __slots__ = ('__name', '__age', '__salary', '__bonus')

    def __init__(self, name, age, salary, bonus):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = bonus

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @property
    def age(self):
        return self.__age

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, bonus):
        if bonus <= 0 or not isinstance(bonus, int):
            raise ValueError
        self.__bonus = bonus

    @property
    def total_salary(self):
        return self.__salary + self.__bonus


eml = Employee("Vlad", 22, 11222, 110)
print(eml.name)
print(eml.total_salary)
