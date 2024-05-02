'''The Felicity Committee assigns a power value to each superhero, and the Avengers aim to maximize their team's average power through strategic operations.

Initially, the Avengers have n superheroes with powers a1, a2, ..., an. In each operation, they can either remove a superhero (if there are at least two) or increase a superhero's power by 1.

They are allowed a maximum of m operations, with each superhero limited to k power increases. Can you assist the Avengers in maximizing their team's average power

Input:

The first line contains three integers n, k and m (1≤n≤105, 1≤k≤105, 1≤m≤107) — the number of superheroes, the maximum number of times you can increase power of a particular superhero, and the total maximum number of operations.

The second line contains n integers a1,a2,…,an (1≤ai≤106) — the initial powers of the superheroes in the cast of avengers.

Output:

Output a single number — the maximum final average power.

Your answer is considered correct if its absolute or relative error does not exceed 10−6.

Formally, let your answer be a, and the jury's answer be b. Your answer is accepted if and only if |a−b|max(1,|b|)≤10−6.

Sample input:

2 4 6
4 7

Sample output:

11.0'''

n, k, m = map(int, input().split())
a = list(map(int, input().split()))

#..... YOUR CODE STARTS HERE .....

a.sort()
ans=sum(a)
r=0
for i in range(n):
    if i<=m:
        r=int(max(r,(ans+min(k*(n-i),m-i))/(n-i)))
    ans-=a[i]
    
print(r)

#..... YOUR CODE ENDS HERE .....