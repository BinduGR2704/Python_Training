def square(n):
    return  n*n

import unittest

class TestSquare(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(4), 16)

unittest.main()