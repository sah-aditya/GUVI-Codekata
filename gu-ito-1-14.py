class FactorFinder:
    def __init__(self, n):
        self.n = n

    def find_factors(self):
        def backtrack(remaining, start, path, result):
            #..... YOUR CODE STARTS HERE .....

            if remaining == 1:
                if len(path) > 1:
                    result.append(path[ : ])
                else:
                    result.append([1, path[0]])
                return
            for i in range(start, remaining + 1):
                if remaining % i ==0:
                    path.append(i)
                    backtrack(remaining // i,i,path,result)
                    path.pop()
        result = []
        backtrack(self.n,2,[],result)
        return result

            #..... YOUR CODE ENDS HERE .....

        result = []
        backtrack(self.n, 2, [], result)
        return result

if __name__ == '__main__':
    n = int(input())
    factor_finder = FactorFinder(n)
    print(factor_finder.find_factors())