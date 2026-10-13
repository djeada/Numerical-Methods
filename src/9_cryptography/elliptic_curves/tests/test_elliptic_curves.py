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
G = (3, 6)  # order 5
G2 = (0, 10)  # order 50
Q = (1, 43)  # on curve


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
    alice_pub = scalar_multiply(7, G2, A, P)  # (10, 76)
    bob_pub = scalar_multiply(11, G2, A, P)  # (17, 87)

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

    with pytest.raises(ValueError, match="Prime p must be > 3"):
        _validate_curve(2, 3, 2)
    # p = 3 is also excluded: short Weierstrass form needs char != 2, 3
    with pytest.raises(ValueError, match="Prime p must be > 3"):
        _validate_curve(1, 1, 3)
    # p = 5 is the smallest allowed prime; y^2 = x^3 + x + 1 is non-singular
    _validate_curve(1, 1, 5)


def test_validate_point_not_on_curve():
    from ..implementation.elliptic_curves import _validate_point_on_curve

    with pytest.raises(ValueError, match="not on the curve"):
        _validate_point_on_curve((1, 1), A, B, P)


def test_validate_point_infinity_always_valid():
    from ..implementation.elliptic_curves import _validate_point_on_curve

    # Should not raise
    _validate_point_on_curve(None, A, B, P)


# ---------------------------------------------------------------------------
# Validation wired into the public API
# ---------------------------------------------------------------------------


def test_public_functions_reject_small_characteristic():
    for p in (2, 3):
        with pytest.raises(ValueError, match="Prime p must be > 3"):
            point_add((0, 1), (0, 1), 1, p)
        with pytest.raises(ValueError, match="Prime p must be > 3"):
            point_double((0, 1), 1, p)
        with pytest.raises(ValueError, match="Prime p must be > 3"):
            scalar_multiply(2, (0, 1), 1, p)
        with pytest.raises(ValueError, match="Prime p must be > 3"):
            ecdh_shared_secret(2, (0, 1), 1, p)


def test_point_add_rejects_off_curve_point_when_b_given():
    with pytest.raises(ValueError, match="not on the curve"):
        point_add(G, (1, 1), A, P, b=B)
    # Without b the check cannot be made, matching the legacy behaviour
    assert point_add(G, G, A, P) == point_double(G, A, P)


def test_point_double_rejects_off_curve_point_when_b_given():
    with pytest.raises(ValueError, match="not on the curve"):
        point_double((1, 1), A, P, b=B)


def test_scalar_multiply_rejects_off_curve_point_when_b_given():
    with pytest.raises(ValueError, match="not on the curve"):
        scalar_multiply(3, (1, 1), A, P, b=B)


def test_scalar_multiply_rejects_singular_curve_when_b_given():
    with pytest.raises(ValueError, match="Singular curve"):
        scalar_multiply(3, (0, 0), 0, P, b=0)


def test_ecdh_rejects_invalid_public_key_when_b_given():
    with pytest.raises(ValueError, match="not on the curve"):
        ecdh_shared_secret(7, (1, 1), A, P, b=B)


def test_validated_results_match_unvalidated():
    assert scalar_multiply(7, G2, A, P, b=B) == scalar_multiply(7, G2, A, P)
    assert point_add(G2, Q, A, P, b=B) == (21, 73)
    assert point_double(G, A, P, b=B) == (80, 10)


# ---------------------------------------------------------------------------
# Group-law properties (exhaustive on a small curve)
# ---------------------------------------------------------------------------


def _all_points(a, b, p):
    pts = [None]
    for x in range(p):
        for y in range(p):
            if (y * y - (x**3 + a * x + b)) % p == 0:
                pts.append((x, y))
    return pts


def test_group_law_exhaustive_small_curve():
    a, b, p = 2, 3, 7  # includes a point with y = 0 for 2-torsion
    pts = _all_points(a, b, p)
    assert any(pt is not None and pt[1] == 0 for pt in pts)
    for P1 in pts:
        # identity
        assert point_add(P1, None, a, p, b) == P1
        assert point_add(None, P1, a, p, b) == P1
        # inverse
        neg = None if P1 is None else (P1[0], (-P1[1]) % p)
        assert point_add(P1, neg, a, p, b) is None
        # closure
        assert is_on_curve(point_double(P1, a, p, b), a, b, p)
        for P2 in pts:
            S = point_add(P1, P2, a, p, b)
            assert is_on_curve(S, a, b, p)
            assert S == point_add(P2, P1, a, p, b)
            for P3 in pts:
                assert point_add(S, P3, a, p, b) == point_add(
                    P1, point_add(P2, P3, a, p, b), a, p, b
                )


def test_doubling_point_with_y_zero_is_infinity():
    a, b, p = 2, 3, 7
    pts = [pt for pt in _all_points(a, b, p) if pt and pt[1] == 0]
    for pt in pts:
        assert point_double(pt, a, p, b) is None
        assert point_add(pt, pt, a, p, b) is None
        assert scalar_multiply(2, pt, a, p, b) is None
        assert scalar_multiply(3, pt, a, p, b) == pt


def test_smallest_allowed_prime_group_law():
    # y^2 = x^3 + x + 1 over F_5 has 9 points (cyclic of order 9)
    a, b, p = 1, 1, 5
    pts = _all_points(a, b, p)
    assert len(pts) == 9
    gen = next(
        pt
        for pt in pts
        if pt is not None
        and scalar_multiply(9, pt, a, p, b) is None
        and scalar_multiply(3, pt, a, p, b) is not None
    )
    seen = {scalar_multiply(k, gen, a, p, b) for k in range(9)}
    assert seen == set(pts)
