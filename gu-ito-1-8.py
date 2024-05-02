'''Sanjay is a Stock Exchange Specialist. Any stocks that he buys, he has a capacity of for such greater price. He has created a algorithm to find the profit that can be obtained by trading certain stocks.

The machines will be generating a string, the string will be made up of integers from 0 to 9. Now each integer in this string will be a coded value of the profit. You have to multiply a digit N, with n-1,n-2,...till n-i>=1. Each digit in the string will be giving a profit of the particular amount thus obtained. Now summing up all the profits, it should be equal to the entire string considered as a integer input.

If they are equal, then the prediction was right, so print Right, if else print Wrong.

Input:

One single string input N, where N is the prediction by Victor

Input Constraints : 1<=length of N<=10^5

Output:

"Right" if the prediction is right and "Wrong" if the prediction is wrong

Sample input:

40583

Sample output:

Wrong'''



class NumberChecker:
    def __init__(self, n):
        self.n = n
        self.sum = 0
        self.temp = n

    def check_factorial_sum(self):
        while self.n:
            #..... YOUR CODE STARTS HERE .....

            digit=int(self.n%10)
            factorial=1
            for i in range(1,digit+1):
                factorial*=i
            self.sum+=factorial
            self.n//=10

            #..... YOUR CODE ENDS HERE .....            

        if self.sum == self.temp:
            return "Right"
        else:
            return "Wrong"


if __name__ == "__main__":
    n = int(input())
    number_checker = NumberChecker(n)
    result = number_checker.check_factorial_sum()
    print(result)
