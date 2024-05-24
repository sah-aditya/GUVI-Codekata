'''You are developing a student management system for a B.Tech program. The system has a list of students, where each student is represented as a dictionary with the following keys: 'id', 'name', 'course', and 'grade'.

Write a Python function iterate_students(students: List[Dict[str, Union[str, int]]]) -> None that takes a list of students as input and prints each student's details using an iterator. The details should be printed in the following format: "Student ID: {id}, Name: {name}, Course: {course}, Grade: {grade}".

Constraints:

The id, name, course are strings and grade is an integer.
You can't install any external libraries.
Sample Input:

[ {"id": "BT202101", "name": "John Doe", "course": "Computer Science", "grade": "A"}, {"id": "BT202102", "name": "Jane Doe", "course": "Electrical Engineering", "grade": "B"}, ]

Sample Output:

Student ID: BT202101, Name: John Doe, Course: Computer Science, Grade: A
Student ID: BT202102, Name: Jane Doe, Course: Electrical Engineering, Grade: B

Explanation:

In the sample output, each line is the result of iterating over the list of students and printing each student’s details. This is done using a for loop, which in Python, creates an iterator for the list and iterates over it.

Iterators in Python are objects that can be iterated (or looped) over. An object is called iterable if we can get an iterator from it. Most built-in containers in Python like: list, tuple, string, etc. are iterables. The iter() function (which in turn calls the iter() method) returns an iterator from them.

In this case, the list of students is an iterable and the for loop creates an iterator that iterates over each student in the list. For each student, the student’s details are printed to the console. This demonstrates the use of iterators in Python to efficiently loop over an iterable object.'''



import sys
import json
from io import StringIO

def iterate_students(students):
    #..... YOUR CODE STARTS HERE .....
    
    for student in students:
        print(f"Student ID: {student['id']}, Name: {student['name']}, Course: {student['course']}, Grade: {student['grade']}")    
    
    #..... YOUR CODE ENDS HERE .....
    
def clean_input(value):
    value = value.strip() 
    if (len(value)):
        if ('}'  not in value):
            value += '}'
        
        if ('{' in value and '}' in value):
            return json.load(StringIO(value))
    return False
    
if __name__ == "__main__":
    students_list = ""

    for line in sys.stdin:
        line = line.strip()
        students_list += line
    
    students_list = list(map(clean_input, students_list.replace('[', '').replace(']', '').split('},')))
    students_list = list(filter(lambda student: isinstance(student, dict), students_list))

    iterate_students(students_list)