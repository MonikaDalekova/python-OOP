from project.soccer_player import SoccerPlayer
from unittest import TestCase, main


class TestSoccerPlayer(TestCase):
    _VALID_TEAMS = ["Barcelona", "Real Madrid", "Manchester United", "Juventus", "PSG"]

    def setUp(self) -> None:
        self.p = SoccerPlayer("Hristo", 23, 10, "Barcelona")

    def test_init_correct_values(self):
        self.assertEqual(self.p.name, "Hristo")
        self.assertEqual(self.p.age, 23)
        self.assertEqual(self.p.goals, 10)
        self.assertEqual(self.p.team, "Barcelona")
        self.assertEqual(self.p.achievements, {})

    def test_wrong_name(self):
        with self.assertRaises(ValueError) as ve:
            self.p.name = "M"
        self.assertEqual("Name should be more than 5 symbols!", str(ve.exception))

    def test_wrong_name_equal_five(self):
        with self.assertRaises(ValueError) as ve:
            self.p.name = "Monik"
        self.assertEqual("Name should be more than 5 symbols!", str(ve.exception))

    def test_wrong_age(self):
        with self.assertRaises(ValueError) as ve:
            self.p.age = 10
        self.assertEqual("Players must be at least 16 years of age!", str(ve.exception))

    def test_goals_less_than_zero(self):
        self.assertEqual(self.p.goals, 10)
        self.p.goals = -1
        self.assertEqual(self.p.goals, 0)

    def test_team_not_in_valid_types(self):
        with self.assertRaises(ValueError) as ve:
            self.p.team = "Oreshak"
        self.assertEqual("Team must be one of the following: "
                         "Barcelona, Real Madrid, Manchester United, Juventus, PSG!", str(ve.exception))

    def test_change_team_new_team_not_in_valid_ones(self):
        result = self.p.change_team("Unknown team")
        self.assertEqual(result, "Invalid team name!")

    def test_change_team_not_existing_team(self):
        result = self.p.change_team("Oreshak")
        self.assertEqual(result, "Invalid team name!")

    def test_change_team_existing(self):
        result = self.p.change_team("Real Madrid")
        self.assertEqual(result, "Team successfully changed!")
        self.assertEqual(self.p.team, "Real Madrid")

    def test_add_new_achievement(self):
        self.p.add_new_achievement("New goal")
        self.assertEqual(self.p.achievements, {"New goal": 1})

    def test_add_new_achievement_existing(self):
        self.p.achievements = {"New goal": 0}
        self.p.add_new_achievement("New goal")
        self.assertEqual(self.p.achievements, {'New goal': 1})
        result = self.p.add_new_achievement("New goal")
        self.assertEqual(self.p.achievements, {'New goal': 2})
        self.assertEqual(result, "New goal has been successfully added to the achievements collection!")

    def test_lt_self_goals_less(self):
        another_player = SoccerPlayer("AnaMaria", 33, 15, "Real Madrid")
        self.assertEqual(self.p.__lt__(another_player), "AnaMaria is a top goal scorer! S/he scored more than Hristo.")

    def test_lt_self_goals_more(self):
        another_player = SoccerPlayer("AnaMaria", 33, 3, "Real Madrid")
        self.assertEqual(self.p.__lt__(another_player), "Hristo is a better goal scorer than AnaMaria.")


if __name__ == "__main__":
    main()
