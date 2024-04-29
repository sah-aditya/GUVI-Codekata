'''You are required to implement a notification system for banks that notifies customers through SMS, Email, and monthly e-statement. The system consists of an interface Notification with three methods:

notificationBySms()
notificationByEmail()
notificationByCourier()
Implement two classes, Icici and Hdfc, which implement the Notification interface. Additionally, create a BankFactory class with two methods:

public Icici getIcici() (returns an object for Icici)
public Hdfc getHdfc() (returns an object for Hdfc)
The main class should get input from the user and display the appropriate notification based on the bank and notification type selected.

Input:

The first integer corresponds to the name of the bank, and the next integer corresponds to the type of notification. If there is no valid input, display 'Invalid input'.

Output:

Output the notification message based on the bank and notification type selected.

Sample Input:

1 1

Sample Output:

ICICI - Notification By SMS'''



# Notification interface
class Notification:
    def notificationBySms(self):
        pass
    
    def notificationByEmail(self):
        pass
    
    def notificationByCourier(self):
        pass

# Icici class implementing Notification interface
class Icici(Notification):
    #..... YOUR CODE STARTS HERE .....

    def notificationBySms(self):
        return "ICICI - Notification By SMS"

    def notificationByEmail(self):
        return "ICIcI - Notification By Email"
    
    def notificationByCourier(self):
        return "ICICI - Notification By Courier"
    #..... YOUR CODE ENDS HERE .....

# Hdfc class implementing Notification interface
class Hdfc(Notification):
    #..... YOUR CODE STARTS HERE .....
    
    def notificationBySms(self):
        return "HDFC - Notification By SMS"
    
    def notificationByEmail(self):
        return "HDFC - Notification By Email"
    
    def notificationByCourier(self):
        return "HDFC - Notification By Courier"
        

    #..... YOUR CODE ENDS HERE .....

# BankFactory class
class BankFactory:
    def getIcici(self):
        return Icici()
    
    def getHdfc(self):
        return Hdfc()

def main():
    bank, notification = map(int, input().split())
    bank_factory = BankFactory()
    
    if bank == 1:
        bank_obj = bank_factory.getIcici()
    elif bank == 2:
        bank_obj = bank_factory.getHdfc()
    else:
        print("Invalid input")
        return
    
    if notification == 1:
        print(bank_obj.notificationBySms())
    elif notification == 2:
        print(bank_obj.notificationByEmail())
    elif notification == 3:
        print(bank_obj.notificationByCourier())
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
