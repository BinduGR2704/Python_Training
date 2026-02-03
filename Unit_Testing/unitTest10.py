from ctypes.macholib import dylib
import unittest

class MyTestCase(unittest.TestCase):

    @unittest.skip("Demonstarting skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skip(mylib.__version__<(1,3),
                   "not supported in this library version")
    def test_format(self):
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("External Resouce not Available")

@unittest.skip("Showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass

class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")

def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip({"skipped function"})

# ERROR