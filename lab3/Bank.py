class BankAccount():
    def __init__(self,owner="Unknown",balance=0):
        self.owner=owner
        self.balance=balance
    
    def balanceRN(self):
        self.owner=(input("Enter your name:"))
        print(f"Welcome {self.owner}! Your bank balance {self.balance} KZT")

    def deposit(self):
        self.balance += int(input("Enter the amount to deposit:"))
        print(f"Your bank balance after deposit {self.balance} KZT")

    def withdraw(self):
        sum=int(input("Enter the amount to withdraw:"))
        if sum < self.balance:
            self.balance-=sum
            print(f"Your bank balance after withdraw {self.balance} KZT")
        else:
            print("You have insufficient funds to complete this withdrawal:(")
obj=BankAccount()
obj.balanceRN()
obj.deposit()
obj.withdraw()