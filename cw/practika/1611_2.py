from dataclasses import dataclass
# декоратор автоматом навешивает init, , repr
# from datetime import timedelta
import json


# в скобках можно добавить параметр
@dataclass(eq=False)
class Book:
    __slots__ = ("title", "author", "rent_days")
    title: str
    author: str
    rent_days: int

    def __eq__(self, other: "Book"):
        return self.author == other.author and self.title == other.title

    def __repr__(self):
        return f"title: {self.title}, author: {self.author}, rent_days: {self.rent_days}"


class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.__books = books

    def add_book(self, book: "Book"):
        if not isinstance(book, Book):
            raise ValueError
        self.__books.append(book)

    def show_books(self):
        return self.__books

    def load_from_json(self, filename):
        self.__books = []
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        for book_d in data:
            book = Book(**book_d)
            self.__books.append(book)

    # @classmethod
    # def load_from_json(cls, filename):
    #     books = []
    #     with open(filename, "r", encoding="utf-8") as file:
    #         data = json.load(file)
    #     for book_d in data:
    #         book = Book(**book_d)
    #         books.append(book)
    #     return cls(books)


# book = Book("Алиса в стране чудес", "Кэрол", timedelta(days=30))
# book1 = Book("Властелин Колец", "Толкиен", timedelta(days=30))
# book2 = Book("Песнь льда и пламени", "Мартин", timedelta(days=45))
# print(book1 in [book1, book2])
lib = Library()
# lib.add_book(book2)
# print(lib.show_books())

lib.load_from_json("1.json")
print(lib.show_books())
