import core
import pytest


class TestDidYouCopyBookClassExamples:
    '''You should at least be copying code down from the book.
    Copying the code gives you the opportunity to make simple mistakes (and learn from them) early.'''

    def test_class_Book_should_exist(self):
        assert isinstance(core.Book, type)

    def test_python_book_should_exist(self):
        assert isinstance(core.python_book, core.Book)

    def test_survival_book_should_exist(self):
        assert isinstance(core.survival_book, core.Book)

    def test_example_book_should_be_correctly_initialized(self):
        assert core.python_book.title == 'Practical Programming'
        assert core.python_book.authors == [
            'Campbell', 'Gries', 'Montojo']
        assert core.python_book.publisher == 'Pragmatic Bookshelf'
        assert core.python_book.ISBN == '978-1-93778-545-1'
        assert core.python_book.price == 25.0

    def test_python_book_should_have_3_authors(self):
        assert core.python_book.num_authors() == 3

    def test_survival_book_should_have_one_author(self):
        assert core.survival_book.num_authors() == 1

    def test_Book_str_should_be_implemented(self):
        expected = '''Title: Practical Programming
Authors: Campbell, Gries, Montojo
Publisher: Pragmatic Bookshelf
ISBN: 978-1-93778-545-1
Price: $25.0'''
        assert str(core.python_book) == expected

    def test_python_book_should_not_equal_survival_book(self):
        assert core.python_book != core.survival_book

    def test_python_book_should_equal_python_book(self):
        assert core.python_book == core.python_book

    def test_python_book_should_equal_book_with_same_isbn(self):
        same_isbn = core.Book(
            'title', ['author'], 'publisher',
            core.python_book.ISBN, 10)
        assert core.python_book == same_isbn