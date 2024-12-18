from project.furniture import Furniture
from unittest import TestCase, main


class TestFurniture(TestCase):
    def setUp(self) -> None:
        self.f = Furniture("table", 100.0, (10, 5, 2), True, 10)

    def test_init_correct_numbers(self):
        self.assertEqual(self.f.model, "table")
        self.assertEqual(self.f.price, 100.)
        self.assertEqual(self.f.dimensions, (10, 5, 2))
        self.assertEqual(self.f.in_stock, True)
        self.assertEqual(self.f.weight, 10)

    def test_wrong_model_name(self):
        with self.assertRaises(ValueError) as ve:
            self.f.model = ""
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.f.model = "jhnfzsjhrfhszjfgbszjgfsjzgefshzbfjsegfsjgbzmhfgzjsgejge\jgjagswa\hfvb"
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ve.exception))

    def test_price_higher_than_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.f.price = -1
        self.assertEqual("Price must be a non-negative number.", str(ve.exception))

    def test_dimensions_len_equal_to_three(self):
        with self.assertRaises(ValueError) as ve:
            self.f.dimensions = (1, 2, 3, 4)
        self.assertEqual("Dimensions tuple must contain 3 integers.", str(ve.exception))

    def test_dimensions_wrong_sizes(self):
        with self.assertRaises(ValueError) as ve:
            self.f.dimensions = (0, 0, 0)
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(ve.exception))

    def test_weight_below_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.f.weight = -1
        self.assertEqual("Weight must be greater than zero.", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.f.weight = 0.0
        self.assertEqual("Weight must be greater than zero.", str(ve.exception))

    def test_get_available_status_in_stock(self):
        expected = "Model: table is currently in stock."
        self.assertEqual(self.f.get_available_status(), expected)

    def test_get_available_status_not_in_stock(self):
        self.f.in_stock = False
        expected = "Model: table is currently unavailable."
        self.assertEqual(self.f.get_available_status(), expected)

    def test_get_specifications_existing_weight(self):
        expected = "Model: table has the following dimensions: 10mm x 5mm x 2mm and weighs: 10"
        self.assertEqual(self.f.get_specifications(), expected)

    def test_get_specifications_no_weight(self):
        f = Furniture("table", 100.0, (10, 5, 2), True)
        expected = "Model: table has the following dimensions: 10mm x 5mm x 2mm and weighs: N/A"
        self.assertEqual(f.get_specifications(), expected)


if __name__ == "__main__":
    main()

