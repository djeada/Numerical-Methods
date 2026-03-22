import pytest
import numpy as np
from ..implementation.lagrange_evaluation import (
    lagrange_basis,
    lagrange_interpolate,
    generate_shares,
    reconstruct_secret,
)


# ---------------------------------------------------------------------------
# lagrange_basis tests
# ---------------------------------------------------------------------------


def test_lagrange_basis_two_points():
    # Points: (0, *), (1, *).  L_0(x) at x=0 should be 1.
    x_values = [0, 1]
    assert lagrange_basis(0, x_values, 0) == pytest.approx(1.0)
    assert lagrange_basis(0, x_values, 1) == pytest.approx(0.0)
    assert lagrange_basis(1, x_values, 0) == pytest.approx(0.0)
    assert lagrange_basis(1, x_values, 1) == pytest.approx(1.0)


def test_lagrange_basis_three_points():
    x_values = [1, 2, 3]
    # L_0(1)=1, L_0(2)=0, L_0(3)=0
    assert lagrange_basis(0, x_values, 1) == pytest.approx(1.0)
    assert lagrange_basis(0, x_values, 2) == pytest.approx(0.0)
    assert lagrange_basis(0, x_values, 3) == pytest.approx(0.0)


def test_lagrange_basis_with_modulus():
    prime = 17
    x_values = [1, 2, 3]
    # L_0(0) mod 17 = (0-2)/(1-2) * (0-3)/(1-3) mod 17
    result = lagrange_basis(0, x_values, 0, modulus=prime)
    assert 0 <= result < prime


def test_lagrange_basis_index_out_of_range():
    with pytest.raises(ValueError, match="out of range"):
        lagrange_basis(3, [1, 2, 3], 0)


def test_lagrange_basis_negative_index():
    with pytest.raises(ValueError, match="out of range"):
        lagrange_basis(-1, [1, 2, 3], 0)


def test_lagrange_basis_duplicate_x_values():
    with pytest.raises(ValueError, match="unique"):
        lagrange_basis(0, [1, 1, 3], 0)


# ---------------------------------------------------------------------------
# lagrange_interpolate tests
# ---------------------------------------------------------------------------


def test_interpolate_linear():
    # f(x) = 2x + 1 through (0,1) and (1,3)
    x_data = [0, 1]
    y_data = [1, 3]
    assert lagrange_interpolate(x_data, y_data, 0) == pytest.approx(1.0)
    assert lagrange_interpolate(x_data, y_data, 1) == pytest.approx(3.0)
    assert lagrange_interpolate(x_data, y_data, 0.5) == pytest.approx(2.0)


def test_interpolate_quadratic():
    # f(x) = x^2 through (0,0), (1,1), (2,4)
    x_data = [0, 1, 2]
    y_data = [0, 1, 4]
    assert lagrange_interpolate(x_data, y_data, 3) == pytest.approx(9.0)
    assert lagrange_interpolate(x_data, y_data, -1) == pytest.approx(1.0)


def test_interpolate_single_point():
    assert lagrange_interpolate([5], [7], 5) == pytest.approx(7.0)
    assert lagrange_interpolate([5], [7], 10) == pytest.approx(7.0)


def test_interpolate_with_modulus():
    prime = 17
    x_data = [1, 2, 3]
    y_data = [5, 10, 15]
    result = lagrange_interpolate(x_data, y_data, 0, modulus=prime)
    assert 0 <= result < prime


def test_interpolate_with_numpy_arrays():
    x_data = np.array([0, 1, 2])
    y_data = np.array([1, 3, 7])
    result = lagrange_interpolate(x_data, y_data, 1)
    assert result == pytest.approx(3.0)


def test_interpolate_mismatched_lengths():
    with pytest.raises(ValueError, match="same length"):
        lagrange_interpolate([1, 2], [1], 0)


def test_interpolate_empty_data():
    with pytest.raises(ValueError, match="At least one"):
        lagrange_interpolate([], [], 0)


def test_interpolate_duplicate_x():
    with pytest.raises(ValueError, match="unique"):
        lagrange_interpolate([1, 1], [2, 3], 0)


