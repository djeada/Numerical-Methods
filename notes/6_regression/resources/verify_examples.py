"""Recompute the regression chapter's examples with independent NumPy/SciPy solvers.

Run from the repository root:
    python notes/6_regression/resources/verify_examples.py

Requires NumPy and SciPy. These checks verify the documented examples, not
accuracy against an unknown underlying function or every repository algorithm.
"""

from math import factorial, pi, sqrt

import numpy as np
from numpy.testing import assert_allclose
from scipy.interpolate import BarycentricInterpolator, CubicSpline, RBFInterpolator
from scipy.special import expit


def check_regression():
    x = np.array([0.8, 1.2, 1.9, 2.4, 3.0])
    y = np.array([1.2, 1.9, 3.1, 3.9, 5.1])
    X = np.column_stack((np.ones(x.size), x))
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    assert_allclose(X.T @ X, [[5, 9.3], [9.3, 20.45]])
    assert_allclose(X.T @ y, [15.2, 33.79])
    assert_allclose(beta, np.array([-3.407, 27.59]) / 15.76)
    assert_allclose(X @ beta, [1.184327, 1.884581, 3.110025, 3.985343, 5.035723], atol=5e-7, rtol=0)
    r = y - X @ beta
    assert_allclose(X.T @ r, 0, atol=1e-12)
    assert_allclose(r @ r, 0.01199873096446699)
    tss = np.sum((y - y.mean()) ** 2)
    assert_allclose(tss, 9.672)
    assert_allclose(1 - (r @ r) / tss, 0.9987594364180659)
    assert_allclose(np.array([1, 2]) @ beta, 51.773 / 15.76)

    X = np.column_stack((np.ones(3), [1, 2, 3]))
    y = np.array([1, 2, 2])
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    r = y - X @ beta
    assert_allclose(beta, [2 / 3, 1 / 2])
    assert_allclose(r, [-1 / 6, 1 / 3, -1 / 6])
    assert_allclose(X.T @ r, 0, atol=1e-12)
    assert_allclose(r @ r, 1 / 6)
    assert_allclose(1 - (r @ r) / np.sum((y - y.mean()) ** 2), 0.75)
    assert_allclose(np.array([1, 4]) @ beta, 8 / 3)

    X = np.column_stack((np.ones(3), [-1, 0, 1]))
    y = np.array([0, 0, 1])
    probabilities = expit(X @ np.zeros(2))
    g = X.T @ (y - probabilities)
    information = X.T @ np.diag(probabilities * (1 - probabilities)) @ X
    beta = np.linalg.solve(information, g)
    assert_allclose(g, [-0.5, 1])
    assert_allclose(information, [[0.75, 0], [0, 0.5]])
    assert_allclose(beta, [-2 / 3, 2])
    assert_allclose(expit(np.array([1, 1]) @ beta), 0.791391472673955)
    eta = X @ beta
    assert_allclose(np.sum(y * eta - np.logaddexp(0, eta)), -0.7155083879727648)


def check_linear_and_polynomials():
    assert_allclose(np.interp(1, [-2, 2], [0, 2]), 1.5)
    estimate = np.interp(pi / 4, [0, pi / 2], [0, 1])
    assert_allclose(estimate, 0.5)
    assert abs(sqrt(2) / 2 - estimate) < (pi / 2) ** 2 / 8

    x = np.array([-1, 2, 3])
    y = np.array([1, 3, 5])
    interpolant = BarycentricInterpolator(x, y)
    q = np.array([-1, 0, 1, 2, 3])
    assert_allclose(interpolant(q), (q * q + q + 3) / 3)
    weights = np.array([1 / 12, -1 / 3, 1 / 4])
    assert_allclose(np.sum(weights * y / (1 - x)) / np.sum(weights / (1 - x)), 5 / 3)

    x = np.array([1, 2, 3, 4])
    y = np.array([2, 3, 5, 8])
    q = np.array([1, 2, 2.5, 3, 4])
    newton = 2 + (q - 1) * (1 + 0.5 * (q - 2))
    assert_allclose(newton, BarycentricInterpolator(x, y)(q))
    assert_allclose(newton[2], 3.875)


