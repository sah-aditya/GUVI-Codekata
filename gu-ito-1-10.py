'''Sanjay wants to become the largest of bears, or at least to become larger than his brother Midhun.

Right now, Sanjay and Midhun weigh a and b respectively. It's guaranteed that Sanjay's weight is smaller than or equal to his brother's weight.

Sanjay eats a lot and his weight is tripled after every year, while Midhun's weight is doubled after every year.

After how many full years will Sanjay become strictly larger (strictly heavier) than Midhun?

Input:

The only line of the input contains two integers a and b (1 ≤ a ≤ b ≤ 10) — the weight of Sanjay and the weight of Midhun respectively.

Output:

Print one integer, denoting the integer number of years after which Sanjay will become strictly larger than Midhun.

Sample input:

4 7

Sample output:

2'''



class Calculation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def find_iteration(self):
        #..... YOUR CODE STARTS HERE .....

        if self.x>self.y:
            return 1
        years=0
        while self.x<=self.y:
            self.x*=3
            self.y*=2
            years+=1
        return years

        #..... YOUR CODE ENDS HERE .....

if __name__ == "__main__":
    x, y = map(int, input().split())
    calculation = Calculation(x, y)
    result = calculation.find_iteration()
    if result is not None:
        print(result)