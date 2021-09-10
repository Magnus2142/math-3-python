from numpy import *

a = array([[2, -2, -1, -2],[4, 1, -2, 1],[-2, 1, -1, -3]], dtype=float)
b = array([[1, 2, -1, 2],[0, 3, 1, 4],[2, -1, 1, 2]], dtype=float)
c = array([[2, 1, -4, -7],[1, -1, 1, -2],[-1, 3, -2, 6]], dtype=float)


def naive_gauss_elimination(matrix):
    rows=shape(matrix)[0]

    cols=shape(matrix)[1]

    print("Before Gausselimination:\n", matrix)

    for i in range(cols-1):
        for j in range(i+1,rows):
            print((matrix[j,i]/matrix[i,i])) # This is the multipliers
            matrix[j,:]=-(matrix[j,i]/matrix[i,i])*matrix[i,:]+matrix[j,:]

    print("After Gausselimination:\n", matrix)

def hilmat(a, b):
    return [[1 / (i + j + 1) for j in range(b)] for i in range(a)]

print(hilmat(3, 3))

naive_gauss_elimination(a)
naive_gauss_elimination(b)
naive_gauss_elimination(c)