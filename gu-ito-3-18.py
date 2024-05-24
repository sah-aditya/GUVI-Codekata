'''You are developing a calculator in Python. The calculator has four operations: add, subtract, multiply, and divide. Each operation is a function that takes two numbers and returns the result of the operation.

Write a Python function calculate(operation: Callable[[float, float], float], num1: float, num2: float) -> float that takes an operation function and two numbers as input and returns the result of the operation. The operation function is a higher-order function that can be any of the four operation functions.

Constraints:

num1 and num2 are floats.
You can't install any external libraries.
Sample Input:

add, 1.0, 2.0

Sample Output:

3.0

Explanation:

In the sample outputs, each number is the result of a calculation performed by the calculate function. The calculate function is a higher-order function, which means it accepts other functions as arguments and/or returns a function as its result. In this case, calculate accepts an operation function as an argument and applies it to the two number arguments.

The operation functions (add, divide) are defined using lambda functions, which are small anonymous functions defined with the lambda keyword in Python. They can take any number of arguments but can only have one expression. In this case, each lambda function takes two arguments and returns the result of a specific arithmetic operation.

This demonstrates the power and flexibility of higher-order functions and lambda functions in Python. They allow us to write more modular and concise code by treating functions as first-class objects, meaning that functions can be passed around and used as arguments or return values, just like any other objects (strings, numbers, lists, etc.).'''



from typing import Callable

def calculate(operation: Callable[[float, float], float], num1: float, num2: float) -> float:
    #..... YOUR CODE STARTS HERE .....
    
    return operation(num1, num2)    
    
    #..... YOUR CODE ENDS HERE .....
    
def clean_input(value):
    return str(value.strip())

add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else None


operation, num1, num2 = map(clean_input, input().strip().split(','))

func = None

if (operation == 'add'):
    func = add
    
elif (operation == 'subtract'):
    func = subtract
    
elif (operation == 'multiply'):
    func = multiply
    
elif (operation == 'divide'):
    func = divide

print(calculate(func, float(num1), float(num2)))
