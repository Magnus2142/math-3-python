import numpy as np



# Takes in a array of vectors
def classical_Gram_Schmidt_orthogonalization(vector_array):
    
    n_vectors = vector_array.shape[0]
    y = np.zeros(vector_array.shape)
    q = np.zeros(vector_array.shape)
    r = np.zeros((n_vectors, n_vectors))


    for j in range(n_vectors):
        y[j] = vector_array[j]
        for i in range(j):
            r[i, j] = np.dot(q[i],vector_array[j])
            y[j] = y[j] - r[i, j]*q[i]
        r[j, j] = np.linalg.norm(y[j])
        q[j] = y[j]/r[j, j]
    # Transpose q to make the result easier to read
    return q.transpose(), r


vectors = np.array([[2, -2, 1], [3, -6, 0]])

result = classical_Gram_Schmidt_orthogonalization(vectors)

print("Q: \n", result[0])
print("R: \n", result[1])