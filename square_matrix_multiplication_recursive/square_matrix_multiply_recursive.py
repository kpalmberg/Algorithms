


def matrixAddition(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def squareMatrixMultiplyRecursive(A, B):
    n = len(A)

    #Initialize new n x n matrix 
    C = [[0 for j in range(0, n)] for i in range(0, n)] 

    #Base case, returns single 1x1 matrix with product of two 1x1 matrices from A,B when n == 1
    if(n == 1):
        newC = [[0 for j in range(0, n)] for i in range(0, n)] #new 1x1 matrix
        newC[0][0] = A[0][0] * B[0][0] #set the only element to product of the two 1x1 matrices A,B
        return newC #Return the 1x1 matrix

    #Get half the size of n, the size of our quandrants
    newSize = len(A) / 2
    newSize = int(newSize)

     #Initialize a sub matrices
    a11 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
    a12 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
    a21 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
    a22 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]

    #Initialize b sub matrices
    b11 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
    b12 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
    b21 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
    b22 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]   

    for i in range(0, newSize):
        for j in range(0, newSize):
            a11[i][j] = A[i][j] #Top left quadrant
            a12[i][j] = A[i][j + newSize] #Top right quadrant
            a21[i][j] = A[i + newSize][j] #Bottom left quadrant
            a22[i][j] = A[i + newSize][j + newSize] #Bottom right quadrant

            b11[i][j] = B[i][j] #Top left quadrant
            b12[i][j] = B[i][j + newSize] #Top right quadrant
            b21[i][j] = B[i + newSize][j] #Bottom left quadrant
            b22[i][j] = B[i + newSize][j + newSize] #Bottom right quadrant

    c11 = matrixAddition(squareMatrixMultiplyRecursive(a11, b11), squareMatrixMultiplyRecursive(a12, b21))
    c12 = matrixAddition(squareMatrixMultiplyRecursive(a11, b12), squareMatrixMultiplyRecursive(a12, b22))
    c21 = matrixAddition(squareMatrixMultiplyRecursive(a21, b11), squareMatrixMultiplyRecursive(a22, b21))
    c22 = matrixAddition(squareMatrixMultiplyRecursive(a21, b12), squareMatrixMultiplyRecursive(a22, b22))

    #Construct the new matrix
    for i in range(0, newSize):
        for j in range(0, newSize):
            C[i][j] = c11[i][j]
            C[i][j + newSize] = c12[i][j]
            C[i + newSize][j] = c21[i][j]
            C[i + newSize][j + newSize] = c22[i][j]

    #Return the new matrix
    return C

if __name__ == "__main__":
    A = [[13, 23, 3,33],
         [11, 6, 17,40],
         [8, 4, 13, 44],
         [54,13,24,33]]

    B = [[22, 1, 12, 7],
        [27, 5, 16, 5],
        [9, 10, 19, 11],
        [31, 45, 55, 17]]

    #Square matrix multiply recursive call
    C = squareMatrixMultiplyRecursive(A, B)

    print("SQUARE MATRIX RECURSIVE MULTIPLICATION:\n")

    print("MATRIX A IS:")
    for entry in A:
        for subEntry in entry:
            print(str(subEntry) + " ", end= " "),
        print("\n")

    print("MATRIX B IS:")
    for entry in B:
        for subEntry in entry:
            print(str(subEntry) + " ", end= " "),
        print("\n")

    print("SQUARE MATRIX MULTIPLICATION RECURSIVE RESULT:")

    for entry in C:
        for subEntry in entry:
            print(str(subEntry) + " ", end= " "),
        print("\n")