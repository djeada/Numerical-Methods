import unittest
import numpy as np

from implementation.gradient_descent import gradient_descent


class TestGradientDescent(unittest.TestCase):
    def objective_function(self, x):
        return x ** 2

    def gradient_function(self, x):
        return 2 * x

    def test_gradient_descent(self):
        initial_point = np.array([5])
        minimum, _ = gradient_descent(
            self.objective_function, self.gradient_function, initial_point
        )

        # The minimum for f(x) = x^2 is at x = 0
        np.testing.assert_array_almost_equal(minimum, 0, decimal=5)


if __name__ == "__main__":
    unittest.main()
