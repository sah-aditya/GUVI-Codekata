'''You are a college professor and you have the scores of your students in a list. You want to grade the students based on their scores. Write a Python function grade_students(scores) that takes a list of scores and returns a list of grades. Use the map function to apply the grading scheme to all scores.

The grading scheme is as follows:

Score >= 90: 'A'
80 <= Score < 90: 'B'
70 <= Score < 80: 'C'
60 <= Score < 70: 'D'
Score < 60: 'F'
Input:

scores: a list of integers representing the scores of the students.
Output:

The function should return a list of strings representing the grades of the students.
Sample Input:

[95,55]

Sample Output:

['A','F']

Explanation:

The map function applies the get_grade function to every item in the scores list. The get_grade function takes a score and returns a grade based on the grading scheme. This demonstrates how the map function can be used to apply a function to every item in a list. In the context of grading students in a college, this can be useful to grade all students based on their scores.'''



import json
from io import StringIO

def grade_students(scores):
    def get_grade(score):
        #..... YOUR CODE STARTS HERE .....
    
        if score >= 90:
            return 'A'
        elif 80 <= score < 90:
            return 'B'
        elif 70 <= score < 80:
            return 'C'
        elif 60 <= score < 70:
            return 'D'
        else:
            return 'F'    
    
        #..... YOUR CODE ENDS HERE .....
        
    return list(map(get_grade, scores))

if __name__ == "__main__":
    scores = json.load(StringIO(input().strip()))
    grades = grade_students(scores)
    
    print(grades)