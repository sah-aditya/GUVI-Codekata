'''You need to implement a Matrix class with methods to perform various operations on matrices. The class should have methods for the following:

Get the number of rows.
Get the number of columns.
Set the elements of the matrix at a given position (i, j).
Multiply two matrices.
Input:

The input consists of the following:

Number of rows for the first matrix (mat1).
Number of columns for the first matrix (mat1).
Values of each element of the first matrix (mat1) in row-major order.
Number of rows for the second matrix (mat2).
Number of columns for the second matrix (mat2).
Values of each element of the second matrix (mat2) in row-major order.
Output:

After inputting both matrices, print each resultant element of the matrix multiplication in a loop.

Sample Input:

2
2
2 2 2 2
2
2
2 2 2 2

Sample Output:

8 8 8 8'''




class Matrix:
    #..... YOUR CODE STARTS HERE .....

    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.matrix=[[0 for _ in range(cols)]for _ in range(rows)]
    
    def get_rows(self):
        return self.rows
    def get_cols(self):
        return self.cols
    
    def set_element(self,i,j,value):
        self.matrix[i][j]=value
    
    def multiply(self,other):
        if self.cols !=other.rows:
            print("Invalid")
            return None
        
        result= Matrix(self.rows,other.cols)
        
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.matrix[i][j]+= self.matrix[i][k] * other.matrix[k][j]
        return result

    #..... YOUR CODE ENDS HERE .....

def main():
    mat1_rows = int(input())
    mat1_cols = int(input())
    mat1_values = list(map(int, input().split()))

    mat2_rows = int(input())
    mat2_cols = int(input())
    mat2_values = list(map(int, input().split()))

    if mat1_cols != mat2_rows:
        print("Invalid")
        return

    mat1 = Matrix(mat1_rows, mat1_cols)
    mat2 = Matrix(mat2_rows, mat2_cols)

    # Set values for matrix 1
    index = 0
    for i in range(mat1_rows):
        for j in range(mat1_cols):
            mat1.set_element(i, j, mat1_values[index])
            index += 1

    # Set values for matrix 2
    index = 0
    for i in range(mat2_rows):
        for j in range(mat2_cols):
            mat2.set_element(i, j, mat2_values[index])
            index += 1

    # Multiply matrices
    result = mat1.multiply(mat2)

    if result:
        for i in range(result.get_rows()):
            for j in range(result.get_cols()):
                if j+1 == result.get_cols() and i+1 == result.get_rows():
                    print(result.matrix[i][j], end="")
                else:
                    print(result.matrix[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()
