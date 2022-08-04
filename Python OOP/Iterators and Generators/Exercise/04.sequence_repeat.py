import unittest


class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.number:
            raise StopIteration
        result = self.sequence[self.idx % len(self.sequence)]
        self.idx += 1
        return result


# test zero


class Tests(unittest.TestCase):
    def test_zero(self):
        result = list(sequence_repeat('abc', 5))
        self.assertEqual(result, ['a', 'b', 'c', 'a', 'b'])


if __name__ == '__main__':
    unittest.main()
