import numpy as np


# func - array of f(t, y) function
# y0 - array of initial values y0 = [1, 0] for example, means y0_1 = 1 and y0_2 = 0
# h - how big each step is
# n - how many steps we want
def euler_on_system(func, y0, h, n):
    w = np.zeros((y0.size, n + 1))

    w[:, 0] = y0

    for i in range(1, n + 1):
        w[:, i] = w[:, i - 1] + (h * func(w[:, i - 1]))
    
    return w
        

y0 = np.array([1, 0])

F0 = lambda y1, y2: np.array([y1 + y2, -y1 + y2])
F = lambda y: F0(y[0], y[1])

# y1(1) and y2(2) actual values
y1_exact = 1.46869394
y2_exact = -2.287355287

# With h = 0.1
print("With h = 0.1")

h = 0.1
steps = int(1/h)

w = euler_on_system(F, y0, h, steps)
print("y1 approximate: ", w[0, -1])
print("y1 global error: ", abs(w[0, -1] - y1_exact))
print("\n")
print("y2 approximate: ", w[1, -1])
print("y1 global error: ", abs(w[1, -1] - y2_exact))

print("\n\n")

# With h = 0.01
print("With h = 0.01")

h = 0.01
steps = int(1/h)

w = euler_on_system(F, y0, h, steps)
print("y1 approximate: ", w[0, -1])
print("y1 global error: ", abs(w[0, -1] - y1_exact))
print("\n")
print("y2 approximate: ", w[1, -1])
print("y1 global error: ", abs(w[1, -1] - y2_exact))

# The lower the h is, the lower the global error is as well