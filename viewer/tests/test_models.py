from django.test import TestCase

from viewer.models import Genre, Movie


class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        drama = Genre.objects.create(name="Drama")

    def setUp(self):
        print('-' * 80)

    def test_repr(self):
        drama = Genre.objects.get(id=1)
        print(f"test_repr: '{drama.__repr__()}'")
        self.assertEqual(drama.__repr__(), "Genre(name=Drama)")

    def test_str(self):
        drama = Genre.objects.get(id=1)
        print(f"test_str: '{drama.__str__()}'")
        self.assertEqual(drama.__str__(), "Drama")


class MovieModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        movie = Movie.objects.create(
            title_orig="The Green Mile",
            title_cz="Zelená míle",
            length=123
        )

    def test_length_format(self):
        movie = Movie.objects.get(id=1)
        print(f"test_length_format: {movie.length_format()}")
        self.assertEqual(movie.length_format(), "2:03")
