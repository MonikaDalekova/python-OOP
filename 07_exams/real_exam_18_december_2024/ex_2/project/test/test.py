from project.gallery import Gallery
from unittest import TestCase, main


class TestGallery(TestCase):
    def setUp(self) -> None:
        self.g = Gallery('Monika', 'Sofia', 100.0, True)

    def test_init_correct(self):
        self.assertEqual('Monika', self.g.gallery_name)
        self.assertEqual('Sofia', self.g.city)
        self.assertEqual(100.0, self.g.area_sq_m)
        self.assertEqual(True, self.g.open_to_public)
        self.assertEqual({}, self.g.exhibitions)

    def test_wrong_gallary_name(self):
        with self.assertRaises(ValueError) as ve:
            self.g = Gallery('Monika@', 'Sofia', 100.0, True)
        self.assertEqual("Gallery name can contain letters and digits only!", str(ve.exception))

    def test_city_wrong_name(self):
        with self.assertRaises(ValueError) as ve:
            self.g = Gallery('Monika', '@Sofia', 100.0, True)
        self.assertEqual("City name must start with a letter!", str(ve.exception))

    def test_are_below_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.g = Gallery('Monika', 'Sofia', -1.5, True)
        self.assertEqual("Gallery area must be a positive number!", str(ve.exception))

    def test_add_exhibition_which_already_exist(self):
        self.g.exhibitions = {'Books': 1998, 'Toys': 1999}
        result = self.g.add_exhibition('Books', 1998)
        self.assertEqual(self.g.exhibitions, {'Books': 1998, 'Toys': 1999})
        self.assertEqual('Exhibition "Books" already exists.', result)

    def test_add_exhibition_which_not_exist(self):
        self.g.exhibitions = {'Books': 1998, 'Toys': 1999}
        result = self.g.add_exhibition('Cats', 1998)
        self.assertEqual({'Books': 1998, 'Toys': 1999, 'Cats': 1998}, self.g.exhibitions)
        self.assertEqual('Exhibition "Cats" added for the year 1998.', result)

    def test_remove_exhibition_which_not_exist(self):
        self.g.exhibitions = {'Books': 1998, 'Toys': 1999}
        result = self.g.remove_exhibition('Cats')
        self.assertEqual(self.g.exhibitions, {'Books': 1998, 'Toys': 1999})
        self.assertEqual('Exhibition "Cats" not found.', result)

    def test_remove_exhibition_which_exist(self):
        self.g.exhibitions = {'Books': 1998, 'Toys': 1999}
        result = self.g.remove_exhibition('Books')
        self.assertEqual(self.g.exhibitions, {'Toys': 1999})
        self.assertEqual('Exhibition "Books" removed.', result)

    def test_list_exhibitions_not_open_to_public(self):
        self.g.exhibitions = {}
        self.g.open_to_public = False
        result = self.g.list_exhibitions()
        self.assertEqual('Gallery Monika is currently closed for public! Check for updates later on.', result)

    def test_list_exhibitions_open_to_public(self):
        self.g.exhibitions = {'Books': 1998, 'Toys': 1999}
        result = self.g.list_exhibitions()
        self.assertEqual('\n'.join(f"{name}: {year}" for name, year in self.g.exhibitions.items()), result)


if __name__ == "__main__":
    main()