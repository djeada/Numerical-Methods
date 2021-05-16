import unittest
import numpy as np
from scipy import optimize
from least_squares import least_squares


class TestLeasSquares(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.x = np.array(
            [
                0.0,
                0.20408163,
                0.40816327,
                0.6122449,
                0.81632653,
                1.02040816,
                1.2244898,
                1.42857143,
                1.63265306,
                1.83673469,
                2.04081633,
                2.24489796,
                2.44897959,
                2.65306122,
                2.85714286,
                3.06122449,
                3.26530612,
                3.46938776,
                3.67346939,
                3.87755102,
                4.08163265,
                4.28571429,
                4.48979592,
                4.69387755,
                4.89795918,
                5.10204082,
                5.30612245,
                5.51020408,
                5.71428571,
                5.91836735,
                6.12244898,
                6.32653061,
                6.53061224,
                6.73469388,
                6.93877551,
                7.14285714,
                7.34693878,
                7.55102041,
                7.75510204,
                7.95918367,
                8.16326531,
                8.36734694,
                8.57142857,
                8.7755102,
                8.97959184,
                9.18367347,
                9.3877551,
                9.59183673,
                9.79591837,
                10.0,
            ]
        )
        cls.y = np.array(
            [
                -0.47139676,
                0.18310196,
                0.39951482,
                1.5576663,
                0.76340984,
                1.39095281,
                1.32319101,
                1.34522593,
                2.71198003,
                1.64900057,
                2.6192386,
                1.67330283,
                3.26002007,
                2.3623968,
                1.68320331,
                3.21782813,
                3.53049433,
                3.45982964,
                3.82994889,
                4.58339703,
                3.72655103,
                3.97591479,
                4.28123171,
                5.12941195,
                5.11461634,
                4.39917738,
                4.98486774,
                5.5335837,
                6.06553955,
                5.74859003,
                6.58515321,
                5.89555955,
                7.17880347,
                7.10074465,
                6.46172558,
                7.14980904,
                7.64307475,
                7.19799869,
                8.55219535,
                8.49926832,
                8.55443768,
                8.43600581,
                9.27978119,
                9.43767861,
                8.93879867,
                9.80153962,
                9.94328021,
                9.15692127,
                9.92889667,
                9.91725616,
            ]
        )

    def test_compare_with_np(self):
        alpha = least_squares(self.x, self.y)
        a = np.vstack([self.x, np.ones(len(self.x))]).T
        expected_alpha = np.linalg.lstsq(a, self.y, rcond=None)[0]
        np.testing.assert_allclose(alpha, expected_alpha)

    def test_compare_with_scipy(self):
        def func(x, a, b):
            return a * x + b

        alpha = least_squares(self.x, self.y)
        expected_alpha = optimize.curve_fit(func, xdata=self.x, ydata=self.y)[0]
        np.testing.assert_allclose(alpha, expected_alpha)


if __name__ == "__main__":
    unittest.main()
