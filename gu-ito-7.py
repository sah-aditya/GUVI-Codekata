'''You are tasked with writing a program to calculate and print the area and circumference of a circle given its radius r units. Implement a class named 'Circle' without any parameter in its constructor.

Input:

The input consists of a single line containing an integer r representing the radius of the circle.

Output:

Output the area and circumference of the circle. Round the output to one decimal value.

Sample Input:

3

Sample Output:

28.3
18.8'''



import math

class Circle:
    #..... YOUR CODE STARTS HERE .....

    def area(self,radius):
        a=math.pi*radius*radius
        a=round(a,1)
        return a
    
    def circumference(self,radius):
        c=2*math.pi*radius
        c=round(c,1)
        return c
    #..... YOUR CODE ENDS HERE .....

def main():
    circle = Circle()
    
    # Input for the radius of the circle
    r = int(input())
    
    # Calculate and print the area and circumference of the circle
    print(circle.area(r))
    print(circle.circumference(r))

if __name__ == "__main__":
    main()
