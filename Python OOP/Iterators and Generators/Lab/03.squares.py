import unittest


def squares(n):
    num = 1
    while num < n + 1:
        yield num * num
        num += 1


# test zero
class SquaresTests(unittest.TestCase):
    def test_zero(self):
        res = list(squares(5))
        self.assertEqual(res, [1, 4, 9, 16, 25])


if __name__ == '__main__':
    unittest.main()
