from numpy import *

def LO_factorization(matrix):
    rows=shape(matrix)[0]

    cols=shape(matrix)[1]

    L = identity(rows)

    for i in range(cols-1):
        for j in range(i+1,rows):
            L[j, i] = matrix[j,i]/matrix[i,i] # This is the row multiplier
            if matrix[i, i] == 0:
                break
            matrix[j,:]=-(matrix[j,i]/matrix[i,i])*matrix[i,:]+matrix[j,:]

    U = matrix
    return L, U

def forward_substitution(L, c):
    # Number of rows
    n = L.shape[0]

    #Allocating space for the solution vector
    x = zeros_like(c, dtype=float)

    #Here we perform the forward-substitution.  
    #Initializing  with the first row.
    x[0] = c[0] / L[0, 0]

    for i in range(1, n):
        x[i] = (c[i] - dot(L[i, :i], c[:i])) / L[i, i]

    return x

def back_substitution(U, b):
    # Number of rows
    n = U.shape[0]


    # Allocating space for the solution vector
    x = zeros_like(b, dtype=float)

    x[-1] = b[-1] / U[-1, -1]

    #Looping over rows in reverse (from the bottom up), 
    #starting with the second to last row, because the 
    #last row solve was completed in the last step.
    for i in range(n-2, -1, -1):
        x[i] = (b[i] - dot(U[i,i:], x[i:])) / U[i,i]
        
    return x


a = array([[3, 1, 2],[6, 3, 4],[3, 1, 5]], dtype=float)
b1 = array([[0], [1], [3]])

b = array([[4, 2, 0],[4, 4, 2],[2, 2, 3]], dtype=float)
b2 = array([[2], [4], [6]])

c = array([[1, -1, 1, 2],[0, 2, 1, 0],[1, 3, 4, 4], [0, 2, 1, -1]], dtype=float)
b3 = array([[1], [1], [2], [0]])

# a)

LO_result = LO_factorization(a)
Lc_C = forward_substitution(LO_result[0], b1)
Ux_Y = back_substitution(LO_result[1], Lc_C)
print(Ux_Y)

# b)

LO_result = LO_factorization(b)
Lc_C = forward_substitution(LO_result[0], b2)
Ux_Y = back_substitution(LO_result[1], Lc_C)
print(Ux_Y)

# c
LO_result = LO_factorization(c)
Lc_C = forward_substitution(LO_result[0], b3)
Ux_Y = back_substitution(LO_result[1], Lc_C)
print(Ux_Y)