import unittest
from src.book import Book
from src.library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("1234", "Python Basics", "John Doe", 2020)
        self.book2 = Book("5678", "Advanced Python", "Jane Smith", 2021)
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book(self):
        book3 = Book("9101", "Data Science 101", "Alan Turing", 2022)
        self.library.add_book(book3)
        self.assertIn(book3, self.library.books.values())

    def test_borrow_book(self):
        self.library.borrow_book("1234")
        self.assertFalse(self.library.books["1234"].is_available)

    def test_return_book(self):
        self.library.borrow_book("1234")
        self.library.return_book("1234")
        self.assertTrue(self.library.books["1234"].is_available)

    def test_view_available_books(self):
        self.library.borrow_book("1234")
        available_books = self.library.view_available_books()
        self.assertEqual(len(available_books), 1)
        self.assertIn(self.book2, available_books)

if __name__ == "__main__":
    unittest.main()
