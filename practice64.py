import numpy as np
x = np.array([6,8,12,14,18])
y = np.array([7,9,13,15,19])

def gradiant_descent(x,y):
    m = c = 0
    loop = 10
    alpha = 0.3
    n = len(x)
    for i in range(loop):
        yp = m*x + c
        costfunc = (1/n)*sum(val*val for val in (y-yp))
        dm = -(2/n)*sum(x*(y-yp))
        dn = -(2/n)*sum(y-yp)
        m = m - alpha*dm
        c = c - alpha*dn
        print(f"m:{m} c:{c} y:{yp} cost: {costfunc}")

gradiant_descent(x,y)