def gauss_terms(x, y, query, backward):
    """Evaluate the formulas printed in the note, checking every table index."""
    n = len(x) - 1
    m = (n + 1) // 2 if backward else n // 2
    t = (query - x[m]) / (x[1] - x[0])
    differences = [np.asarray(y, dtype=float)]
    for _ in range(n):
        differences.append(np.diff(differences[-1]))
    terms = [y[m]]
    for k in range(1, n + 1):
        base = m - ((k + 1) // 2 if backward else k // 2)
        assert 0 <= base and base + k <= n
        lo = -(k // 2) if backward else -((k - 1) // 2)
        hi = (k - 1) // 2 if backward else k // 2
        product = np.prod([t - j for j in range(lo, hi + 1)])
        terms.append(product * differences[k][base] / factorial(k))
    return terms


def check_gauss():
    x = np.arange(5, dtype=float)
    y = np.array([2, 3.5, 5, 5.8, 6])
    terms = gauss_terms(x, y, 1.5, backward=True)
    assert_allclose(terms, [5, -0.75, 0.0875, -0.04375, 0.01875])
    assert_allclose(np.cumsum(terms), [5, 4.25, 4.3375, 4.29375, 4.3125])
    assert_allclose(sum(terms), BarycentricInterpolator(x, y)(1.5))
    # Even and odd counts, both central rows, endpoints and interior queries.
    # Non-polynomial samples keep the highest differences nonzero.
    for count in (2, 3, 4, 5, 6):
        x = 0.3 + 0.7 * np.arange(count)
        y = np.exp(0.2 * x)
        reference = BarycentricInterpolator(x, y)
        for query in np.linspace(x[0], x[-1], 9):
            for backward in (False, True):
                assert_allclose(sum(gauss_terms(x, y, query, backward)), reference(query), atol=1e-12)


def check_splines():
    x = np.arange(9, 16, dtype=float)
    y = np.array([20, 22, 26, 28, 30, 31, 31])
    expected_M = np.array([0, 4.1, -4.4, 1.5, -1.6, -1.1, 0])
    spline = CubicSpline(x, y, bc_type="natural")
    assert_allclose(spline(x), y)
    assert_allclose(spline(x, 2), expected_M, atol=1e-12)
    A = np.diag(np.full(5, 4)) + np.diag(np.ones(4), 1) + np.diag(np.ones(4), -1)
    assert_allclose(A @ expected_M[1:-1], [12, -12, 0, -6, -6])
    assert_allclose(spline(10.5), 24.01875)
    assert_allclose(np.interp(10.5, x, y), 24)

    spline = CubicSpline([0, 1, 2], [0, 0.5, 0], bc_type="natural")
    # SciPy stores coefficients in descending powers of the local coordinate.
    assert_allclose(spline.c, [[-0.25, 0.25], [0, -0.75], [0.75, 0], [0, 0.5]])
    assert_allclose(spline(0.5), 0.34375)
    assert_allclose(spline([0, 2], 2), 0, atol=1e-12)
    assert_allclose(spline(1, 1), 0, atol=1e-12)
    assert_allclose(spline(1, 2), -1.5)

    coords = np.array([[0, 0], [1, 0], [0, 1], [1, 1]], dtype=float)
    P = np.column_stack((np.ones(4), coords))
    K = np.log(2) * np.fliplr(np.eye(4))
    A = np.block([[K, P], [P.T, np.zeros((3, 3))]])
    cases = [([0, 1, 1, 2], np.zeros(4), [0, 1, 1], 1),
             ([1, 0, 0, 1], np.array([1, -1, -1, 1]) / (2 * np.log(2)), [0.5, 0, 0], 0.5)]
    for z, w, alpha, midpoint in cases:
        coefficients = np.r_[w, alpha]
        assert_allclose(A @ coefficients, np.r_[z, np.zeros(3)], atol=1e-12)
        assert_allclose(np.linalg.solve(A, np.r_[z, np.zeros(3)]), coefficients, atol=1e-12)
        reference = RBFInterpolator(coords, z, kernel="thin_plate_spline", degree=1, smoothing=0)
        assert_allclose(reference(coords), z, atol=1e-12)
        assert_allclose(reference([[0.5, 0.5]]), midpoint)
        for q in ([0.2, 0.7], [0.8, 0.4]):
            distances = np.linalg.norm(coords - q, axis=1)
            value = np.r_[1, q] @ alpha + w @ (distances**2 * np.log(distances))
            assert_allclose(reference([q]), value, atol=1e-12)


if __name__ == "__main__":
    for check in (check_regression, check_linear_and_polynomials, check_gauss, check_splines):
        check()
        print(f"PASS: {check.__name__}")
    print("All documented example checks passed.")
