import unittest

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount

class TestDemo(unittest.TestCase):

    def setUp(self):
        self.a = 10
        self.b = 5

    def test_add(self):
        self.assertEqual(self.a + self.b, 15)
    
    def test_exception(self):
        with self.assertRaises(ValueError):
            withdraw(100,200)

    def tearDown(self):
        pass

class Bank:
    def deposit(self, amt):
        return amt

class TestBank(unittest.TestCase):
    def test_deposit(self):
        bank = Bank()
        self.assertEqual(bank.deposit(1000), 100)

@unittest.skip("Feature not raedy")

def test_future(self):
    pass

if __name__ == "__main__":
    unittest.main()