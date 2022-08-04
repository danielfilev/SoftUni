import unittest


class countdown_iterator:

    def __init__(self, count):
        self.count = count
        self.value = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == 0:
            raise StopIteration
        self.value -= 1
        return self.value


# test zero

class CountdownIteratorTests(unittest.TestCase):
    def test_zero(self):
        iterator = countdown_iterator(10)
        result = []
        for item in iterator:
            result.append(item)
        self.assertEqual(result, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])


if __name__ == '__main__':
    unittest.main()
