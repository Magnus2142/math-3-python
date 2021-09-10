from numpy import *

def fa(x):
    return x**3-9

def fb(x):
    return -5 - x + x**2 + (3 * x**3)

def fc(x):
    return cos(x)**2 + 6 - x

def samesign(a, b):
        return a * b > 0

def bisect(func, low, high, tolerance=None):


    assert not samesign(func(low), func(high))

    for i in range(54):
        midpoint = (low + high) / 2.0
        if samesign(func(low), func(midpoint)):
            low = midpoint
        else:
            high = midpoint
        if tolerance is not None and abs(high - low) < tolerance:
            break
    return midpoint


x1 = bisect(fa, 0, 2.5, 0.000001)

print("Value fa(x1)", fa(x1), "\nX value where fa(x) = 0: ", x1)

x2 = bisect(fb, -4, 2.5, 0.000001)

print("Value fa(x2)", fb(x2), "\nX value where fa(x) = 0: ", x2)

x3 = bisect(fc, -10, 20, 0.000001)

print("Value fa(x3)", fc(x3), "\nX value where fa(x) = 0: ", x3)