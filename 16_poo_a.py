# POO - parte 1
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance  # encapsulamiento

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Saldo insuficiente o monto no válido.")

    def check_balance(self):
        return f"Saldo actual: {self.__balance}"


account = BankAccount("John", 1000)  # abstracción
account.deposit(5000)
account.withdraw(2000)
print(account.check_balance())
