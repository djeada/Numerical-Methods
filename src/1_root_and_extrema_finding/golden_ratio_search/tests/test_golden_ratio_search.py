import unittest
from implementation.golden_ratio_search import golden_ratio_search


class GoldenRatioSearchTestCase(unittest.TestCase):
    def test_minimum_value(self):
        # Test the function on a simple quadratic function
        def objective_function(x):
            return (x - 2) ** 2

        # Define the interval [a, b] within which to search for the minimum
        a = 0
        b = 4

        # Perform the golden ratio search
        minimum = golden_ratio_search(objective_function, a, b)

        # Assert that the minimum value is close to the expected value
        expected_minimum = 2
        self.assertAlmostEqual(minimum, expected_minimum, places=3)

    def test_negative_interval(self):
        # Test the function on a different objective function with a negative interval
        def objective_function(x):
            return x ** 2 - 5 * x + 6

        # Define the interval [a, b] within which to search for the minimum
        a = -10
        b = -1

        # Perform the golden ratio search
        minimum = golden_ratio_search(objective_function, a, b)

        # Assert that the minimum value is close to the expected value
        expected_minimum = 2.5
        self.assertAlmostEqual(minimum, expected_minimum, places=3)


# Run the tests
if __name__ == "__main__":
    unittest.main()
