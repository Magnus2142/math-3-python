import numpy as np
from math import e


# func - f(t, y) function
# inter - interval as an array with 2 elements for example [0, 1]
# y0 - y(0) = y0, the initial value
# n - how many steps we want
def euler(func, inter, y0, n):
    # initializing the t values and euler approximation array
    t = np.zeros(n + 1)
    w = np.zeros(n + 1)

    t[0] = inter[0]
    w[0] = y0
    h = (inter[1] - inter[0])/n


    for i in range(1, n + 1):
        t[i] = t[i - 1] + h
        w[i] = w[i - 1] + (h * func(t[i - 1], w[i - 1]))
    
    return t, w
        


# 1a
# Defining the function to use
def f(t, y):
    return t

# 1b
# Defining the function to use
def f_2(t, y):
    return t**2 * y


# Both tasks uses the same interval, y0 and amount of steps
interval = np.array([0, 1])
y0 = 1
steps = 10

#  1a Exact function
def f_exact(t):
    return 0.5*t**2 + 1

# 1b Actual value of y(1) = 
def f_2_exact(t):
    return e**((1/3)*t**3)

# 1a first
result = euler(f, interval, y0, steps)

full_results = np.array([result[0], result[1], np.zeros(steps + 1)]).transpose()

for i in range(steps + 1):
    full_results[i, 2] = abs(full_results[i, 1] - f_exact(full_results[i, 0]))

print("[t, w, error]")
print(full_results)

# 1b second
result = euler(f_2, interval, y0, steps)

full_results = np.array([result[0], result[1], np.zeros(steps + 1)]).transpose()

for i in range(steps + 1):
    full_results[i, 2] = abs(full_results[i, 1] - f_2_exact(full_results[i, 0]))

print("[t, w, error]")
print(full_results)