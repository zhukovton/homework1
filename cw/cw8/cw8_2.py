# Класс книга. Класс библиотека
# в книге содержится id, название, автор
# в библиотеке хранятся книги
import random


class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        self.__id = random.randint(100_000, 999_999)

    def __repr__(self):
        return f"{self.name} {self.author}"


class Magazine(Book):
    def __init__(self, name, author, year):
        super().__init__(name, author, year)
        self.expire = 30


class Nowel(Book):
    def __init__(self, name, author, year):
        super().__init__(name, author, year)
        self.expire = 60


class Library:
    def __init__(self, books: list):
        self.books = books
        self.time = 0

    def add_book(self, book: Book):
        self.books.append(book)

    def new_day(self):
        self.time += 1

    def check_expired_books(self):
        exp_lst = []
        for i in self.books:
            if i.expire <= self.time:
                exp_lst.append(i)
        return exp_lst

    def show_books(self):
        book_names = []
        for i in self.books:
            book_names.append(i.name)

        return book_names


# print(library.show_books())
mag = Magazine("Букварь", "Афанасий", 2000)
now = Nowel("Букварь", "Афанасий", 2000)
library = Library([now, mag])

for i in range(61):
    library.new_day()

print(library.check_expired_books())
