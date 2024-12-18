from project.tennis_player import TennisPlayer

from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.t = TennisPlayer("Mon", 37, 2000)
        self.t_2 = TennisPlayer("Ico", 40, 1500)

    def test_correct_init(self):
        self.assertEqual("Mon", self.t.name)
        self.assertEqual(37, self.t.age)
        self.assertEqual(2000, self.t.points)
        self.assertEqual([], self.t.wins)

    def test_correct_name(self):
        with self.assertRaises(ValueError) as ve:
            self.t = TennisPlayer("M", 37, 2000)
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_proper_age(self):
        with self.assertRaises(ValueError) as ve:
            self.t = TennisPlayer("Mon", 12, 2000)
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_if_name_not_in_wins(self):
        self.t.add_new_win("Mati")

        self.assertEqual(self.t.wins, ["Mati"])

    def test_add_new_win_if_name_already_exist(self):
        self.t.add_new_win("Mati")
        result = self.t.add_new_win("Mati")

        self.assertEqual("Mati has been already added to the list of wins!", result)

    def test_lt_if_first_points_are_less(self):
        self.t = TennisPlayer("Moni", 37, 1500)
        self.t_2 = TennisPlayer("Ico", 40, 2000)

        result = self.t < self.t_2

        self.assertEqual("Ico is a top seeded player and he/she is better than Moni", result)

    def test_lt_if_first_points_are_higher(self):
        self.tennis_player = TennisPlayer('Alex', 20, 1519)
        self.other_player = TennisPlayer('Grigor', 30, 1520)

        result = self.tennis_player < self.other_player
        self.assertEqual(result, "Grigor is a top seeded player and he/she is better than Alex")

    def test__str__no_wins(self):
        self.tennis_player = TennisPlayer('Alex', 20, 0)
        self.assertEqual(self.tennis_player.wins, [])

        result = str(self.tennis_player)
        self.assertEqual(result, 'Tennis Player: Alex\nAge: 20\nPoints: 0.0\nTournaments won: ')

    def test__str__one_win(self):
        self.tennis_player = TennisPlayer('Alex', 20, 0)
        self.tennis_player.wins = ['AO 2023']

        result = str(self.tennis_player)
        self.assertEqual(result, 'Tennis Player: Alex\nAge: 20\nPoints: 0.0\nTournaments won: AO 2023')

    def test__str__two_wins(self):
        self.tennis_player = TennisPlayer('Alex', 20, 0)
        self.tennis_player.wins = ['AO 2023', 'FO 2022']

        result = str(self.tennis_player)
        self.assertEqual(result, 'Tennis Player: Alex\nAge: 20\nPoints: 0.0\nTournaments won: AO 2023, FO 2022')


if __name__ == "__main__":
    main()