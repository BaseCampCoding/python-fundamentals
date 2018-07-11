import core
import inspect
import pytest


class TestMovie:
    @staticmethod
    def test_class_Movie_should_exist():
        assert isinstance(core.Movie, type)

    @staticmethod
    def test_init_should_have_correct_parameters():
        '''
        Movie's __init__ method should have 5 parameters:
            - self
            - title
            - director
            - genre
            - cast
        '''
        params = inspect.getargspec(core.Movie).args

        assert params == ['self', 'title', 'director', 'genre', 'cast']

    @staticmethod
    def test_init_should_apporiately_set_attributes():
        '''
        Movie's __init__ method should initialize self with
        attributes corresponding to each of the initializers
        parameters.
        '''
        movie = core.Movie('Toy Story', 'John Lasseter', 'Children\'s',
                           ['Tom Hanks', 'Tim Allen'])

        assert movie.title == 'Toy Story'
        assert movie.director == 'John Lasseter'
        assert movie.genre == 'Children\'s'
        assert movie.cast == ['Tom Hanks', 'Tim Allen']

    @staticmethod
    def test_Movie_str_should_be_implemented():
        '''
        Movie's __str__ method should be defined to return
        a string like the expected string below.
        '''
        movie = core.Movie(
            'Toy Story',
            'John Lasseter',
            'Children\'s',
            ['Tom Hanks', 'Tim Allen'], )

        expected = '''Title: Toy Story
Director: John Lasseter
Genre: Children's
Cast:
- Tom Hanks
- Tim Allen'''

        assert str(movie) == expected

    @staticmethod
    def test_Movie_should_define_equality_by_its_parts():
        '''
        A Movie is equal to another movie if both movies have
        all the same attributes.
        '''
        movie1 = core.Movie(
            'Toy Story',
            'John Lasseter',
            'Children\'s',
            ['Tom Hanks', 'Tim Allen'], )
        movie2 = core.Movie(
            'Toy Story',
            'John Lasseter',
            'Children\'s',
            ['Tom Hanks', 'Tim Allen'], )

        assert movie1 == movie2


class TestFMDB:
    @staticmethod
    def test_class_FMDB_should_exist():
        assert isinstance(core.FMDB, type)

    @staticmethod
    def test_init_should_have_correct_parameters():
        '''
        FMDB's __init__ method should have 2 parameters:
            - self
            - movies
        '''
        params = inspect.getargspec(core.FMDB).args

        assert params == ['self', 'movies']

    @staticmethod
    def test_init_should_appropriately_set_attributes():
        '''
        FMDB's __init__ method should initialize self with
        attributes corresponding to each of the initializers
        parameters.
        '''
        movies = [
            core.Movie('title1', 'dir1', 'genre1', ['a1', 'a2', 'a3']),
            core.Movie('title2', 'dir2', 'genre1', ['a3', 'a2', 'a4']),
            core.Movie('title3', 'dir1', 'genre2', ['a2', 'a4']),
        ]
        fmdb = core.FMDB(movies)
        assert fmdb.movies == movies

    @staticmethod
    def test_movies_by_cast_member_should_work():
        '''
        FMDB's movies_by_cast_member method should return a
        list of movies. Each returned movie should have the provided
        cast member in its cast.
        '''
        movies = [
            core.Movie('title1', 'dir1', 'genre1', ['a1', 'a2', 'a3']),
            core.Movie('title2', 'dir2', 'genre1', ['a3', 'a2', 'a4']),
            core.Movie('title3', 'dir1', 'genre2', ['a2', 'a4']),
        ]
        fmdb = core.FMDB(movies)

        assert fmdb.movies_by_cast_member('a1') == [
            core.Movie('title1', 'dir1', 'genre1', ['a1', 'a2', 'a3'])
        ]

        assert fmdb.movies_by_cast_member('a2') == movies

        assert fmdb.movies_by_cast_member('nate') == []

    @staticmethod
    def test_movies_by_director_should_work():
        '''
        FMDB's movie_by_director method should return a
        list of movies. Each returned movie should have the provided
        director as its director.
        '''
        movies = [
            core.Movie('title1', 'dir1', 'genre1', ['a1', 'a2', 'a3']),
            core.Movie('title2', 'dir2', 'genre1', ['a3', 'a2', 'a4']),
            core.Movie('title3', 'dir1', 'genre2', ['a2', 'a4']),
        ]
        fmdb = core.FMDB(movies)

        assert fmdb.movies_by_director('dir1') == [
            core.Movie('title1', 'dir1', 'genre1', ['a1', 'a2', 'a3']),
            core.Movie('title3', 'dir1', 'genre2', ['a2', 'a4']),
        ]

        assert fmdb.movies_by_director('dir2') == [
            core.Movie('title2', 'dir2', 'genre1', ['a3', 'a2', 'a4']),
        ]

        assert fmdb.movies_by_director('nate') == []
