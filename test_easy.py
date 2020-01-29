import unittest
from scripts import FizzBuzz


class TestExceptions(unittest.TestCase):
    def test_not_integer(self):
        self.assertRaises(TypeError, FizzBuzz.fizzbuzz, "5")

    def test_value_not_in_range(self):
        self.assertRaises(ValueError, FizzBuzz.fizzbuzz, 1005)
        self.assertRaises(ValueError, FizzBuzz.fizzbuzz, -10)
        self.assertRaises(ValueError, FizzBuzz.fizzbuzz, 0)


class TestResult(unittest.TestCase):
    def test_divisible_by_3(self):
        self.assertEqual(FizzBuzz.fizzbuzz(3), ['1', '2', 'Fizz'])
        # test value=9 -> 8 position on list
        self.assertEqual(FizzBuzz.fizzbuzz(20)[8], 'Fizz')

    def test_divisible_by_5(self):
        self.assertEqual(FizzBuzz.fizzbuzz(5), ['1', '2', 'Fizz', '4', 'Buzz'])
        # test value=10 -> 9 position on list
        self.assertEqual(FizzBuzz.fizzbuzz(20)[9], 'Buzz')

    def test_divisible_by_3_and_5(self):
        # test value=15 -> 14 position on list
        self.assertEqual(FizzBuzz.fizzbuzz(20)[14], 'FizzBuzz')
        # test value=30 -> 29 position on list
        self.assertEqual(FizzBuzz.fizzbuzz(50)[29], 'FizzBuzz')

    def test_not_divisible(self):
        # test value=29 -> 28 position on list
        self.assertEqual(FizzBuzz.fizzbuzz(50)[28], '29')


if __name__ == '__main__':
    unittest.main()
