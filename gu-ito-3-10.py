'''You are managing a bank's software system. Every time a customer makes a transaction, the transaction amount is recorded. You want to create a function that calculates the square root of the transaction amount. Write a Python function transaction_sqrt(transaction_amount) that takes a transaction amount and returns the square root of the transaction amount. Use the sqrt function from the built-in Python math module to calculate the square root.

Input:

transaction_amount: a float representing the transaction amount.
Output:

The function should return a float representing the square root of the transaction amount.
Sample Input:

100.0

Sample Output:

10.0

Explanation :

The sqrt function from the math module calculates the square root of a number. In the context of managing a bank's software system, this can be useful to perform various calculations related to the transaction amount.'''


from math import sqrt

def transaction_sqrt(transaction_amount):
    #..... YOUR CODE STARTS HERE .....

    return sqrt(transaction_amount)

    #..... YOUR CODE ENDS HERE .....

transaction_amount = float(input())
result = transaction_sqrt(transaction_amount)
print(result)