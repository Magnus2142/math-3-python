import numpy as np 


def Newtons_multivariate_method(f, df, x0, tol):
    x = x0
    while(np.abs(np.linalg.norm(f(x))) > tol):
        fx = f(x)
        dfx = df(x)
        s = np.linalg.solve(dfx, -fx)
        x = x+s
    return x

f = lambda x: np.array([x[0]**2+x[1]**2-1, (x[0]-1)**2 + x[1]**2 - 1]).reshape((2,1))
df = lambda x: np.array([2*x[0], 2*x[1], 2*x[0] - 2, 2*x[1]]).reshape((2,2))

f2 = lambda x: np.array([x[0]**2+4*x[1]**2-4, 4*x[0]**2 + x[1]**2 - 4]).reshape((2,1))
df2 = lambda x: np.array([2*x[0], 8*x[1], 8*x[0], 2*x[1]]).reshape((2,2))

f3 = lambda x: np.array([x[0]**2-4*x[1]**2-4, (x[0]-1)**2 + x[1]**2 - 4]).reshape((2,1))
df3 = lambda x: np.array([2*x[0], -8*x[1], 2*x[0] - 2, 2*x[1]]).reshape((2,2))



x0 = np.array([1, 1]).reshape((2,1))


xa = Newtons_multivariate_method(f, df, x0, 0.0001)
xb = Newtons_multivariate_method(f2, df2, x0, 0.0001)
xc = Newtons_multivariate_method(f3, df3, x0, 0.0001)
print(xa)
print("\n\n", xb)
print("\n\n", xc)
