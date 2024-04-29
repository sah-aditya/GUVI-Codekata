'''You are required to write a program that calculates and prints the perimeter of a triangle given its three sides a, b, and c units. Implement a class named 'Triangle' without any parameter in its constructor.

Input:

The input consists of three lines. Each line contains an integer representing one side of the triangle.

Output:

Output the perimeter of the triangle.

Sample Input:

3
4
5

Sample Output:

12'''


class Triangle:
    def __init__(self):
        pass
    
    


a=int(input())
b=int(input())
c=int(input())
print(a+b+c)
    

def main():
    triangle = Triangle()
    
    # Input for the sides of the triangle
    a = int(input())
    b = int(input())
    c = int(input())
    
    # Calculate and print the perimeter of the triangle
    print(triangle.perimeter(a, b, c))

if __name__ == "__main__":
    main()
