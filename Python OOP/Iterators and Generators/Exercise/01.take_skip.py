import unittest


class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.iterations * self.step
        self.iterations += 1
        if self.iterations > self.count:
            raise StopIteration
        return result


# test zero
class TakeSkipTests(unittest.TestCase):
    def test_zero(self):
        numbers = take_skip(2, 6)
        res = []
        for number in numbers:
            res.append(number)
        self.assertEqual(res, [0, 2, 4, 6, 8, 10])


if __name__ == '__main__':
    unittest.main()
