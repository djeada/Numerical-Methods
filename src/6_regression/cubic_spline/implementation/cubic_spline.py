import numpy as np
import bisect
from typing import Callable

def solve_tridiagonal_system(a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray) -> np.ndarray:
    n = len(d)
    for i in range(1, n):
        w = a[i-1]/b[i-1]
        b[i] -= w*c[i-1]
        d[i] -= w*d[i-1]
    x = np.zeros(n)
    x[-1] = d[-1]/b[-1]
    for i in range(n-2,-1,-1):
        x[i] = (d[i]-c[i]*x[i+1])/b[i]
    return x

def cubic_spline(x_data: np.ndarray, y_data: np.ndarray) -> Callable[[float], float]:
    if x_data.shape[0] != y_data.shape[0]:
        raise ValueError()
    if x_data.shape[0] < 3:
        raise ValueError()
    if len(np.unique(x_data)) != x_data.shape[0]:
        raise ValueError()
    if not np.all(np.diff(x_data) > 0):
        raise ValueError()
    n = x_data.shape[0]
    h = np.diff(x_data)
    alpha = np.zeros(n-1)
    for i in range(1,n-1):
        alpha[i] = 3*( (y_data[i+1]-y_data[i])/h[i] - (y_data[i]-y_data[i-1])/h[i-1] )
    l = np.ones(n)
    mu = np.zeros(n)
    z = np.zeros(n)
    for i in range(1,n-1):
        l[i] = 2*(x_data[i+1]-x_data[i-1]) - h[i-1]*mu[i-1]
        mu[i] = h[i]/l[i]
        z[i] = (alpha[i]-h[i-1]*z[i-1])/l[i]
    M = np.zeros(n)
    for j in range(n-2,0,-1):
        M[j] = z[j]-mu[j]*M[j+1]
    def spline(X: float) -> float:
        if X < x_data[0] or X > x_data[-1]:
            raise ValueError()
        i = bisect.bisect_right(x_data, X)-1
        i = min(max(i,0),n-2)
        dx = X - x_data[i]
        return (M[i]/(6*h[i])*( (x_data[i+1]-X)**3 ) + M[i+1]/(6*h[i])*(dx**3)
                + (y_data[i]-M[i]*h[i]**2/6)*( (x_data[i+1]-X)/h[i] )
                + (y_data[i+1]-M[i+1]*h[i]**2/6)* (dx/h[i]) )
    return spline
