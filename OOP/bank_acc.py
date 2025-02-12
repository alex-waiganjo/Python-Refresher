""" self._balance = balance # Protected attribute """
""" self.__balance = balance # Private attribute """

class BankAccount:
    MIN_BALANCE = 100 

    def __init__(self,owner,balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self,amount):
        if amount>0:
            self._balance += amount
            print(f'New Balance: {self._balance}')
        else:
            print("Amount must be More than Zero")

    @staticmethod # Specific for class domains
    def is_valid_interest(rate):
        return 0 <= rate <= 10
    
acc1 = BankAccount("Alex",600)
acc1.deposit(200)
print(acc1._balance)
print(acc1.is_valid_interest(22))