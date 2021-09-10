from numpy import *

a = array([[3, 1, 2],[6, 3, 4],[3, 1, 5]], dtype=float)
b = array([[4, 2, 0],[4, 4, 2],[2, 2, 3]], dtype=float)
c = array([[1, -1, 1, 2],[0, 2, 1, 0],[1, 3, 4, 4], [0, 2, 1, -1]], dtype=float)

def LO_factorization(matrix):
    rows=shape(matrix)[0]

    cols=shape(matrix)[1]

    L = identity(rows)

    print("Before LO factorization:\n", matrix)

    for i in range(cols-1):
        for j in range(i+1,rows):
            L[j, i] = matrix[j,i]/matrix[i,i] # This is the row multiplier
            if matrix[i, i] == 0:
                break
            matrix[j,:]=-(matrix[j,i]/matrix[i,i])*matrix[i,:]+matrix[j,:]

    print("After LO factorization:\n", L,"\n",matrix)


LO_factorization(a)
LO_factorization(b)
LO_factorization(c)