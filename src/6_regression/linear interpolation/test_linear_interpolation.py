import unittest
import numpy as np
import math
from scipy.interpolate import interp1d
from linear_interpolation import linear_interpolation


class TestLinearInterpolation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.x = np.array([-1, 4, 7])
        cls.y = np.array([1, 5, 2])

    def test_compare_with_scipy(self):
        points = [1, 2.5, 4.2]

        f = interp1d(self.x, self.y)

        for point in points:
            result = linear_interpolation(self.x, self.y, point)
            expected_result = f(point)
            assert math.isclose(result, expected_result, rel_tol=1e-5)


if __name__ == "__main__":
    unittest.main()
