# Класс книга. Класс библиотека
# в книге содержится id, название, автор
# в библиотеке хранятся книги

class Book:
    def __init__(self, name, author, year, id):
        self.name = name
        self.author = author
        self.year = year
        self.id = id


class Library:
    def __init__(self, books: list):
        self.books = books

    def add_book(self, book: Book):
        self.books.append(book)

    def show_books(self):
        book_names = []
        for i in self.books:
            book_names.append(i.name)

        return book_names


book1 = Book("Азбука", "Кирилл и Мефодий", 100, 999999)
book2 = Book("Букварь", "Афанасий", 2000, 999998)

books = []
library = Library(books)

library.add_book(book1)
library.add_book(book2)

print(library.show_books())
