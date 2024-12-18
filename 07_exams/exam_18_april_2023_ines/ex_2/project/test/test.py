from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.r = Robot("88", "Military", 50, 10)

    def test_init_valid(self):
        self.assertEqual("88", self.r.robot_id)
        self.assertEqual("Military", self.r.category)
        self.assertEqual(50, self.r.available_capacity)
        self.assertEqual(10, self.r.price)
        self.assertEqual([], self.r.hardware_upgrades)
        self.assertEqual([], self.r.software_updates)

    def test_init_invalid_category_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.r = Robot("88", "Moni", 50, 10)

        self.assertEqual(f"Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'", str(ve.exception))

    def test_init_invalid_price_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.r = Robot("88", "Military", 50, -10)

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_existing_hardware_component(self):
        self.r.hardware_upgrades.append("Part A")
        self.assertEqual(self.r.hardware_upgrades, ["Part A"])
        self.assertEqual(self.r.price, 10)

        result = self.r.upgrade("Part A", 10)

        self.assertEqual(self.r.hardware_upgrades, ["Part A"])
        self.assertEqual(self.r.price, 10)
        self.assertEqual("Robot 88 was not upgraded.", result)

    def test_upgrade_new_hardware_component(self):
        self.r.hardware_upgrades.append("Part A")
        self.assertEqual(self.r.hardware_upgrades, ["Part A"])
        self.assertEqual(self.r.price, 10)

        result = self.r.upgrade("Part B", 2)

        self.assertEqual(self.r.hardware_upgrades, ["Part A", "Part B"])
        self.assertEqual(self.r.price, 13)
        self.assertEqual('Robot 88 was upgraded with Part B.', result)

    def test_update_no_updates(self):
        self.assertEqual(self.r.software_updates, [])
        self.assertEqual(self.r.available_capacity, 50)

        result = self.r.update(15, 200)

        self.assertEqual(self.r.software_updates, [])
        self.assertEqual(self.r.available_capacity, 50)
        self.assertEqual('Robot 88 was not updated.', result)

    def test_update_version_is_less_than_existing_updates(self):
        self.r.software_updates = [10]
        self.assertEqual(self.r.software_updates, [10])
        self.assertEqual(self.r.available_capacity, 50)

        result = self.r.update(15, 200)

        self.assertEqual(self.r.software_updates, [10])
        self.assertEqual(self.r.available_capacity, 50)
        self.assertEqual('Robot 88 was not updated.', result)

    def test_update_available_capacity(self):
        self.assertEqual(self.r.software_updates, [])
        self.assertEqual(self.r.available_capacity, 50)

        self.r.software_updates.append(2)

        self.assertEqual(self.r.software_updates, [2])
        self.assertEqual(self.r.available_capacity, 50)

        result = self.r.update(3, 3)

        self.assertEqual(self.r.software_updates, [2, 3])
        self.assertEqual(self.r.available_capacity, 47)
        self.assertEqual('Robot 88 was updated to version 3.', result)

    def test_gt_self_price_greater_than_other_price(self):
        robot_less = Robot("89", "Military", 50, 1)
        robot_equal = Robot("90", "Military", 50, 10)
        robot_greater = Robot("91", "Military", 50, 20)

        result = self.r.__gt__(robot_less)
        self.assertEqual('Robot with ID 88 is more expensive than Robot with ID 89.', result)

        result = self.r.__gt__(robot_equal)
        self.assertEqual('Robot with ID 88 costs equal to Robot with ID 90.', result)

        result = self.r.__gt__(robot_greater)
        self.assertEqual('Robot with ID 88 is cheaper than Robot with ID 91.', result)


if __name__ == "__main__":
    main()