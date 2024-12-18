from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.film = Movie("It", 2007, 8.0)

    def test_init_correct_values(self):
        self.assertEqual(self.film.name, "It")
        self.assertEqual(self.film.year, 2007)
        self.assertEqual(self.film.rating, 8.0)
        self.assertEqual(self.film.actors, [])

    def test_wrong_name(self):
        with self.assertRaises(ValueError) as ve:
            self.film.name = ""
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_lower_year(self):
        with self.assertRaises(ValueError) as ve:
            self.film.year = 1885
        self.assertEqual("Year is not valid!", str(ve.exception))

    def tests_add_actor_name_not_in_self_actors(self):
        self.assertEqual(self.film.actors, [])
        self.film.add_actor("Moni")
        self.assertEqual(self.film.actors, ["Moni"])

    def test_add_actor_name_already_in_the_list(self):
        self.assertEqual(self.film.actors, [])
        result = self.film.add_actor("Moni")
        result = self.film.add_actor("Mati")
        result = self.film.add_actor("Moni")
        self.assertEqual(self.film.actors, ["Moni", "Mati"])
        self.assertEqual("Moni is already added in the list of actors!", result)

    def test__gt__self_rating_higher_than_other_rating(self):
        other_film = Movie("Her", 2007, 7.0)
        result = self.film.__gt__(other_film)
        self.assertEqual('"It" is better than "Her"', result)

    def test__gt__self_rating_lower_than_other_rating(self):
        other_film = Movie("Her", 2007, 10.0)
        result = other_film.__gt__(self.film)
        self.assertEqual('"Her" is better than "It"', result)

    def test_repr(self):
        self.film.add_actor("Moni")
        self.film.add_actor("Mati")
        self.assertEqual(f"Name: It\n"
                         f"Year of Release: 2007\n"
                         f"Rating: 8.00\n"
                         f"Cast: Moni, Mati", repr(self.film))


if __name__ == "__main__":
    main()