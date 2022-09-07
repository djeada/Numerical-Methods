import unittest
import numpy as np
import math
from scipy.interpolate import CubicSpline
from cubic_spline import cubic_spline


class TestCubicSpline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.x = np.array([-1, 4, 7])
        cls.y = np.array([1, 5, 2])
        cls.result_function = cubic_spline(cls.x, cls.y)
        cls.epsilon = 1e-5

    def test_distance_to_data_points(self):

        for i, x in enumerate(self.x):
            assert math.isclose(
                self.y[i], __class__.result_function(x), rel_tol=self.epsilon
            )

    def test_compare_with_scipy(self):
        cs = CubicSpline(self.x, self.y)
        for i, x in enumerate(self.x):
            assert math.isclose(
                cs(x), __class__.result_function(x), rel_tol=self.epsilon
            )


if __name__ == "__main__":
    unittest.main()
