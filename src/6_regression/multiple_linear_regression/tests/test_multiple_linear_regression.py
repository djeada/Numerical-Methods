import unittest
import numpy as np
import math
from multiple_linear_regression import multiple_linear_regression
from sklearn import linear_model


class TestMultipleLinearRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        n = 100
        x_1 = np.random.uniform(low=0.0, high=100.0, size=n)
        x_2 = np.random.uniform(low=0.0, high=300.0, size=n)

        x_1.sort()
        x_2.sort()

        cls.x = np.column_stack((x_1, x_2))

        cls.y = np.random.uniform(low=-80, high=80, size=n)
        cls.y.sort()

        cls.epsilon = 1e-5

    def test_compare_with_sklearn(self):
        a, b = multiple_linear_regression(self.x, self.y)

        lm = linear_model.LinearRegression()
        lm.fit(self.x, self.y)
        expected_a = lm.intercept_
        expected_b = lm.coef_

        assert math.isclose(a, expected_a, rel_tol=self.epsilon)

        for elem, expected_elem in zip(b, expected_b):

            assert math.isclose(elem, expected_elem, rel_tol=self.epsilon)


if __name__ == "__main__":
    unittest.main()
