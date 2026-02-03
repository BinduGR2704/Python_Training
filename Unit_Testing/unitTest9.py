import unittest

class Widget:
    def __init__(self):
        self.width = 50
        self.height = 50

    def resize(self, width, height):
        self.width = width
        self.height = height

class WidgetTestCase(unittest.TestCase):

    def test_default_widget_size(self):
        widget = Widget()
        self.assertEqual(widget.width, 50)
        self.assertEqual(widget.height, 50)

    def test_widget_resize(self):
        widget = Widget()
        widget.size(100, 200)

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(WidgetTestCase('test_default_widget_size'))
    test_suite.addTest(WidgetTestCase('test_widget_resize'))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())