class Account:

    def __init__(self, name: String, balance: Double, ownerType: String):

        self.name = name
        self.accountBalance = balance
        self.ownerType = ownerType

    def _increaseBalance(self, amount: Double):

        self.accountBalance += amount

    def _decreaseBalance(self, amount: Double):

        self.accountBalance -= amount

    def _returnBalance(self):

        print("Account Balance: " + str(self.accountBalance))