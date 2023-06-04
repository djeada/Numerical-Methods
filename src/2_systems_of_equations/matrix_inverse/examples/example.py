"""
Find the solution to the following system of linear equations:

x+y+z=2
6x−4y+5z=31
5x+2y+2z=13
"""
import numpy as np

A = np.array([[1.0, 1.0, 1.0], [6.0, -4.0, 5.0], [5.0, 2.0, 2.0]])
b = np.array([2.0, 31.0, 13.0])

if np.isclose(np.linalg.det(A), 0):
    raise ValueError("Because matrix A is singular, it cannot be inverted.")

x = np.dot(np.linalg.inv(A), b)
print(x)
