#this file contains the solution to the problem of gu introduction to oops unit 1 - question 1.
'''Mani finds himself in a queue of( n) people but is uncertain about his exact position. However, he's confident that there are at least( a) people in front of him and at most( b) people behind him. Mani seeks to determine the number of different positions he could occupy in the queue.

Input:

The input consists of a single line containing three integers:( n),( a), and( b) (( 0≤a,b<n≤100)). These represent the total number of people in the queue, the minimum number of people in front of Mani, and the maximum number of people behind Mani, respectively.
Output:

Print a single integer, the number of possible positions Mani could occupy in the queue.
Constraints:

The queue contains between 1 and 100 people.
Mani is certain there are at least 0 people in front of him and at most( n-1) people behind him.
Sample input:

5 2 3

Sample output:

3'''

n, a, b = map(int, input().split())
c= n-max(a+1, n-b)+1.
print(c)
