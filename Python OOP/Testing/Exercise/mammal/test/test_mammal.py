import unittest
from project.mammal import Mammal


class MammalTests(unittest.TestCase):

    NAME = "Candace"
    TYPE = "Dolphin"
    SOUND = "Ek Ek Ek Ek"

    def setUp(self):
        self.mammal = Mammal(self.NAME, self.TYPE, self.SOUND)

    def test__working__init__(self):
        self.assertEqual("Candace", self.mammal.name)
        self.assertEqual("Dolphin", self.mammal.type)
        self.assertEqual("Ek Ek Ek Ek", self.mammal.sound)

    def test__make_sound(self):
        expected_name = "Candace"
        expected_sound = "Ek Ek Ek Ek"
        expected_message = f"{expected_name} makes {expected_sound}"
        self.assertEqual(expected_message, self.mammal.make_sound())

    def test__get_animal_kingdom(self):
        expected_message = "animals"
        self.assertEqual(expected_message, self.mammal.get_kingdom())

    def test__info(self):
        expected_message = f"{self.NAME} is of type {self.TYPE}"
        self.assertEqual(expected_message, self.mammal.info())


if __name__ == '__main__':
    unittest.main()
