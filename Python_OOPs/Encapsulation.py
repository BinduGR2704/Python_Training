class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self):
        print("Balance : rs", self.balance)

    def __update_balance(self, amount):  #This method cannot be called outside the class as it is private
        self.balance += amount

    def deposite(self, amount):
        if amount > 0:
            self.__update_balance(amount)
            self._show_balance()
        else:
            print("Invalid deposite amount")

account = BankAccount()
account.deposite(240)