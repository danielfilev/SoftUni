import unittest


def fibonacci():
    current = 0
    previous = 1
    yield current
    yield previous

    while True:
        result = current + previous
        current, previous = previous, result
        yield result


# test zero


class FibonacciTests(unittest.TestCase):
    def test_zero(self):
        numbers = [0, 1, 1, 2, 3]
        generator = fibonacci()
        for i in range(5):
            self.assertEqual(next(generator), numbers[i])


if __name__ == '__main__':
    unittest.main()
