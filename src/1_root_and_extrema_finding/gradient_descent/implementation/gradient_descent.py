import numpy as np

def gradient_descent(f, x1=0.1, x2=-0.1, gamma=1, num_iter=100, epsilon=1e-8):
    values = []
    x0 = np.array([x1, x2])
    for i in range(num_iter):
        values.append(x0)
        x0 -= gamma * gradient_f(f, x0)
        if np.linalg.norm(x0 - values[-1]) < epsilon:
            return x0[0], x0[1]
    raise ValueError("FAILURE")
