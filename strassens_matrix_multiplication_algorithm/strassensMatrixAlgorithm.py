#Strassen's Algorithm, an algorithm for matrix multiplication.
#Reduces the number of times we have to recursively multiply
#compared to a traditional matrix multiplication method.

#Calculates addition between two matrices
def matrixAddition(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C

#Calculates subtraction between two matrices
def matrixSubtraction(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C

#Calculates product between two matrices
def squareMatrixProduct(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

#Strassen's algorithm
def strassenAlgorithm(A, B):
    n = len(A) #Number of rows

    #When length is 1, return product of two matrices, base case, return
    if(n == 1):
        return squareMatrixProduct(A, B)

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

    #Initialize new array 
    C = [[0 for j in range(0, n)] for i in range(0, n)] 

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

    #Compute 10 different matrices
    S1 = matrixSubtraction(b12, b22)
    S2 = matrixAddition(a11, a12)
    S3 = matrixAddition(a21, a22)
    S4 = matrixSubtraction(b21, b11)
    S5 = matrixAddition(a11, a22)
    S6 = matrixAddition(b11, b22)
    S7 = matrixSubtraction(a12, a22)
    S8 = matrixAddition(b21, b22)
    S9 = matrixSubtraction(a11, a21)
    S10 = matrixAddition(b11, b12)

    #Recursively multiply
    P1 = strassenAlgorithm(a11, S1)
    P2 = strassenAlgorithm(S2, b22)
    P3 = strassenAlgorithm(S3, b11)
    P4 = strassenAlgorithm(a22, S4)
    P5 = strassenAlgorithm(S5, S6)
    P6 = strassenAlgorithm(S7, S8)
    P7 = strassenAlgorithm(S9, S10)

    #Compute the quadrants for the new matrix
    c11 = matrixAddition(matrixSubtraction(matrixAddition(P5, P4), P2), P6)
    c12 = matrixAddition(P1, P2)
    c21 = matrixAddition(P3, P4)
    c22 = matrixSubtraction(matrixSubtraction(matrixAddition(P5, P1), P3), P7)

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

    #Strassen function call
    C = strassenAlgorithm(A, B) 

    print("STRASSEN'S MULTIPLICATION:\n")

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

    print("STRASSEN MATRIX MULTIPLICATION RESULT:")

    for entry in C:
        for subEntry in entry:
            print(str(subEntry) + " ", end= " "),
        print("\n")
