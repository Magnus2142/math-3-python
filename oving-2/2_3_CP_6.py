from numpy import *

def naive_gauss_elimination(matrix):
    rows=shape(matrix)[0]

    cols=shape(matrix)[1]

    print("Before Gausselimination:\n", matrix)

    for i in range(cols-1):
        for j in range(i+1,rows):
            print((matrix[j,i]/matrix[i,i])) # This is the multipliers
            matrix[j,:]=-(matrix[j,i]/matrix[i,i])*matrix[i,:]+matrix[j,:]

    print("After Gausselimination:\n", matrix)


matrix = array([[2*10**(-20), 1, 1], [1, 2, 4]], dtype=float)

# Example 2.13 version 2 IEEE double precision
naive_gauss_elimination(matrix)

# Example 2.13 version 3 IEEE double precision, after row exchange
matrix2 = array([[1, 2, 4], [2*10**(-20), 1, 1]], dtype=float)
naive_gauss_elimination(matrix2)