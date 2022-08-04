import unittest


class dictionary_iter:

    def __init__(self, data):
        self.items = list(data.items())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == len(self.items):
            raise StopIteration
        result = self.items[self.idx]
        self.idx += 1
        return result

# test zero


class DictionaryIteratorTests(unittest.TestCase):
    def test_zero(self):
        result = dictionary_iter({1: "1", 2: "2"})
        expected = []
        for x in result:
            expected.append(x)
        self.assertEqual(expected, [(1, "1"), (2, "2")])


if __name__ == '__main__':
    unittest.main()
