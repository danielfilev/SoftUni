import unittest


class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.next_value = start

    def __iter__(self):
        return self

    def __next__(self):

        if self.next_value > self.end:
            raise StopIteration

        value_to_return = self.next_value
        self.next_value += 1
        return value_to_return


# zero test
class CustomRangeTests(unittest.TestCase):
    def test_zero(self):
        one_to_ten = custom_range(1, 10)
        res = ""
        for num in one_to_ten:
            res += f"{num}\n"
        self.assertEqual(res, "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n")


if __name__ == '__main__':
    unittest.main()
