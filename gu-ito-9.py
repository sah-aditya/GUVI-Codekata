'''You are required to implement a class called 'Matrix' containing a constructor that initializes the number of rows and the number of columns of a new Matrix object. The Matrix class should have the following methods:

print_rows(): Print the number of rows of the matrix.
print_cols(): Print the number of columns of the matrix.
print_elements(): Print the elements of the matrix in the form of a 2D array.
If the input is invalid, print 'invalid'.

Input:

The input consists of a single line in the format rowsxcols total_elements, where rows and cols are integers representing the number of rows and columns of the matrix respectively, and total_elements is the total number of elements in the matrix. This is followed by the elements of the matrix, each element separated by a space.

Output:

Output the number of rows and columns of the matrix on separate lines, followed by the elements of the matrix in the form of a 2D array.

Constraints:

The total number of elements in the matrix must equal rows * cols.

Sample Input:

3x3 9
1 2 3
4 5 6
7 8 9

Sample Output:

3
3
1 2 3
4 5 6
7 8 9'''



class Matrix:
    def __init__(self, rows, cols, elements):
        self.rows = rows
        self.cols = cols
        self.elements = elements

    def print_rows(self):
        print(self.rows)

    def print_cols(self):
        print(self.cols)

    def print_elements(self):
        for row in self.elements:
            print(*row)

def main():
    try:
        # Input
        rows_cols, total_elements = input().split()
        rows, cols = map(int, rows_cols.split("x"))
        total_elements = int(total_elements)

        # Validate input
        if rows * cols!= total_elements:
            print("invalid")
            return

        elements = [list(map(int, input().split())) for _ in range(rows)]

        matrix = Matrix(rows, cols, elements)

        # Output
        matrix.print_rows()
        matrix.print_cols()
        matrix.print_elements()

    except ValueError:
        print("invalid")

if __name__ == "__main__":
    main()