from math import *
from sympy import *

# Define x as an symbol
x = Symbol('x')


# Define the function
f = ((2*pi*x**3)/3) + ((0.1*pi*x**2)/3) - (6*10**(-5))

# define the derived function
f_prime = f.diff(x)

# Connect x and the functions so we can use the functions like f(3) and f_prime(2) for example
f = lambdify(x, f)
f_prime = lambdify(x, f_prime)

# Setting the start value as 1
x_approximate = 1

# Setting tolerance
tolerance = 0.00001

# Setting max iterations
max_iterations = 100

for i in range(0, max_iterations):
    x_approximate = x_approximate - (f(x_approximate) / f_prime(x_approximate))
    if f(x_approximate) < tolerance:
        print("Breaking after", i, "iterations")
        break
    

print("The approximated root is: ", x_approximate)
print("f(x_approximate) = ", f(x_approximate))

# The radius of the hemisphere is about 0.02 meters