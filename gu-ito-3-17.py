'''You are developing a student management system for a B.Tech program. The system has a function get_student_grade(student_id: str) -> str that takes a student ID as input and returns the grade of that student.

The program has the following students enrolled:

Student ID: "BT202101", Grade: "A"
Student ID: "BT202102", Grade: "B"
However, not all students are enrolled in the program at all times. If a student is not enrolled, the function should raise a StudentNotFoundError with a message "Student not found".

Write a Python function proxy_get_student_grade(student_id: str) -> str that acts as a proxy to the get_student_grade(student_id: str) -> str function. The proxy function should handle any StudentNotFoundError that might be raised and return a default grade 'N/A' if the student is not found.

Constraints:

Student ID is a string.
You can't install any external libraries.
Sample Input:

BT202101

Sample Output:

A

Explanation:

In the sample outputs, the first grade is returned when the student is found in the program. The grade of the student is displayed in the output. This is done by catching the grade returned by the get_student_grade function in a try block.

This demonstrates how proxy functions work in Python - a proxy function acts as an interface to another function and can add additional behavior (like error handling) without changing the original function’s code. In this case, the proxy function adds error handling to the get_student_grade function, allowing it to return a default grade when a student is not found. This is a key aspect of robust software design.

In Python, functions are first-class objects, which means they can be passed around and used as arguments just like any other object (string, int, float, list, etc.). Higher-order functions are a kind of function that takes one or more functions as arguments, returns a function, or both. This property allows us to create proxy functions like proxy_get_student_grade.'''



class StudentNotFoundError(Exception):
    pass

def get_student_grade(student_id):
    
    students = {
        "BT202101": "A",
        "BT202102": "B",
    }
    if student_id in students:
        return students[student_id]
    else:
        raise StudentNotFoundError("Student not found")

def proxy_get_student_grade(student_id):
    #..... YOUR CODE STARTS HERE .....
    
    try:
        return get_student_grade(student_id)
    except StudentNotFoundError:
        return 'N/A'    
    
    #..... YOUR CODE ENDS HERE .....
        
student_id = input()

print(proxy_get_student_grade(student_id))

