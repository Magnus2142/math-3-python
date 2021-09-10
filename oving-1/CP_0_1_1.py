


def horner(poly, n, x):
    

    result = poly[0]

    for i in range(1, n):

        result = result * x + poly[i]


    return result



# P(x)=1+x+ ··· +x^50

poly = [1] * 51

x = 1.00001
n = len(poly)

print("Value of polynomial is" , horner(poly, n, x))

# Q(x)=(x51−1)/(x−1)
# Error of computation is 4.76×10^(−12)