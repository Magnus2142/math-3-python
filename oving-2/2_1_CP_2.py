from numpy import *

def naive_gauss_elimination(matrix):
    rows=shape(matrix)[0]

    cols=shape(matrix)[1]

    print("Before Gausselimination:\n", matrix)

    for i in range(cols-1):

        for j in range(i+1,rows):

            matrix[j,:]=-(matrix[j,i]/matrix[i,i])*matrix[i,:]+matrix[j,:]

    print("After Gausselimination:\n", matrix)

def hilmat(a, b):
    return [[1 / (i + j + 1) for j in range(b)] for i in range(a)]


a = hilmat(2, 2)   
a = array(a, dtype=float)
z = ones((2,1), dtype=float)
a = append(a, z, axis=1)

naive_gauss_elimination(a)

b = hilmat(5, 5)   
b = array(b, dtype=float)
z = ones((5,1), dtype=float)
b = append(b, z, axis=1)

naive_gauss_elimination(b)

c = hilmat(10, 10)   
c = array(c, dtype=float)
z = ones((10,1), dtype=float)
c = append(c, z, axis=1)

naive_gauss_elimination(c)