'''
online reading system like kindle

requirements: (clarify)
1. library containing all books accept addiing and removing books
2. set a book to active book
3. library records the last page of all given books
4. display a page in active book

Core objects:
book
- id: int
- title: str
- pages/content: list<str>
- last page: int
library
- collection of all books: list<int>/dict<int>
- active book: int

check whether core objects cover all the requirements.
'''

class Book:
    id = 0
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.last_page = 0
        self.id  = Book.id
        Book.id += 1
        print('new book: id {} named {}'.format(self.id, self.title))

    def display_page(self, page):
        return self.content[page]

    def display_last_page(self):
        return self.content[self.last_page]

    def turn_page(self):
        self.last_page += 1

    def get_id(self):
        return self.id

class Library:
    def __init__(self):
        self.books = {}
        self.activeBook = None

    def add_book(self,book):
        self.books[book.get_id()] = book

    def remove_book(self,book):
        del self.books[book.get_id()]

    def set_active(self,book):
        self.activeBook = book.get_id()

    def display_page(self):
        self.books[self.activeBook].display_last_page()

    def turn_page(self):
        self.books[self.activeBook].turn_page()

    def get_books(self):
        print(self.books.keys())
        return self.books.items()


b1 = Book('abc',['a','b','c'])
b2 = Book('abcd',['a','b','c','d'])
b3 = Book('1234',['a1','b2','c3','d4'])
lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.get_books()
lib.remove_book(b2)
lib.get_books()
