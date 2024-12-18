from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self) -> None:
        self.ts = RailwayStation("Monika")

    def test_init_correct_info(self):
        self.assertEqual("Monika", self.ts.name)
        self.assertEqual(self.ts.arrival_trains, deque())
        self.assertEqual(self.ts.departure_trains, deque())

    def test_lower_len__name(self):
        with self.assertRaises(ValueError) as ve:
            self.ts = RailwayStation("Mo")
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_equal_len__name(self):
        with self.assertRaises(ValueError) as ve:
            self.ts = RailwayStation("Mon")
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board(self):
        self.assertEqual(self.ts.arrival_trains, deque())

        self.ts.new_arrival_on_board("Some info")

        self.assertEqual(self.ts.arrival_trains, deque(["Some info"]))

    def test_train_has_arrived_with_different_train(self):
        self.ts.new_arrival_on_board("Test")
        self.assertEqual(self.ts.arrival_trains, deque(["Test"]))

        result = self.ts.train_has_arrived("Sofia")

        self.assertEqual(len(self.ts.arrival_trains), 1)
        self.assertNotEqual(self.ts.arrival_trains[0], "Sofia")
        self.assertEqual("There are other trains to arrive before Sofia.", result)

    def test_train_has_arrived_with_actual_train(self):
        self.ts.new_arrival_on_board("Test")

        self.assertEqual(len(self.ts.arrival_trains), 1)
        self.assertEqual(len(self.ts.departure_trains), 0)

        train_info = "Test"

        result = self.ts.train_has_arrived(train_info)

        self.assertEqual(f"{train_info} is on the platform and will leave in 5 minutes.", result)

        self.assertEqual(len(self.ts.arrival_trains), 0)
        self.assertEqual(len(self.ts.departure_trains), 1)

    def test_train_has_left_true(self):
        self.assertEqual(len(self.ts.departure_trains), 0)

        self.ts.new_arrival_on_board("Test")

        train_info = "Test"

        result = self.ts.train_has_arrived(train_info)

        self.assertEqual(len(self.ts.departure_trains), 1)

        train_info = "Test"

        result = self.ts.train_has_left(train_info)

        self.assertTrue(result)

    def test_train_has_left_false(self):

        self.assertEqual(len(self.ts.departure_trains), 0)

        self.ts.new_arrival_on_board("Test")

        train_info = "Test"

        result = self.ts.train_has_arrived(train_info)

        self.assertEqual(len(self.ts.departure_trains), 1)

        train_info = "Sofia"

        result = self.ts.train_has_left(train_info)

        self.assertFalse(result)


if __name__ == "__main__":
    main()