import unittest
from exercise.movie import Movie


class MovieTests(unittest.TestCase):

    NAME = "DN"
    YEAR = 2015
    RATING = 9.99
    MIN_YEAR = 1887

    def setUp(self):

        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test__init__(self):

        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test__name__setter_not_working(self):

        with self.assertRaises(ValueError) as ex:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test__year__setter_raises_error_when_year_too_early(self):

        with self.assertRaises(ValueError) as ex:
            self.movie.year = self.MIN_YEAR - 10
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test__add_actor__when_actor_is_already_added(self):

        self.movie.actors = ["Dido", "Nia"]
        name = "Dido"
        result = self.movie.add_actor(name)
        self.assertEqual(
            f"{name} is already added in the list of actors!", result)

    def test__add_actor__when_actor_is_not_added(self):

        self.movie.actors = ["Ne", "Da"]
        expected = ["Ne", "Da", "Moje bi"]
        actor = "Moje bi"
        self.movie.add_actor(actor)
        self.assertEqual(expected, self.movie.actors)

    def test__gt__method_when_other_rating_is_more(self):

        other = Movie("Ayryan", 2000, 10)
        result = self.movie.__gt__(other)
        expected = f'"{other.name}" is better than "{self.movie.name}"'
        self.assertEqual(expected, result)

    def test__gt__method_when_self_rating_is_more(self):

        other = Movie("Tupa boza", 2000, 0.33)
        result = self.movie.__gt__(other)
        expected = f'"{self.movie.name}" is better than "{other.name}"'
        self.assertEqual(expected, result)

    def test__repr__method(self):

        expected = f"Name: {self.NAME}\n" \
            f"Year of Release: {self.YEAR}\n" \
            f"Rating: {self.RATING:.2f}\n" \
            f"Cast: {', '.join(self.movie.actors)}"
        result = repr(self.movie)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
