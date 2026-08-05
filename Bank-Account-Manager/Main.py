from Account import Account
from BusinessAccount import BusinessAccount

myBusinessAccount = BusinessAccount("Jathon", 100.00, "business")
myBusinessAccount._returnBalance()
myBusinessAccount._increaseBalance(200.00)
myBusinessAccount._returnBalance()