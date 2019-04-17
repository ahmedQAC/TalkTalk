class Customer:

    # Initializer / Instance Attributes
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            return"You cannot withdraw " + str(amount) + " as you only have " + str(self.balance) + " in your bank"
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

ahmed = Customer("ahmed", 100.0)

print(ahmed.withdraw(110))
print(ahmed.withdraw(23))
print("{} has {}.".format(
    ahmed.name, ahmed.balance))
