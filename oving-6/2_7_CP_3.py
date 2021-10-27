import numpy as np 


def Newtons_multivariate_method(f, df, x0, tol):
    x = x0
    while(np.abs(np.linalg.norm(f(x))) > tol):
        fx = f(x)
        dfx = df(x)
        s = np.linalg.solve(dfx, -fx)
        x = x+s
    return x


f = lambda x: np.array([x[0]**3-x[1]**3+x[0], x[0]**2 + x[1]**2 - 1]).reshape((2,1))
df = lambda x: np.array([3*x[0]**2 + 1, -3*x[1]**2, 2*x[0], 2*x[1]]).reshape((2,2))

x0 = np.array([1, 1]).reshape((2,1))


xa = Newtons_multivariate_method(f, df, x0, 0.0001)
print(xa)
