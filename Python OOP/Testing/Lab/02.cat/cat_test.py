import unittest
from cat_exercise.cat import Cat


class CatTests(unittest.TestCase):

    NAME = "Jason"

    def setUp(self):
        self.kitty = Cat(self.NAME)

    def test__check_if__size_increased_after_eating(self):

        self.kitty.eat()
        self.assertEqual(self.kitty.size, 1)

    def test__check_if__cat_is_fed_after_eating(self):

        self.kitty.eat()
        self.assertTrue(self.kitty.fed)

    def test__check_if_cat_can_eat_while_fed(self):

        self.kitty.eat()

        with self.assertRaises(Exception) as ex:
            self.kitty.eat()
        self.assertIsNotNone(ex)

    def test__check_if__cat_can_sleep_if_not_fed(self):

        with self.assertRaises(Exception) as ex:
            self.kitty.sleep()
        self.assertIsNotNone(ex)

    def test__check_if__cat_is_sleepy_after_sleeping(self):

        self.kitty.eat()
        self.kitty.sleep()

        self.assertFalse(self.kitty.sleepy)


if __name__ == "__main__":
    unittest.main()
