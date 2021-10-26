import numpy as np



def power_iteration(A, init_vector, n_iterations):


    x = A@init_vector
    u = None

    for j in range(1, n_iterations):
        u = x / np.linalg.norm(x)
        x = A@u
        eigenvalue = u.transpose()@x

    u = x / np.linalg.norm(x)
    
    return u, eigenvalue


A = np.array([[10, -12, -6], [5, -5, -4], [-1, 0, 3]])
B = np.array([[-14, 20, 10], [-19, 27, 12], [23, -32, -13]])

init_vector = np.array([[1], [1], [1]])

print(power_iteration(A, init_vector, 30))
print(power_iteration(B, init_vector, 30))

