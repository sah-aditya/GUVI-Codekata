'''You are required to implement a program that calculates the service tax on every transaction for different types of accounts: Savings, Checking, and Demat. The service tax rates are 10%, 20%, and 5% respectively.

Create an abstract class Account with three private data member variables: accountNumber of type String, balance of type double, holderName of type String, and methods display() and an abstract method calculateServiceTax() with an argument of type int and return type as double.

Create the classes CheckingAccount, SavingsAccount, and DematAccount which extend the class Account. Use appropriate getters and setters for the above classes.

Input:

The input consists of a single line with the following information separated by space:

Account type (1 for Checking Account, 2 for Savings Account, 3 for Demat Account)
Holder's name
Account number
Current balance
Amount to be transferred
Output:

Output the remaining balance after the transaction.

Sample Input:

3 Rohan 562263 985.32 155

Sample Output:

Your remaining balance is Rs.822.57'''



from abc import ABC, abstractmethod

class Account(ABC):
    #..... YOUR CODE STARTS HERE .....

    def __init__(self,holder_name,account_number,balance):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance
        
    @abstractmethod
    
    def calculate_service_tax(self,transfer_amount):
        pass
    
    def display(self):
        print(f"Your remaining balance is Rs.{self.balance:.2f}")
        

    #..... YOUR CODE ENDS HERE .....

class CheckingAccount(Account):
    #..... YOUR CODE STARTS HERE .....

    def calculate_service_tax(self,ta):
        return ta*0.1


    #..... YOUR CODE ENDS HERE .....

class SavingsAccount(Account):
    #..... YOUR CODE STARTS HERE .....

    def calculate_service_tax(self,ta):
        return ta*0.1
    

    #..... YOUR CODE ENDS HERE .....

class DematAccount(Account):
    #..... YOUR CODE STARTS HERE .....

    def calculate_service_tax(self,ta):
        return ta*0.05

    #..... YOUR CODE ENDS HERE .....

def main():
    # Input
    account_type, holder_name, account_number, current_balance, transfer_amount = input().split()
    account_number = int(account_number)
    current_balance = float(current_balance)
    transfer_amount = float(transfer_amount)
    
    # Create account object based on account type
    if account_type == '1':
        account = CheckingAccount(holder_name, account_number, current_balance)
    elif account_type == '2':
        account = SavingsAccount(holder_name, account_number, current_balance)
    elif account_type == '3':
        account = DematAccount(holder_name, account_number, current_balance)
    else:
        print("Invalid input")
        return
    
    # Calculate service tax
    service_tax = account.calculate_service_tax(transfer_amount)
    
    # Update balance
    account.balance -= (transfer_amount + service_tax)
    
    # Display remaining balance
    account.display()

if __name__ == "__main__":
    main()
