# POO - parte 2

# clase abstracta

from abc import ABC, abstractmethod
from re import A


class BankAccount(ABC):  # heredo de ABC y se convierte en clase abstracta
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance

    def _get_balance(self):
        return self.__balance

    def _set_balance(self, new_balance):
        self.__balance = new_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    @abstractmethod
    def withdraw(self, amount):
        pass  # polimorfismo

    def check_balance(self):
        return f"Saldo actual: {self.__balance}"


# implementacion de la clase abstracta


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        penalty = amount * 0.05
        total = amount + penalty

        if total <= self._get_balance():
            self._set_balance(self._get_balance() - total)
        else:
            print("Fondos insuficientes en la cuenta de ahorro.")


class PayrollAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self._get_balance():
            self._set_balance(self._get_balance() - amount)
        else:
            print("Fondos insuficientes en la cuenta sueldo.")


saving = SavingsAccount("John", 1000)
payroll = PayrollAccount("John", 1000)

saving.withdraw(100)
payroll.withdraw(100)

print("Cuenta de ahorro:", saving.check_balance())
print("Cuenta sueldo:", payroll.check_balance())
