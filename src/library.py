from src.book import Book

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.isbn in self.books:
            raise ValueError("Book with this ISBN already exists.")
        self.books[book.isbn] = book

    def borrow_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book not found.")
        if not self.books[isbn].is_available:
            raise ValueError("Book is currently not available.")
        self.books[isbn].is_available = False

    def return_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book not found.")
        if self.books[isbn].is_available:
            raise ValueError("Book is not borrowed.")
        self.books[isbn].is_available = True

    def view_available_books(self):
        return [book for book in self.books.values() if book.is_available]