# ---------------------------------------------------------------------------
# generate_shares tests
# ---------------------------------------------------------------------------


def test_generate_shares_count():
    shares = generate_shares(secret=42, num_shares=5, threshold=3, prime=97)
    assert len(shares) == 5


def test_generate_shares_x_values():
    shares = generate_shares(secret=10, num_shares=4, threshold=2, prime=97)
    x_vals = [s[0] for s in shares]
    assert x_vals == [1, 2, 3, 4]


def test_generate_shares_within_field():
    prime = 97
    shares = generate_shares(secret=50, num_shares=6, threshold=3, prime=prime)
    for _, y in shares:
        assert 0 <= y < prime


def test_generate_shares_negative_secret():
    with pytest.raises(ValueError, match="non-negative"):
        generate_shares(secret=-1, num_shares=3, threshold=2, prime=97)


def test_generate_shares_threshold_exceeds_num_shares():
    with pytest.raises(ValueError, match="Threshold"):
        generate_shares(secret=10, num_shares=2, threshold=3, prime=97)


def test_generate_shares_prime_not_greater_than_secret():
    with pytest.raises(ValueError, match="Prime"):
        generate_shares(secret=100, num_shares=3, threshold=2, prime=97)


def test_generate_shares_threshold_zero():
    with pytest.raises(ValueError, match="at least 1"):
        generate_shares(secret=10, num_shares=3, threshold=0, prime=97)


# ---------------------------------------------------------------------------
# reconstruct_secret tests
# ---------------------------------------------------------------------------


def test_reconstruct_exact_threshold():
    secret = 42
    prime = 97
    shares = generate_shares(secret, num_shares=5, threshold=3, prime=prime)
    # Use exactly 3 shares (the threshold)
    recovered = reconstruct_secret(shares[:3], prime)
    assert recovered == secret


def test_reconstruct_more_than_threshold():
    secret = 42
    prime = 97
    shares = generate_shares(secret, num_shares=6, threshold=3, prime=prime)
    # Use 5 shares (more than the threshold of 3)
    recovered = reconstruct_secret(shares[:5], prime)
    assert recovered == secret


def test_reconstruct_all_shares():
    secret = 42
    prime = 97
    shares = generate_shares(secret, num_shares=5, threshold=3, prime=prime)
    recovered = reconstruct_secret(shares, prime)
    assert recovered == secret


def test_reconstruct_zero_secret():
    secret = 0
    prime = 97
    shares = generate_shares(secret, num_shares=4, threshold=2, prime=prime)
    recovered = reconstruct_secret(shares[:2], prime)
    assert recovered == secret


def test_reconstruct_large_secret():
    secret = 123456
    prime = 524287  # Mersenne prime
    shares = generate_shares(secret, num_shares=6, threshold=4, prime=prime)
    recovered = reconstruct_secret(shares[:4], prime)
    assert recovered == secret


def test_reconstruct_threshold_one():
    # threshold=1 means the polynomial is constant: f(x) = secret
    secret = 77
    prime = 97
    shares = generate_shares(secret, num_shares=5, threshold=1, prime=prime)
    recovered = reconstruct_secret(shares[:1], prime)
    assert recovered == secret


def test_reconstruct_fewer_than_threshold_fails():
    secret = 42
    prime = 97
    shares = generate_shares(secret, num_shares=6, threshold=4, prime=prime)
    # Only 2 shares, but threshold is 4 — reconstruction should give a wrong answer
    recovered = reconstruct_secret(shares[:2], prime)
    assert 0 <= recovered < prime  # still a valid field element
    assert recovered != secret


def test_reconstruct_empty_shares():
    with pytest.raises(ValueError, match="At least one share"):
        reconstruct_secret([], 97)


def test_roundtrip_multiple_secrets():
    prime = 1000003
    for secret in [0, 1, 999, 500000]:
        shares = generate_shares(secret, num_shares=5, threshold=3, prime=prime)
        recovered = reconstruct_secret(shares[:3], prime)
        assert recovered == secret
