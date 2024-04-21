'''Many years ago, the country of Berland was inhabited by a small population of( n) individuals, each with their own savings. The government aimed to increase the number of wealthy individuals by implementing a series of reforms.

Each reform involved the government selecting a subset of individuals, collecting all their savings, and then redistributing the total equally among the selected individuals. The ultimate goal was to ensure that each individual had at least( x) burles to be considered wealthy.

Given the initial savings of each individual and the minimum wealth threshold( x), your task is to calculate the maximum possible number of wealthy individuals after the reforms, if any were implemented.

Input:

The first line contains a single integer( T) where, ( 1 <= T <= 1000) — the number of test cases.
For each test case, there are two lines: - The second line contains two integers( n) and( x) where, (1 <= n <= 10^5, 1 <= x <= 10^9) — representing the number of individuals and the minimum wealth threshold. - The third line contains( n) integers( a1, a2,...., an) where, ( 1 <= ai <= 10^9) — the initial savings of each individual.
Output:

Print( T) integers, one per test case, representing the maximum possible number of wealthy individuals after the reforms.
Constraints:

The total sum of( n) across all test cases does not exceed( 10^5).
Sample input:

1
1 2
13

Sample output:

1'''

class TestCase:
    def __init__(self, n, x, a):
        self.n = n
        self.x = x
        self.a = a

    def calculate_qualified_elements(self):
        a_sorted = sorted(self.a, reverse=True)
        p, q = 0, 0
        

        for savings in a_sorted:
            p+=savings
            if p >= self.x*(q+1):
                q+=1
            else:
                break

        
        return q


def process_test_cases():
    test_cases = int(input())
    results = []

    for _ in range(test_cases):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        

        case=TestCase(n,x,a)
        results.append(case.calculate_qualified_elements())

        

    return results


if __name__ == "__main__":
    results = process_test_cases()
    for result in results:
        print(result)
