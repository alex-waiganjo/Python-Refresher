class BankAcc:

    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return f'Current Balance: KSH {self._balance}'

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        print(f'KSH {amount} Sucessfully Deposited!')

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount >= self._balance:
            raise ValueError("Insufficient Funds!")
        self._balance -= amount
        print(f'KSH {amount} Sucessfully Withdrawn!')


acc = BankAcc()
acc.deposit(100)
print(acc.balance)
acc.withdraw(50)
print(acc.balance)
