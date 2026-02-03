import unittest

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = widget("The widget")
        self.assertEqual(widget.size(), (50,50))

if __name__ == '__main__':
    unittest.main()