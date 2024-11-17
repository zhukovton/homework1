# Дандр методы, либо магические методы (Их не нужно напрямую вызывать)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # метод представления пользователя
    def __str__(self):
        return f"{self.name}"

    # метод возвращает представления для програмиста
    def __repr__(self):
        return f"User('{self.name}', {self.age})"


user = User("vlad", 22)
user1 = User("Alex", 32)
print([user, user1])
print(f"{user1=}")
