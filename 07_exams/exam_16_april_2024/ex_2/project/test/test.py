from unittest import TestCase, main

from project.restaurant import Restaurant


class TestRestaurant(TestCase):
    def setUp(self) -> None:
        self.r = Restaurant("Mati", 4)

    def test_init_correct(self):
        self.assertEqual(self.r.name, "Mati")
        self.assertEqual(self.r.capacity, 4)
        self.assertEqual(self.r.waiters, [])

    def test_name_wrong_without_value(self):
        with self.assertRaises(ValueError) as ve:
            self.r.name = ''
        self.assertEqual("Invalid name!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.r.name = ' '
        self.assertEqual("Invalid name!", str(ve.exception))

    def test_capacity_below_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.r.capacity = -2
        self.assertEqual("Invalid capacity!", str(ve.exception))

    def test_get_waiters_expect_empty(self):
        self.r.waiters = []
        result = self.r.get_waiters()
        self.assertEqual(result, [])

    def test_get_waiters_adding_one(self):
        self.r.add_waiter('Pesho')
        result = self.r.get_waiters()
        self.assertEqual(result, [{'name': 'Pesho'}])

    def test_get_waiters_min_earnings(self):
        self.r.add_waiter('Pesho')
        self.r.add_waiter('Gosho')
        self.r.waiters[0]['total_earnings'] = 1
        self.r.waiters[1]['total_earnings'] = 5
        expect = [{'name': 'Gosho', 'total_earnings': 5}]
        actual = self.r.get_waiters(min_earnings=2)
        self.assertEqual(expect, actual)

    def test_get_waiters__expect_waiter_max_earnings(self):
        self.r.add_waiter('Pesho')
        self.r.add_waiter('Gosho')
        self.r.waiters[0]['total_earnings'] = 1
        self.r.waiters[1]['total_earnings'] = 5
        expect = [{'name': 'Pesho', 'total_earnings': 1}]
        actual = self.restaurant.get_waiters(max_earnings=2)
        self.assertEqual(expect, actual)

    def test_get_waiters__expect_waiter_min_max_earnings(self):
        self.r.add_waiter('Pesho')
        self.r.add_waiter('Gosho')
        self.r.add_waiter('Minka')
        self.r.waiters[0]['total_earnings'] = 1
        self.r.waiters[1]['total_earnings'] = 5
        self.r.waiters[2]['total_earnings'] = 7
        expect = [{'name': 'Gosho', 'total_earnings': 5}]
        actual = self.r.get_waiters(min_earnings=2, max_earnings=6)
        self.assertEqual(expect, actual)

    def test_add_waiters_equal_to_capacity(self):
        self.assertEqual(self.r.waiters, [])
        self.r.waiters = ["Pesho", "Gosho", "Misho", "Tosho"]
        result = self.r.add_waiter("Tisho")
        self.assertEqual("No more places!", result)

    def test_add_waiter_already_exist(self):
        self.r.add_waiter('Pesho')
        result = self.r.add_waiter('Pesho')
        self.assertEqual(result, "The waiter Pesho already exists!")

    def test_add_waiter_not_exist(self):
        self.r.add_waiter('Pesho')
        result = self.r.add_waiter('Misho')
        self.assertEqual(self.r.waiters, [{'name': 'Pesho'}, {'name': 'Misho'}])
        self.assertEqual(result, "The waiter Misho has been added.")

    def test_remove_existing_waiter(self):
        self.r.add_waiter('Pesho')
        self.r.add_waiter('Misho')
        self.assertEqual(self.r.waiters, [{'name': 'Pesho'}, {'name': 'Misho'}])
        result = self.r.remove_waiter('Pesho')
        self.assertEqual(self.r.waiters, [{'name': 'Misho'}])
        self.assertEqual(result, "The waiter Pesho has been removed.")

    def test_remove_not_existing_waiter(self):
        self.r.add_waiter('Pesho')
        self.r.add_waiter('Misho')
        self.assertEqual(self.r.waiters, [{'name': 'Pesho'}, {'name': 'Misho'}])
        result = self.r.remove_waiter('moni')
        self.assertEqual(result, "No waiter found with the name moni.")

    def test_get_total_earnings__expect_no_waiter(self):
        expect = 0
        actual = self.r.get_total_earnings()
        self.assertEqual(expect, actual)

    def test_get_total_earnings__expect_one_waiter(self):
        self.r.add_waiter('Pesho')
        self.r.waiters[0]['total_earnings'] = 10
        expect = 10
        actual = self.r.get_total_earnings()
        self.assertEqual(expect, actual)

    def test_get_total_earnings__expect_one_plus_waiters(self):
        self.r.add_waiter('Pesho')
        self.r.waiters[0]['total_earnings'] = 10
        self.r.add_waiter('Gosho')
        self.r.waiters[1]['total_earnings'] = 10
        expect = 20
        actual = self.r.get_total_earnings()
        self.assertEqual(expect, actual)


if __name__ == "__main__":
    main()