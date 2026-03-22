import random
from typing import List, Optional, Tuple, Union

import numpy as np


def lagrange_basis(
    i: int,
    x_values: Union[List[float], np.ndarray],
    x: Union[float, int],
    modulus: Optional[int] = None,
) -> Union[float, int]:
    """
    Compute the i-th Lagrange basis polynomial evaluated at x.

    The i-th basis polynomial is defined as:
        L_i(x) = product over j != i of (x - x_j) / (x_i - x_j)

    If modulus is provided, all arithmetic is performed in the finite
    field Z/modulus using modular inverse (for Shamir's Secret Sharing).

    Args:
        i: Index of the basis polynomial.
        x_values: Array of x coordinates of the data points.
        x: Point at which to evaluate the basis polynomial.
        modulus: Optional prime modulus for finite field arithmetic.

    Returns:
        Value of the i-th Lagrange basis polynomial at x.

    Raises:
        ValueError: If i is out of range or x_values has duplicate entries.
    """
    x_values = np.asarray(x_values)

    if i < 0 or i >= len(x_values):
        raise ValueError(
            f"Index i={i} is out of range for {len(x_values)} data points."
        )

    if len(x_values) != len(set(x_values.tolist())):
        raise ValueError("x_values must contain unique values.")

    result: Union[float, int] = 1

    for j in range(len(x_values)):
        if j == i:
            continue
        numerator = x - int(x_values[j])
        denominator = int(x_values[i]) - int(x_values[j])

        if modulus is not None:
            numerator = numerator % modulus
            denominator = denominator % modulus
            result = (result * numerator * pow(denominator, modulus - 2, modulus)) % modulus
        else:
            result = result * numerator / denominator

    return result


def lagrange_interpolate(
    x_data: Union[List[float], np.ndarray],
    y_data: Union[List[float], np.ndarray],
    x: Union[float, int],
    modulus: Optional[int] = None,
) -> Union[float, int]:
    """
    Evaluate the Lagrange interpolating polynomial at point x.

    Constructs the unique polynomial of degree at most n-1 that passes
    through all n data points and evaluates it at x.  When a modulus is
    provided, computation is done in the finite field Z/modulus, which
    is the core operation used to reconstruct a secret in Shamir's
    Secret Sharing scheme.

    Args:
        x_data: Array of x coordinates of the data points.
        y_data: Array of y coordinates of the data points.
        x: Point at which to evaluate the interpolating polynomial.
        modulus: Optional prime modulus for finite field arithmetic.

    Returns:
        Value of the interpolating polynomial at x.

    Raises:
        ValueError: If x_data and y_data differ in length, are empty,
                     or contain duplicate x values.
    """
    x_data = np.asarray(x_data)
    y_data = np.asarray(y_data)

    if len(x_data) != len(y_data):
        raise ValueError(
            f"x_data (length {len(x_data)}) and y_data (length {len(y_data)}) "
            "must have the same length."
        )

    if len(x_data) == 0:
        raise ValueError("At least one data point is required.")

    if len(x_data) != len(set(x_data.tolist())):
        raise ValueError("x_data must contain unique values.")

    result: Union[float, int] = 0

    for i in range(len(x_data)):
        basis = lagrange_basis(i, x_data, x, modulus)
        yi = int(y_data[i]) if modulus is not None else y_data[i]

        if modulus is not None:
            result = (result + yi * basis) % modulus
        else:
            result = result + yi * basis

    return result


def generate_shares(
    secret: int,
    num_shares: int,
    threshold: int,
    prime: int,
) -> List[Tuple[int, int]]:
    """
    Generate shares for Shamir's Secret Sharing.

    A random polynomial of degree (threshold - 1) is constructed with the
    constant term equal to the secret.  Each share is a point (x, f(x))
    evaluated over the finite field Z/prime.

    Args:
        secret: The integer secret to share (must be >= 0).
        num_shares: Total number of shares to generate.
        threshold: Minimum number of shares required to reconstruct the secret.
        prime: A prime number strictly greater than the secret.

    Returns:
        List of (x, y) tuples representing the shares.

    Raises:
        ValueError: If parameters are invalid.
    """
    if secret < 0:
        raise ValueError("Secret must be a non-negative integer.")

    if threshold < 1:
        raise ValueError("Threshold must be at least 1.")

    if threshold > num_shares:
        raise ValueError(
            f"Threshold ({threshold}) must be <= num_shares ({num_shares})."
        )

    if prime <= secret:
        raise ValueError(
            f"Prime ({prime}) must be strictly greater than the secret ({secret})."
        )

    # Build a random polynomial of degree (threshold - 1) with constant term = secret
    coefficients = [secret] + [
        random.randrange(0, prime) for _ in range(threshold - 1)
    ]

    shares: List[Tuple[int, int]] = []
    for i in range(1, num_shares + 1):
        y = 0
        for power, coeff in enumerate(coefficients):
            y = (y + coeff * pow(i, power, prime)) % prime
        shares.append((i, y))

    return shares


def reconstruct_secret(
    shares: List[Tuple[int, int]],
    prime: int,
) -> int:
    """
    Reconstruct the secret from shares using Lagrange interpolation at x=0.

    Given at least *threshold* shares produced by ``generate_shares``, this
    function recovers the original secret by evaluating the Lagrange
    interpolating polynomial at x = 0 over the finite field Z/prime.

    Args:
        shares: List of (x, y) tuples (at least *threshold* shares).
        prime: The prime modulus used during share generation.

    Returns:
        The reconstructed secret as an integer.

    Raises:
        ValueError: If shares list is empty.
    """
    if not shares:
        raise ValueError("At least one share is required.")

    x_data = [s[0] for s in shares]
    y_data = [s[1] for s in shares]

    return int(lagrange_interpolate(x_data, y_data, 0, modulus=prime))
