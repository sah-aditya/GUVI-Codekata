'''You're required to write a program to calculate and print the area and perimeter of two rectangles given their sides. Implement a class named 'Rectangle' with methods named 'Area' and 'Perimeter', which return the area and perimeter, respectively. The length and breadth of the rectangles are passed as parameters to its constructor.

Input:

The input consists of two lines. Each line contains two integers representing the sides of the rectangles in the format (a, b) for the first rectangle and (c, d) for the second rectangle.

Output:

Output the area and perimeter of both rectangles separated by spaces in the format
Area1 Perimeter1
Area2 Perimeter2.

Sample Input:

3 4
4 5

Sample Output:

12 14
20 18'''


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    #..... YOUR CODE STARTS HERE .....

    def Area(self):
        return self.length*self.breadth
    def Perimeter(self):
        return 2*(self.length+self.breadth)
    #..... YOUR CODE ENDS HERE .....

def main():
    # Input for rectangle 1
    a, b = map(int, input().split())
    rectangle1 = Rectangle(a, b)
    
    # Input for rectangle 2
    c, d = map(int, input().split())
    rectangle2 = Rectangle(c, d)
    
    # Calculate and print area and perimeter for both rectangles
    print(rectangle1.Area(), rectangle1.Perimeter())
    print(rectangle2.Area(), rectangle2.Perimeter())

if __name__ == "__main__":
    main()

