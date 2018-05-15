# Algorithm for square matrix multiplication (Recursive)
This is one of the intuitive approaches to matrix multiplication using recursion. This is a divide-and-conquer algorithm which 
partitions the given matrix into 4 quadrants of size n/2 where n is the number of rows in the original given matrix. For each 
of the multiplication steps we will use recursion until the size of the matrices being halfed reaches 1. Then it will return the
product of the two 1x1 matrices. This will be able to solve square matrix multiplication where n is an exact power of 2 in both
of the n x n matrices.
