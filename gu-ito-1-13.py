'''Sanjay is a student who hates maths. But he was a good programmer. There was a sum in second chapter which was given to him as a homework.Help him to finish his homework. You are given with a number n. You have to find the sum of numbers from 1 to n and subtract all the 2nd values from the sum. Help him to finish the exercise in the second chapter. Write a program to finish the maths homework.

Input:

The first line contains an integer t, the total number of testcases.
The next t lines contain an integer n.
Input Constraints:
1<=t<=100
1<=n<=10^9

Output:

Print t lines of integer values

Sample input:

2
4
1000000000

Sample output:

-4
499999998352516354

'''



import math

class NumberCalculator:
    #..... YOUR CODE STARTS HERE .....

    def __init__(self):
        pass
    
    def calculate_result(self,n):
        return n*(n+1)//2 - 2*(2**(int(math.log2(n))+1)-1)

    #..... YOUR CODE ENDS HERE .....

if __name__ == "__main__":
    number_calculator = NumberCalculator()
    test_cases = int(input())

    for i in range(test_cases):
        n = int(input())
        result = number_calculator.calculate_result(n)
        print(result)
