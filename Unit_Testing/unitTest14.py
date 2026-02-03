import unittest

class TestFloatValues(unittest.TestCase):

    def test_float_instances(self):
        float_values = {
            "a": 1.25,
            "b": 2.5,
            "c": 3.75,
            "d": 4.95
        }

        for name, value in float_values.items():
            with self.subTest(variable=name):
                self.assertIsInstance(value, float)

if __name__ == "__main__":
    unittest.main()
