import unittest
import numpy as np
from implementation.newton_raphson import newton_raphson

class TestNewtonRaphson(unittest.TestCase):

    def test_quadratic_function(self):
        # Define the function, its gradient and Hessian
        def f(x):
            return x[0] ** 2 + x[1] ** 2

        def f_gradient(x):
            return np.array([2 * x[0], 2 * x[1]])

        def f_hessian(x):
            return np.array([[2, 0], [0, 2]])

        initial_point = np.array([1, 1])

        minimum_point, visited_points = newton_raphson(f, f_gradient, f_hessian, initial_point)
        np.testing.assert_almost_equal(minimum_point, np.array([0.0, 0.0]), decimal=6)

    def test_convergence_to_zero(self):
        # Test the function on x^2
        def f(x):
            return x[0]**2

        def f_gradient(x):
            return np.array([2*x[0]])

        def f_hessian(x):
            return np.array([2])

        initial_point = np.array([2])
        minimum_point, visited_points = newton_raphson(f, f_gradient, f_hessian, initial_point)
        np.testing.assert_almost_equal(minimum_point, np.array([0.0]), decimal=6)

if __name__ == '__main__':
    unittest.main()
