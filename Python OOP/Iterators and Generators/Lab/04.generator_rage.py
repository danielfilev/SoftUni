import unittest


def genrange(start, end):
    n = start
    while n < end + 1:
        yield n
        n += 1


# test zero
class GenrangeTests(unittest.TestCase):
    def test_zero(self):
        res = list(genrange(1, 10))
        self.assertEqual(res, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()
