"""
Shamir's Secret Sharing — Example

Demonstrates how a secret integer can be split into multiple shares
using Lagrange interpolation over a finite field and then
reconstructed from a subset of those shares.
"""

from ..implementation.lagrange_evaluation import (
    generate_shares,
    reconstruct_secret,
)


def main() -> None:
    secret = 42
    prime = 97  # must be greater than the secret
    num_shares = 5
    threshold = 3  # minimum shares needed to reconstruct

    print(f"Original secret : {secret}")
    print(f"Prime modulus   : {prime}")
    print(f"Total shares    : {num_shares}")
    print(f"Threshold       : {threshold}")
    print()

    shares = generate_shares(secret, num_shares, threshold, prime)
    print("Generated shares:")
    for x, y in shares:
        print(f"  Share (x={x}, y={y})")
    print()

    # Reconstruct using exactly the threshold number of shares
    subset = shares[:threshold]
    recovered = reconstruct_secret(subset, prime)
    print(f"Reconstructed secret from {threshold} shares: {recovered}")
    assert recovered == secret, "Reconstruction failed!"

    # Reconstruct using all shares
    recovered_all = reconstruct_secret(shares, prime)
    print(f"Reconstructed secret from all {num_shares} shares: {recovered_all}")
    assert recovered_all == secret, "Reconstruction failed!"

    print("\nSuccess — the secret was correctly recovered.")


if __name__ == "__main__":
    main()
