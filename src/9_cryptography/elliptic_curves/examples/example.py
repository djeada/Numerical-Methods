"""
Elliptic Curve Arithmetic — Example

Demonstrates point addition, point doubling, scalar multiplication,
and an ECDH key exchange on the curve y² = x³ + 2x + 3 (mod 97).
"""

from ..implementation.elliptic_curves import (
    is_on_curve,
    point_add,
    point_double,
    scalar_multiply,
    ecdh_shared_secret,
)


def main() -> None:
    # Curve parameters: y² = x³ + 2x + 3 (mod 97)
    a, b, p = 2, 3, 97
    G = (0, 10)  # generator point of order 50

    print("Elliptic Curve: y² = x³ + 2x + 3 (mod 97)")
    print(f"Generator G = {G}")
    print(f"G on curve:  {is_on_curve(G, a, b, p)}")
    print()

    # --- Point doubling ---
    two_G = point_double(G, a, p)
    print(f"2G = {two_G}")

    # --- Point addition ---
    Q = (1, 43)
    R = point_add(G, Q, a, p)
    print(f"G + {Q} = {R}")
    print()

    # --- Scalar multiplication ---
    for k in range(1, 6):
        kG = scalar_multiply(k, G, a, p)
        print(f"{k}G = {kG}")
    print()

    # --- ECDH key exchange ---
    alice_private = 7
    bob_private = 11

    alice_public = scalar_multiply(alice_private, G, a, p)
    bob_public = scalar_multiply(bob_private, G, a, p)

    print("ECDH Key Exchange")
    print(f"  Alice private key : {alice_private}")
    print(f"  Alice public key  : {alice_public}")
    print(f"  Bob private key   : {bob_private}")
    print(f"  Bob public key    : {bob_public}")

    shared_alice = ecdh_shared_secret(alice_private, bob_public, a, p)
    shared_bob = ecdh_shared_secret(bob_private, alice_public, a, p)

    print(f"  Alice shared secret: {shared_alice}")
    print(f"  Bob shared secret  : {shared_bob}")
    print(f"  Secrets match: {shared_alice == shared_bob}")


if __name__ == "__main__":
    main()
