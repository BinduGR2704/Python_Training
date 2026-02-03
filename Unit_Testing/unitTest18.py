import unittest

def is_even(number):
    return number % 2 == 0

class TestEvenOrOdd(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even(4))

    def test_odd_number(self):
        self.assertFalse(is_even(7))

    def test_zero(self):
        self.assertTrue(is_even(0))

if __name__ == '__main__':
    unittest.main()