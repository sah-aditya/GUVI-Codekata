'''In a college, there are two types of students: Undergraduate and Graduate. Both types of students have a method get_fee() that returns the tuition fee. However, the tuition fee is calculated differently for Undergraduate and Graduate students. For Undergraduate students, the tuition fee is a fixed amount of $5000. For Graduate students, the tuition fee is the number of credits taken times $50.

Please write a Python program that defines classes for Undergraduate and Graduate students, both inheriting from a common Student class. The Student class should have the get_fee() method, which should be overridden in the Undergraduate and Graduate classes.

Sample Input:

60

Sample Output:

5000
3000

Explanation:

The Undergraduate class overrides the get_fee() method and returns a fixed amount of $5000. The Graduate class also overrides the get_fee() method and returns the number of credits taken times $50. In the sample input, the Graduate student has taken 60 credits, so the fee is 60 * $50 = $3000.

Constraints:

The number of credits for a Graduate student is a positive integer.'''



class Student:
    #..... YOUR CODE STARTS HERE .....
    
    def get_fee(self):
        return 0
    
    #..... YOUR CODE ENDS HERE .....

class Undergraduate(Student):
    def get_fee(self):
        #..... YOUR CODE STARTS HERE .....
    
        return 5000
    
        #..... YOUR CODE ENDS HERE .....

class Graduate(Student):
    def __init__(self, credits):
        #..... YOUR CODE STARTS HERE .....
    
        self.credits=credits
    
        #..... YOUR CODE ENDS HERE .....

    def get_fee(self):
        #..... YOUR CODE STARTS HERE .....
    
        return self.credits*50
    
        #..... YOUR CODE ENDS HERE .....

credits = int(input())

undergraduate = Undergraduate()
graduate = Graduate(credits)

programs = [undergraduate, graduate]
for program in programs:
    print(program.get_fee())