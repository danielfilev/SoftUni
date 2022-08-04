import unittest


def is_prime(number):
    if number <= 1:
        return False

    result = True
    for i in range(2, number):
        if number % i == 0:
            result = False
            break
    return result


def get_primes(numbers):
    for number in numbers:
        if is_prime(number):
            yield number


# test zero


class Tests(unittest.TestCase):
    def test_zero(self):
        res = list(get_primes([2, 4, 3, 5, 6, 9, 1, 0]))
        self.assertEqual(res, [2, 3, 5])


if __name__ == '__main__':
    unittest.main()
