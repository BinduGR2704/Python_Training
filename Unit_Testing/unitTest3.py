import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_string_a(self):
        self.assertEqual('a'*4, 'aaaa')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isUpper(self):
        self.assertTrue('FOO'.isupper())
        self.assertEqual('Foo'.isUpper())

    def test_strip(self):
        s = 'abcdefgh'
        self.assertEqual(s.strip('abcd'), 'abcd')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()