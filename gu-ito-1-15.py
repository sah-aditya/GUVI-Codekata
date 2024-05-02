'''Mani, renowned for his cryptographic prowess, has developed a novel encryption technique for transmitting positive integers securely to his acquaintances. In his method, Mani selects three secret integers — a, b, and c — from a specified range determined by lower and upper bounds, denoted as l and r. Subsequently, he employs the formula m = n * a + b - c to generate the encrypted value of the integer n.

However, an adversary has managed to intercept the parameters l, r, and m, posing a challenge to decrypt the original values of a, b, and c. The task at hand is to decipher any valid combination of a, b, and c that adheres to the following criteria:

The values of a, b, and c must be integers.
They must fall within the inclusive range [l, r].
There exists at least one positive integer n such that n * a + b - c equals the intercepted value m.
The input comprises multiple test cases, each presenting the intercepted values of l, r, and m. It is assured that at least one feasible solution exists, and any valid combination of a, b, and c may be outputted if multiple solutions are available.
Sample input:

20
10 12 43
25 49 1
5 7 39
8 9 44
16 17 50
30 40 975
601 801 1000
100 102 909
599 799 1000
503 997 9
194 383 5
90000 100000 709999
75000 100000 124999
375000 499999 625001
375000 500000 624999
300000 400000 499999
250000 500000 1
70000 80000 2272770257
70000 80000 9999953344
90000 100000 9999955820

Sample output:

11 11 12
25 25 49
5 6 7
9 8 9
17 16 17
35 35 40
800 801 601
101 102 102
599 601 799
503 503 997
194 194 383
100000 100000 90001
99999 100000 75000
375000 375000 499999
499999 500000 375000
399999 400000 300000
250000 250001 500000
70007 73002 80000
70009 80000 72198
90003 92499 100000'''


import sys

def get_ints(): 
    return map(int, sys.stdin.readline().split())

for _ in range(int(input())):
    lst = list(get_ints())
    
    #..... YOUR CODE STARTS HERE .....
    
    
    l,r,m=lst[0],lst[1],lst[2]
    for i in range(l,r+1):
        x1=m%i
        x2=i-(m%i)
        if i<=m and x1<=(r-l):
            a=i
            b=r
            c=r-x1
            i=r+2
            break
        elif x2<=(r-l):
            a=i
            b=r-x2
            c=r
            i=r+2
            break
    print(a,end=" ")
    print(b,end=" ")
    print(c)
            
    #..... YOUR CODE ENDS HERE .....