from src.book import Book
from src.library import Library

# Initialize Library
library = Library()

# Add Books
book1 = Book("1234", "Python Basics", "John Doe", 2020)
book2 = Book("5678", "Advanced Python", "Jane Smith", 2021)
library.add_book(book1)
library.add_book(book2)

# Borrow a Book
library.borrow_book("1234")
print(f"Available Books: {[book.title for book in library.view_available_books()]}")

# Return a Book
library.return_book("1234")
print(f"Available Books: {[book.title for book in library.view_available_books()]}")
