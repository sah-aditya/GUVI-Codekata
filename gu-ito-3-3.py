'''You are a college professor and you have the scores of your students in a list. You want to find the total score of all students. Write a Python function total_score(scores) that takes a list of scores and returns the total score. Use the reduce function to calculate the total score.

Input:

scores: a list of integers representing the scores of the students.
Output:

The function should return an integer representing the total score of all students.
Sample Input:

[85, 90, 78, 92]

Sample Output:

345

Explanation:

The reduce function applies a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single output. In this case, it takes two scores at a time and adds them, continuing this process until all scores have been added together. This demonstrates how the reduce function can be used to reduce a list to a single result. In the context of grading students in a college, this can be useful to calculate the total score of all students.

'''


import json
from io import StringIO
from functools import reduce

def total_score(scores):
    #..... YOUR CODE STARTS HERE .....
    
    return reduce(lambda x, y: x + y, scores)    
    
    #..... YOUR CODE ENDS HERE .....
    
def clean_input(value):
    return json.load(StringIO(value))
    
if __name__ == "__main__":
    scores = clean_input(input().strip())
    
    print(total_score(scores))