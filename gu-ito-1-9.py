'''Gordon the wizard possesses an extraordinary collection of magical stones. Each stone has a unique weight ranging from 1 to n.

Gordon's peculiar ability allows him to fuse two stones together, resulting in a new stone with a weight equal to the sum of the weights of the two original stones. However, the two original stones vanish after fusion.

Gordon's ultimate goal is to maximize the number of stones that have the same weight. While it's not mandatory to make all stones uniform in weight, he desires to have as many stones of equal weight as possible.

Given the number of stones in Gordon's collection, determine how many stones of equal weight he can create using his magical fusion process.

Input:

The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases.

The following t lines each contain a single integer n (1 ≤ n ≤ 10^9), representing the number of stones in Gordon's collection.

Output:

For each test case, print a single integer, the maximum number of stones with equal weight that Gordon can create.

Sample input:

1
10

Sample output:

5'''


class StoneCalculator:
    def __init__(self, t):
        self.t = t

    def calculate_max_stones(self, n):
        #..... YOUR CODE STARTS HERE .....

        return n//2

        #..... YOUR CODE ENDS HERE .....
if __name__ == "__main__":
    t = int(input())
    stone_calculator = StoneCalculator(t)

    for i in range(t):
        n = int(input())
        result = stone_calculator.calculate_max_stones(n)
        print(result)
