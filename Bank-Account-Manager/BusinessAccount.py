from Account import Account

class BusinessAccount(Account):

    def __init__(self, name: String, balance: Double, ownerType: String):

        super().__init__(name, balance, ownerType)
        self.EIN = ""

    def setEIN(self, EIN: String):

        self.EIN = EIN