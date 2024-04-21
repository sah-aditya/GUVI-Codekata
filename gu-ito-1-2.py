'''Lucas, a university student, is working on a project where he needs to process a set of student records. He is given a list of students where each record contains the student's name and marks in three subjects: Math, Physics, Biology. Each subject's mark is within the range 0-100. He needs to return the name of the student with the highest average score.

If there is more than one student who has the highest average score, Lucas needs to return the first student in the list.

Input:

The first line contains an integer 'n' (1 <= n <= 1000) - representing the number of students.
The 'n' following lines each contain a string and three space-separated integers.
Output:

Print the name of the student who has the highest average score.
Sample Input:

5
John 85 90 82
Alice 90 91 92
Bob 80 79 81
Lucas 88 90 92
Maria 90 91 90
Sample Output:

Alice
Note: The five students' average scores are as follows:

John's average is 85.67
Alice's average is 91
Bob's average is 80
Lucas's average is 90
Maria's average is 90.33
Alice has the highest average score and showcases the best performance among all students.

'''
class Student:
    def __init__(self, name, scores):
        self._name = name  # protected attribute
        self.__scores = scores  # private attribute

    def calculate_average(self):
        return sum(self.__scores) / len(self.__scores)

    def get_name(self):  # public method to access protected attribute
        return self._name


class TopStudentFinder:
    def __init__(self):
        self.max_avg = -1.0
        self.top_student = ""

    def find_top_student(self, students):
       

        for student in  students:
            avg_score=student.calculate_average()
            if avg_score>self.max_avg:
                self.max_avg=avg_score
                self.top_student=student.get_name()
                
            


        
    def get_top_student(self):
        return self.top_student


if __name__ == "__main__":
    n = int(input())
    students_data = []

    for _ in range(n):
        student_info = input().split()
        name = student_info[0]
        scores = list(map(int, student_info[1:]))
        students_data.append(Student(name, scores))

    

    top_student_finder=TopStudentFinder()
    top_student_finder.find_top_student(students_data)
    top_student=top_student_finder.get_top_student()
    print(top_student)
   
