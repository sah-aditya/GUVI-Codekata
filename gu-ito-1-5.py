'''On Earth, each plane has a special affinity for another plane. Given a group of n planes, numbered from 1 to n, where plane i likes plane fi, we aim to determine if any love triangle exists.

Input:

The first line contains a single integer n (2 ≤ n ≤ 5000) — representing the number of planes.

The second line contains n integers f1, f2, ..., fn (1 ≤ fi ≤ n, fi ≠ i), indicating that the i-th plane is fond of plane fi.

Output:

Output "YES" if there exists a love triangle among the planes. Otherwise, output "NO".

Sample input:

5
5 5 5 5 1

Sample output:

NO'''


class CycleChecker:
    def __init__(self, f):
        self.f = f
        self.n = len(f)

    def check_cycle(self):
        
        for i in range(self.n):
            a=i+1
            b=self.f[a-1]
            c=self.f[b-1]
            if self.f[c-1]==a:
                return "YES"
            else:
                return "NO"

             
 
if __name__ == "__main__":
    n = int(input())
    f = list(map(int, input().split()))

    

    cycle_checker=CycleChecker(f)
    result=cycle_checker.check_cycle()
    print(result)
    

    
