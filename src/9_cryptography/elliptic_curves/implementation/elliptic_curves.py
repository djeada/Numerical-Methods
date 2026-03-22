"""
Elliptic Curve Arithmetic over Prime Finite Fields

Provides core operations on elliptic curves of the form
    y² ≡ x³ + ax + b  (mod p)
where *p* is a prime, together with a simple ECDH key-exchange
helper.

Points are represented as ``(x, y)`` tuples.  The *point at
infinity* (identity element) is represented by ``None``.
"""

from typing import Optional, Tuple

# A point is either an (x, y) tuple or None (point at infinity).
Point = Optional[Tuple[int, int]]


# ------------------------------------------------------------------
# Internal helpers
# ------------------------------------------------------------------


def _validate_curve(a: int, b: int, p: int) -> None:
    """Validate that curve parameters define a non-singular curve.

    Args:
        a: Coefficient *a* of the curve.
        b: Coefficient *b* of the curve.
        p: Prime modulus of the finite field.

    Raises:
        ValueError: If *p* is not greater than 2 or the curve is singular.
    """
    if p <= 2:
        raise ValueError(f"Prime p must be > 2, got {p}.")

    discriminant = (4 * pow(a, 3) + 27 * pow(b, 2)) % p
    if discriminant == 0:
        raise ValueError(
            f"Singular curve: 4a³ + 27b² ≡ 0 (mod {p}). "
            "Choose different a, b, or p."
        )


def _validate_point_on_curve(point: Point, a: int, b: int, p: int) -> None:
    """Raise if *point* does not lie on the curve.

    Args:
        point: The point to validate (``None`` is always accepted).
        a: Coefficient *a* of the curve.
        b: Coefficient *b* of the curve.
        p: Prime modulus of the finite field.

    Raises:
        ValueError: If the point is not on the curve.
    """
    if point is not None and not is_on_curve(point, a, b, p):
        raise ValueError(f"Point {point} is not on the curve.")


# ------------------------------------------------------------------
# Public API
# ------------------------------------------------------------------


def is_on_curve(point: Point, a: int, b: int, p: int) -> bool:
    """Check whether *point* lies on the curve y² ≡ x³ + ax + b (mod p).

    The point at infinity (``None``) is always considered to be on
    every curve.

    Args:
        point: An ``(x, y)`` tuple or ``None`` for the point at infinity.
        a: Coefficient *a* of the curve equation.
        b: Coefficient *b* of the curve equation.
        p: Prime modulus defining the finite field.

    Returns:
        ``True`` if the point satisfies the curve equation, ``False``
        otherwise.
    """
    if point is None:
        return True

    x, y = point
    lhs = pow(y, 2, p)
    rhs = (pow(x, 3, p) + a * x + b) % p
    return lhs == rhs


def point_add(P: Point, Q: Point, a: int, p: int) -> Point:
    """Add two points on the elliptic curve.

    Handles the following special cases:

    * Either operand is ``None`` (point at infinity / identity).
    * ``P == Q`` — delegates to :func:`point_double`.
    * ``P`` and ``Q`` share the same *x* but different *y* (inverse
      points) — returns ``None``.

    Args:
        P: First point (or ``None``).
        Q: Second point (or ``None``).
        a: Coefficient *a* of the curve equation.
        p: Prime modulus defining the finite field.

    Returns:
        The sum ``P + Q`` on the curve, or ``None`` for the point at
        infinity.
    """
    if P is None:
        return Q
    if Q is None:
        return P

    x_p, y_p = P
    x_q, y_q = Q

    if x_p % p == x_q % p:
        if y_p % p == y_q % p:
            return point_double(P, a, p)
        # P and Q are inverses of each other
        return None

    # Slope of the secant line
    lam = ((y_q - y_p) * pow(x_q - x_p, -1, p)) % p

    x_r = (lam * lam - x_p - x_q) % p
    y_r = (lam * (x_p - x_r) - y_p) % p
    return (x_r, y_r)


def point_double(P: Point, a: int, p: int) -> Point:
    """Double a point on the elliptic curve.

    If *P* is the point at infinity or has *y = 0* the result is
    ``None``.

    Args:
        P: The point to double (or ``None``).
        a: Coefficient *a* of the curve equation.
        p: Prime modulus defining the finite field.

    Returns:
        The point ``2P`` on the curve, or ``None`` for the point at
        infinity.
    """
    if P is None:
        return None

    x_p, y_p = P

    if y_p % p == 0:
        return None

    lam = ((3 * x_p * x_p + a) * pow(2 * y_p, -1, p)) % p

    x_r = (lam * lam - 2 * x_p) % p
    y_r = (lam * (x_p - x_r) - y_p) % p
    return (x_r, y_r)


def scalar_multiply(k: int, P: Point, a: int, p: int) -> Point:
    """Compute ``k * P`` using the double-and-add algorithm.

    Args:
        k: Non-negative integer scalar.
        P: A point on the curve (or ``None``).
        a: Coefficient *a* of the curve equation.
        p: Prime modulus defining the finite field.

    Returns:
        The point ``k * P``, or ``None`` for the point at infinity.

    Raises:
        ValueError: If *k* is negative.
    """
    if k < 0:
        raise ValueError(f"Scalar k must be non-negative, got {k}.")

    if k == 0 or P is None:
        return None

    result: Point = None
    addend: Point = P

    while k > 0:
        if k & 1:
            result = point_add(result, addend, a, p)
        addend = point_double(addend, a, p)
        k >>= 1

    return result


def ecdh_shared_secret(
    private_key: int,
    public_key: Point,
    a: int,
    p: int,
) -> Point:
    """Compute the ECDH shared secret.

    The shared secret is the point ``private_key * public_key``.

    Args:
        private_key: The party's private scalar (positive integer).
        public_key: The other party's public-key point on the curve.
        a: Coefficient *a* of the curve equation.
        p: Prime modulus defining the finite field.

    Returns:
        The shared-secret point on the curve.

    Raises:
        ValueError: If *private_key* is not a positive integer.
    """
    if private_key <= 0:
        raise ValueError(
            f"Private key must be a positive integer, got {private_key}."
        )
    return scalar_multiply(private_key, public_key, a, p)
