class Banks:
    def calculateCreditScore(self):
        pass

class RBI(Banks):
    CREDIT = 0.10
    
    def __init__(self, accountNumber, creditScore, holderName):
        self.__accountNumber = accountNumber
        self.__creditScore = creditScore
        self.__holderName = holderName
    
    def calculateCreditScore(self, amount):
        #..... YOUR CODE STARTS HERE .....
        credit_gained = amount * self.CREDIT
        self.__creditScore += credit_gained
        return credit_gained


        #..... YOUR CODE ENDS HERE .....
    
    def display(self):
        print("Bank type: RBI")
        print("Account Number:", self.__accountNumber)
        print("Credit score:", "{:.2f}".format(self.__creditScore))
        
class ICICI(RBI):
    def __init__(self, accountNumber, creditScore, holderName):
        super().__init__(accountNumber, creditScore, holderName)
    
    def calculateCreditScore(self, amount):
        #..... YOUR CODE STARTS HERE .....
        
        credit_gained = super().calculateCreditScore(amount)
        print("Hi,", self._RBI__holderName, "You have gained {:.2f} credit score for the payment of {:.1f} Your Total Credit Score is {:.2f}".format(credit_gained, amount, self._RBI__creditScore))

        #..... YOUR CODE ENDS HERE .....

class HDFC(RBI):
    def __init__(self, accountNumber, creditScore, holderName):
        super().__init__(accountNumber, creditScore, holderName)
    
    def calculateCreditScore(self, amount):
        #..... YOUR CODE STARTS HERE .....
        
        credit_gained = super().calculateCreditScore(amount)
        print("Hi,", self._RBI__holderName, "You have gained {:.2f} credit score for the payment of {:.1f} Your Total Credit Score is {:.2f}".format(credit_gained, amount, self._RBI__creditScore))

        #..... YOUR CODE ENDS HERE .....

class Main:
    def __init__(self):
        input_data = input().split()
        bank = int(input_data[0])
        holderName = input_data[1]
        accountNumber = input_data[2]
        previousCreditScore = float(input_data[3])
        amount = float(input_data[4])
        
        if bank == 1:
            icici = ICICI(accountNumber, previousCreditScore, holderName)
            icici.calculateCreditScore(amount)
        elif bank == 2:
            hdfc = HDFC(accountNumber, previousCreditScore, holderName)
            hdfc.calculateCreditScore(amount)
        else:
            print("Invalid bank selection")

# Main program execution
if __name__ == "__main__":
    Main()