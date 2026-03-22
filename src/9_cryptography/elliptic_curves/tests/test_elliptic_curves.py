import pytest

from ..implementation.elliptic_curves import (
    is_on_curve,
    point_add,
    point_double,
    scalar_multiply,
    ecdh_shared_secret,
)

# Curve: y² = x³ + 2x + 3 (mod 97)
A = 2
B = 3
P = 97

# Known points on the curve (verified by hand)
G = (3, 6)        # order 5
G2 = (0, 10)      # order 50
Q = (1, 43)        # on curve


# ---------------------------------------------------------------------------
# is_on_curve tests
# ---------------------------------------------------------------------------


def test_is_on_curve_valid_point():
    assert is_on_curve(G, A, B, P) is True


def test_is_on_curve_second_valid_point():
    assert is_on_curve(Q, A, B, P) is True


def test_is_on_curve_point_at_infinity():
    assert is_on_curve(None, A, B, P) is True


def test_is_on_curve_invalid_point():
    assert is_on_curve((1, 1), A, B, P) is False


def test_is_on_curve_another_invalid_point():
    assert is_on_curve((0, 0), A, B, P) is False


# ---------------------------------------------------------------------------
# point_add tests
# ---------------------------------------------------------------------------


def test_point_add_two_distinct_points():
    # G2=(0,10) + Q=(1,43) on y²=x³+2x+3 (mod 97) => (21, 73)
    result = point_add(G2, Q, A, P)
    assert result == (21, 73)


def test_point_add_identity_left():
    result = point_add(None, G, A, P)
    assert result == G


def test_point_add_identity_right():
    result = point_add(G, None, A, P)
    assert result == G


def test_point_add_both_identity():
    result = point_add(None, None, A, P)
    assert result is None


def test_point_add_same_point_delegates_to_double():
    # Adding a point to itself should produce the same result as doubling
    result_add = point_add(G, G, A, P)
    result_double = point_double(G, A, P)
    assert result_add == result_double


def test_point_add_inverse_gives_infinity():
    # G = (3, 6), -G = (3, 91) since 6 + 91 = 97 ≡ 0 (mod 97)
    neg_G = (3, 91)
    assert is_on_curve(neg_G, A, B, P) is True
    result = point_add(G, neg_G, A, P)
    assert result is None


# ---------------------------------------------------------------------------
# point_double tests
# ---------------------------------------------------------------------------


def test_point_double():
    # 2*(3,6) = (80, 10)
    result = point_double(G, A, P)
    assert result == (80, 10)
    assert is_on_curve(result, A, B, P) is True


def test_point_double_infinity():
    result = point_double(None, A, P)
    assert result is None


def test_point_double_result_on_curve():
    result = point_double(G2, A, P)
    assert result == (65, 32)
    assert is_on_curve(result, A, B, P) is True


# ---------------------------------------------------------------------------
# scalar_multiply tests
# ---------------------------------------------------------------------------


def test_scalar_multiply_k_zero():
    result = scalar_multiply(0, G, A, P)
    assert result is None


def test_scalar_multiply_k_one():
    result = scalar_multiply(1, G, A, P)
    assert result == G


def test_scalar_multiply_k_two():
    result = scalar_multiply(2, G, A, P)
    assert result == (80, 10)


def test_scalar_multiply_k_three():
    result = scalar_multiply(3, G, A, P)
    assert result == (80, 87)


def test_scalar_multiply_k_four():
    result = scalar_multiply(4, G, A, P)
    assert result == (3, 91)


def test_scalar_multiply_at_order():
    # G has order 5, so 5*G = point at infinity
    result = scalar_multiply(5, G, A, P)
    assert result is None


def test_scalar_multiply_multiple_of_order():
    # 10*G should also be None since order is 5
    result = scalar_multiply(10, G, A, P)
    assert result is None


def test_scalar_multiply_with_larger_order_point():
    # 7 * (0,10) = (10, 76)
    result = scalar_multiply(7, G2, A, P)
    assert result == (10, 76)


def test_scalar_multiply_identity_point():
    result = scalar_multiply(5, None, A, P)
    assert result is None


def test_scalar_multiply_negative_k_raises():
    with pytest.raises(ValueError, match="non-negative"):
        scalar_multiply(-1, G, A, P)


# ---------------------------------------------------------------------------
# ecdh_shared_secret tests
# ---------------------------------------------------------------------------


def test_ecdh_shared_secret():
    # Alice: private=7, Bob: private=11, generator G2=(0,10)
    alice_pub = scalar_multiply(7, G2, A, P)   # (10, 76)
    bob_pub = scalar_multiply(11, G2, A, P)     # (17, 87)

    shared_alice = ecdh_shared_secret(7, bob_pub, A, P)
    shared_bob = ecdh_shared_secret(11, alice_pub, A, P)

    assert shared_alice == shared_bob
    assert shared_alice == (49, 63)


def test_ecdh_invalid_private_key():
    with pytest.raises(ValueError, match="positive integer"):
        ecdh_shared_secret(0, G, A, P)

    with pytest.raises(ValueError, match="positive integer"):
        ecdh_shared_secret(-3, G, A, P)


# ---------------------------------------------------------------------------
# Error handling tests
# ---------------------------------------------------------------------------


def test_validate_curve_singular():
    from ..implementation.elliptic_curves import _validate_curve

    with pytest.raises(ValueError, match="Singular curve"):
        _validate_curve(0, 0, 97)


def test_validate_curve_small_prime():
    from ..implementation.elliptic_curves import _validate_curve

    with pytest.raises(ValueError, match="Prime p must be > 2"):
        _validate_curve(2, 3, 2)


def test_validate_point_not_on_curve():
    from ..implementation.elliptic_curves import _validate_point_on_curve

    with pytest.raises(ValueError, match="not on the curve"):
        _validate_point_on_curve((1, 1), A, B, P)


def test_validate_point_infinity_always_valid():
    from ..implementation.elliptic_curves import _validate_point_on_curve

    # Should not raise
    _validate_point_on_curve(None, A, B, P)
