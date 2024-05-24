'''You are working on a Python project that involves performing complex mathematical operations. For this project, you need to calculate the square root of a list of transaction amounts. So write a Python function calculate_sqrt(transaction_amounts) that takes a list of transaction amounts and returns a list of their square roots.

Sample Input:

[100.0, 200.0, 300.0, 400.0]

Sample Output:

[10.0, 14.142135623730951, 17.320508075688775, 20.0]

Explanation:

The calculate_sqrt function uses the sqrt function from the math module to calculate the square root of each transaction amount. The square root of a number is a value that, when multiplied by itself, gives the original number. In this case, we're calculating the square root of each transaction amount in the list.'''



import math

def calculate_sqrt(transaction_amounts):
   #..... YOUR CODE STARTS HERE .....
    
   return [math.sqrt(amount) for amount in transaction_amounts]    
    
    #..... YOUR CODE ENDS HERE .....
   
if __name__ == "__main__":
    transaction_amounts = eval(input().strip())
    print(calculate_sqrt(transaction_amounts))