'''You are a college professor and you have the scores of your students in a list. You want to find out which students have passed the course. A student passes the course if they score 60 or more. Write a Python function passed_students(scores) that takes a list of scores and returns a list of scores that are 60 or more. Use the filter function to filter out the passing scores.

Input:

scores: a list of integers representing the scores of the students.
Output:

The function should return a list of integers representing the scores of the students who have passed.
Sample Input:

[55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

Sample Output:

[60, 65, 70, 75, 80, 85, 90, 95, 100]

Explanation:

The filter function applies a function to every item in the scores list and returns a new list with the items for which the function returns True. In this case, the function is a lambda function that checks if a score is 60 or more. This demonstrates how the filter function can be used to filter items in a list based on a condition. In the context of grading students in a college, this can be useful to find out which students have passed the course based on their scores.

'''


import json
from io import StringIO

def passed_students(scores):
    #..... YOUR CODE STARTS HERE .....
    
    return list(filter(lambda x: x >= 60, scores))    
    
    #..... YOUR CODE ENDS HERE .....

if __name__ == "__main__":
    scores = json.load(StringIO(input().strip()))
    passed_students = passed_students(scores)
    
    print(passed_students)
       