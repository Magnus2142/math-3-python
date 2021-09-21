import numpy as np

def fpi(g, x0, k):
    x = x0
    

    for i in range(k):
        x = g(x)

    return x


# 1.2 1 a)

def f(x):
    return ((2*x**3)-2)/((3*x**2)-2)

# 1.2 1 b)

def g(x):
    return np.log(7-x)


print("1.2 1 a) answer: ", fpi(f, 0.5, 1000))

print("1.2 1 b) answer: ", fpi(g, 0.5, 1000))

# I am not managing to find the g(x) of 1.2 1 c) :(((((