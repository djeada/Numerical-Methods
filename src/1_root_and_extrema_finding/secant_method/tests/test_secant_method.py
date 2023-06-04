import unittest
from implementation.secant_method import secant_method


class SecantMethodTestCase(unittest.TestCase):
    def test_root_on_interval(self):
        # Test the function on a simple linear function with a root on the interval
        def objective_function(x):
            return x - 3

        # Define the interval [a, b] within which to search for the root
        a = 2
        b = 4

        # Perform the secant search
        root = secant_method(objective_function, a, b)

        # Assert that the root value is close to the expected value
        expected_root = 3
        self.assertAlmostEqual(root, expected_root, places=3)

    def test_root_not_on_interval(self):
        # Test the function on a quadratic function with a root not on the interval
        def objective_function(x):
            return x ** 2 - 5 * x + 6

        # Define the interval [a, b] within which to search for the root
        a = 1
        b = 2

        # Perform the secant search
        root = secant_method(objective_function, a, b)

        # Assert that the root value is close to the expected value
        expected_root = 2
        self.assertAlmostEqual(root, expected_root, places=3)

    def test_multiple_roots(self):
        # Test the function on a cubic function with multiple roots on the interval
        def objective_function(x):
            return x ** 3 - 4 * x ** 2 + 3 * x

        # Define the interval [a, b] within which to search for the root
        a = 0
        b = 2

        # Perform the secant search
        root = secant_method(objective_function, a, b)

        # Assert that the root value is close to the expected value
        expected_root = 1
        self.assertAlmostEqual(root, expected_root, places=3)


# Run the tests
if __name__ == "__main__":
    unittest.main()
