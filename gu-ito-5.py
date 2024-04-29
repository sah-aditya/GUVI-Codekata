'''You are required to write a program that calculates and prints the area of a triangle given its base and height. Implement a class named 'Triangle' without any parameter in its constructor.

Input:

The input consists of two lines. Each line contains an integer representing either the base or the height of the triangle.

Output:

Output the area of the triangle.

Sample Input:

6
6

Sample Output:

18'''


class Triangle:
    #..... YOUR CODE STARTS HERE .....

    def calculate_area(self,b,h):
        return 0.5*b*h

    #..... YOUR CODE ENDS HERE .....

def main():
    triangle = Triangle()
    
    # Input for the base of the triangle
    base = int(input())
    
    # Input for the height of the triangle
    height = int(input())
    
    # Calculate and print the area of the triangle
    area = triangle.calculate_area(base, height)
    print(area)

if __name__ == "__main__":
    main()
