import unittest


def solution():

    def integers():
        n = 1
        while n:
            yield n
            n += 1

    def halves():

        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return (take, halves, integers)


# test zero


class TakeHalvesTests(unittest.TestCase):
    def test_zero(self):
        take = solution()[0]
        halves = solution()[1]
        result = take(5, halves())
        self.assertEqual(result, [0.5, 1.0, 1.5, 2.0, 2.5])


if __name__ == '__main__':
    unittest.main()
