'''You are implementing a simple calculator. Write a Python class Calculator with static methods add, subtract, multiply, and divide that perform the respective operations.

Input:

num1: a float, the first number.
num2: a float, the second number.
Output:

The function should return the result of the operation.
Sample Input:

Calculator.add(5, 3)

Sample Output:

8

Explanation:

The class Calculator has static methods add, subtract, multiply, and divide which perform the respective operations. Static methods, marked with the @staticmethod decorator, don't take a self or cls parameter. This means you can't modify object state or class state within a static method. However, they're useful when you need to perform a utility function that doesn't modify the state of the object or class, like in this case where we're performing simple mathematical operations.'''




class Calculator:
    @staticmethod
    def add(num1, num2):
        #..... YOUR CODE STARTS HERE .....
    
            return num1+num2
    
        #..... YOUR CODE ENDS HERE .....

    @staticmethod
    def subtract(num1, num2):
        #..... YOUR CODE STARTS HERE .....
    
            return num1-num2
    
        #..... YOUR CODE ENDS HERE .....

    @staticmethod
    def multiply(num1, num2):
        #..... YOUR CODE STARTS HERE .....
    
        return num1*num2
    
        #..... YOUR CODE ENDS HERE .....

    @staticmethod
    def divide(num1, num2):
        #..... YOUR CODE STARTS HERE .....
    
            return num1/num2
    
        #..... YOUR CODE ENDS HERE .....
            
def call_func(func, args):
    value = None
    num1, num2 = args
    
    if (func == "add"):
        value = Calculator.add(num1, num2)
        
    elif (func == "subtract"):
        value = Calculator.subtract(num1, num2)
    
    elif (func == "multiply"):
        value = Calculator.multiply(num1, num2)
        
    elif (func == "divide"):
        value = Calculator.divide(num1, num2)
        
    return value
    
    
if __name__ == "__main__":
    func_call = list(map(lambda x: str(x.strip()), input().strip().split('.')))
    class_name, func = func_call
    
    if (class_name == 'Calculator'):
        parans_pos = func.index('(')
        
        name = func[:parans_pos].strip()
        args = tuple(map(lambda x: int(x.strip()), func[parans_pos+1: len(func)-1].strip().split(',')))
        
        print(call_func(name, args))