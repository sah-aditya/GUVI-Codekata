'''You are a college professor and you have two lists: one with the names of your students and another with their corresponding scores. You want to associate each student with their score. Write a Python function associate_students(names, scores) that takes a list of names and a list of scores and returns a list of tuples where each tuple contains a name and the corresponding score. Use the zip function to associate the names with the scores.

Input:

names: a list of strings representing the names of the students.
scores: a list of integers representing the scores of the students.
Output:

The function should return a list of tuples where each tuple contains a name and the corresponding score.
Sample Input:

['Alice', 'Bob', 'Charlie', 'Dave'], [85, 90, 78, 92]

Sample Output:

[('Alice', 85), ('Bob', 90), ('Charlie', 78), ('Dave', 92)]

Explanation:

The zip function takes two or more iterable objects (like lists or strings), aggregates them in a tuple, and returns it. In this case, it takes a name from the names list and a score from the scores list and puts them together in a tuple. This demonstrates how the zip function can be used to combine two lists into a list of tuples. In the context of grading students in a college, this can be useful to associate each student with their score.'''



import re

def associate_students(names, scores):
    #..... YOUR CODE STARTS HERE .....
    
    return list(zip(names, scores))    
    
    #..... YOUR CODE ENDS HERE .....
    
def clean_input(value):
    value = value.strip()
    return re.sub(r'[^A-Z0-9a-z,]', '', value).split(',')
    
if __name__ == "__main__":
   names, scores = list(map(clean_input, input().strip().split('],')))
   scores = list(map(int, scores))
   print(associate_students(names, scores))