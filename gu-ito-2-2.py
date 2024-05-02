'''In a B.Tech course, there are several subjects, each with a different method of evaluation. Some subjects have lab work, some have project work, and some have only theory exams. Define an interface Subject with the methods has_lab(), has_project(), and get_theory_marks(). Then, define three classes LabSubject, ProjectSubject, and TheorySubject that implement this interface according to the following rules:

LabSubject returns True for has_lab(), False for has_project(), and a fixed score of 70 for get_theory_marks().
ProjectSubject returns False for has_lab(), True for has_project(), and a fixed score of 80 for get_theory_marks().
TheorySubject returns False for both has_lab() and has_project(), and a fixed score of 90 for get_theory_marks().
Sample Input:

LabSubject().has_lab()
ProjectSubject().has_project()
TheorySubject().get_theory_marks()

Sample Output:

True
True
90

Explanation:

The LabSubject class returns True for has_lab(), indicating that the subject has lab work. The ProjectSubject class returns True for has_project(), indicating that the subject has project work. The TheorySubject class returns 90 for get_theory_marks(), indicating that the theory marks for the subject are 90.'''




from abc import ABC, abstractmethod

class Subject(ABC):
    #..... YOUR CODE STARTS HERE .....
    
        @abstractmethod
        def has_lab(self):
            pass
        @abstractmethod
        def has_project(self):
            pass
        @abstractmethod
        def get_theory_marks(self):
            pass
    
    #..... YOUR CODE ENDS HERE .....

class LabSubject(Subject):
    def has_lab(self):
        #..... YOUR CODE STARTS HERE .....
    
        return True
    
        #..... YOUR CODE ENDS HERE .....
    
    def has_project(self):
        #..... YOUR CODE STARTS HERE .....
    
        return False
    
        #..... YOUR CODE ENDS HERE .....
    
    def get_theory_marks(self):
        #..... YOUR CODE STARTS HERE .....
    
        return 70
    
        #..... YOUR CODE ENDS HERE .....

class ProjectSubject(Subject):
    def has_lab(self):
        #..... YOUR CODE STARTS HERE .....
    
        return False
    
        #..... YOUR CODE ENDS HERE .....
    
    def has_project(self):
        #..... YOUR CODE STARTS HERE .....
    
        return True
    
        #..... YOUR CODE ENDS HERE .....
    
    def get_theory_marks(self):
        #..... YOUR CODE STARTS HERE .....
    
        return 80
    
        #..... YOUR CODE ENDS HERE .....

class TheorySubject(Subject):
    def has_lab(self):
        #..... YOUR CODE STARTS HERE .....
    
        return False
    
        #..... YOUR CODE ENDS HERE .....
    
    def has_project(self):
        #..... YOUR CODE STARTS HERE .....
    
        return False
    
        #..... YOUR CODE ENDS HERE .....
    
    def get_theory_marks(self):
        #..... YOUR CODE STARTS HERE .....
    
        return 90
    
        #..... YOUR CODE ENDS HERE .....
        
def call_func(cls, func):
    value = None
    
    if (func == "has_lab()"):
        value = cls.has_lab()
        
    elif(func == "has_project()"):
        value = cls.has_project()
        
    elif(func == "get_theory_marks()"):
        value = cls.get_theory_marks()
        
    return value

# Getting input from the user
lab_class, lab_func = input().strip().split(".")
project_class, project_func = input().strip().split(".")
theory_class, theory_func = input().strip().split(".")

if (lab_class == 'LabSubject()'):
    lab = LabSubject()
    print(call_func(lab, lab_func))

if(project_class == "ProjectSubject()"):
    project = ProjectSubject()
    print(call_func(project, project_func))
    
if(theory_class == "TheorySubject()"):
    theory = TheorySubject()
    print(call_func(theory, theory_func))