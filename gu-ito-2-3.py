'''In a school, there are several types of staff members: Teachers, Janitors, and Administrators. All staff members have a method get_salary() that returns their monthly salary. However, the salary is calculated differently for each type of staff member. For Teachers, the salary is a fixed amount of $3000. For Janitors, the salary is a fixed amount of $2000. For Administrators, the salary is a fixed amount of $4000.

Write a Python program that defines an abstract class StaffMember with the abstract method get_salary(). Then, define three classes Teacher, Janitor, and Administrator that inherit from the StaffMember class and implement the get_salary() method.

Sample Input:

Teacher().get_salary()
Janitor().get_salary()
Administrator().get_salary()

Sample Output:

3000
2000
4000

Explanation:

In this sample, the Teacher class returns a salary of $3000, the Janitor class returns a salary of $2000, and the Administrator class returns a salary of $4000. This demonstrates how each class correctly implements the get_salary() method from the StaffMember abstract base class.'''



from abc import ABC, abstractmethod

class StaffMember(ABC):
    @abstractmethod
    def get_salary(self):
        pass

    #..... YOUR CODE STARTS HERE .....
    
class Teacher(StaffMember):
    def get_salary(self):
        return 3000
        
class Janitor(StaffMember):
    def get_salary(self):
        return 2000
        
class Administrator(StaffMember):
    def get_salary(self):
        return 4000
    #..... YOUR CODE ENDS HERE .....
        
def call_func(cls, func):
    value = None
    cls_obj = None
    
    if (cls == "Teacher()"):
        cls_obj = Teacher()
    
    elif(cls == "Janitor()"):
        cls_obj = Janitor()
        
    elif(cls == "Administrator()"):
        cls_obj = Administrator()
    
    if (func == "get_salary()"):
        value = cls_obj.get_salary()
        
    return value

for _ in range(3):
    cls, func = input().strip().split(".")
    print(call_func(cls, func))