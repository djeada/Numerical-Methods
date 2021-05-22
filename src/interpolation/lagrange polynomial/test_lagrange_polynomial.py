import unittest
import numpy as np
import math
from scipy.interpolate import lagrange
from lagrange_polynomial import lagrange_polynomial


class TestLagrangePolynomial(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.x = np.array([-9, -5, -2.5, 4, 7])
        cls.y = np.array([-2, 3, 0, 5, 11])
        cls.result_function = lagrange_polynomial(cls.x, cls.y)
        cls.epsilon = 1e-5

    def test_distance_to_data_points(self):
        for i, x in enumerate(self.x):
            assert math.isclose(
                self.y[i], __class__.result_function(x), rel_tol=self.epsilon
            )

    def test_compare_with_scipy(self):
        lg = lagrange(self.x, self.y)
        for i, x in enumerate(self.x):
            assert math.isclose(
                lg(x), __class__.result_function(x), rel_tol=self.epsilon
            )


if __name__ == "__main__":
    unittest.main()
