from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.p = Plantation(20)

    def test_init_correct_values(self):
        self.assertEqual(self.p.size, 20)
        self.assertEqual(self.p.plants, {})
        self.assertEqual(self.p.workers, [])

    def test_lower_than_zero_size(self):
        with self.assertRaises(ValueError) as ve:
            self.p.size = -2
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_that_already_exist(self):
        self.assertEqual(self.p.workers, [])

        self.p.hire_worker("Mimi")
        self.assertEqual(self.p.workers, ["Mimi"])

        with self.assertRaises(ValueError) as ve:
            self.p.hire_worker("Mimi")
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_do_not_exist(self):
        self.assertEqual(self.p.workers, [])
        result = self.p.hire_worker("Mimi")
        self.assertEqual(self.p.workers, ["Mimi"])
        self.assertEqual("Mimi successfully hired.", result)
        self.assertEqual(1, len(self.p.workers))

    def test_len_(self):
        self.p.hire_worker("Test")
        self.p.hire_worker("Test2")
        self.assertEqual(len(self.p.workers), 2)

        self.p.planting("Test", "Rose")
        self.p.planting("Test2", "Tulip")
        self.p.planting("Test", "Rose2")
        self.assertEqual(len(self.p.plants), 2)

        result = self.p.__len__()
        self.assertEqual(result, 3)

    def test_planting_worker_not_in_self_workers(self):
        self.assertEqual(self.p.workers, [])
        self.p.hire_worker("Mimi")
        self.assertEqual(self.p.workers, ["Mimi"])
        with self.assertRaises(ValueError) as ve:
            self.p.planting("Test", "tulip")
        self.assertEqual("Worker with name Test is not hired!", str(ve.exception))
        self.assertEqual(self.p.workers, ["Mimi"])

    def test_planting_is_full_raises_errors(self):
        self.p1 = Plantation(0)
        self.p1.hire_worker("Test")
        self.p1.__len__()
        with self.assertRaises(ValueError) as ve:
            self.p1.planting("Test", "Rose")
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_worker_in_plants(self):
        self.p.hire_worker("Test")
        self.p.hire_worker("Test2")
        self.assertEqual(len(self.p.workers), 2)

        self.p.plants = {"Test": [], "Test2": []}

        result = self.p.planting("Test", "Rose")
        self.assertEqual({"Test": ["Rose"], "Test2": []}, self.p.plants)
        self.assertEqual("Test planted Rose.", result)

    def test_planting_worker_not_in_plants(self):
        self.p.hire_worker("Test")
        self.p.hire_worker("Test2")
        self.p.hire_worker("Test3")
        self.assertEqual(len(self.p.workers), 3)
        self.p.plants = {"Test": [], "Test2": []}

        result = self.p.planting("Test3", "Tulip")
        self.assertEqual({"Test": [], "Test2": [], "Test3": ["Tulip"]}, self.p.plants)
        self.assertEqual("Test3 planted it's first Tulip.", result)

    def test_str_(self):
        self.p.hire_worker("Moni")
        self.p.planting("Moni", "Rose")
        expected = "Plantation size: 20\nMoni\nMoni planted: Rose"
        self.assertEqual(self.p.__str__(), expected)

    def test_repr_(self):
        self.p.hire_worker("Moni")
        expected = "Size: 20\nWorkers: Moni"
        self.assertEqual(self.p.__repr__(), expected)


if __name__ == "__main__":
    main()