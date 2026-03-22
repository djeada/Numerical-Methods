## Elliptic Curves

Elliptic curve cryptography (ECC) is a public-key cryptographic approach based on the algebraic structure of elliptic curves over finite fields. The security of ECC relies on the difficulty of the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**, which makes it possible to achieve strong security with smaller key sizes compared to RSA.

### Mathematical Formulation

An elliptic curve over a prime finite field $\mathbb{F}_p$ (where $p > 3$) is defined by the short Weierstrass equation:

$$y^2 \equiv x^3 + ax + b \pmod{p}$$

where $a, b \in \mathbb{F}_p$ and the curve is **non-singular**, meaning the discriminant is nonzero:

$$4a^3 + 27b^2 \not\equiv 0 \pmod{p}$$

The set of points on the curve, together with a special **point at infinity** $\mathcal{O}$, forms an abelian group under point addition.

### Point Addition

Given two distinct points $P = (x_P, y_P)$ and $Q = (x_Q, y_Q)$ on the curve with $P \neq -Q$, their sum $R = P + Q = (x_R, y_R)$ is computed as:

$$\lambda = \frac{y_Q - y_P}{x_Q - x_P} \mod p$$

$$x_R = \lambda^2 - x_P - x_Q \mod p$$

$$y_R = \lambda(x_P - x_R) - y_P \mod p$$

Special cases:

- $P + \mathcal{O} = P$ (identity element).
- $P + (-P) = \mathcal{O}$, where $-P = (x_P, -y_P \mod p)$.

### Point Doubling

When $P = Q$ (and $y_P \neq 0$), the tangent line formula gives:

$$\lambda = \frac{3x_P^2 + a}{2y_P} \mod p$$

$$x_R = \lambda^2 - 2x_P \mod p$$

$$y_R = \lambda(x_P - x_R) - y_P \mod p$$

If $y_P = 0$, then $2P = \mathcal{O}$.

### Scalar Multiplication

Scalar multiplication computes $kP = P + P + \cdots + P$ ($k$ times) efficiently using the **double-and-add** algorithm:

1. Initialize $R = \mathcal{O}$ (point at infinity).
2. For each bit of $k$ from the most significant to the least significant:
   - Double: $R = 2R$.
   - If the current bit is 1: Add: $R = R + P$.
3. Return $R$.

This runs in $O(\log k)$ point operations, making it efficient even for large scalars.

### Elliptic Curve Diffie–Hellman (ECDH)

ECDH is a key-agreement protocol that allows two parties to establish a shared secret over an insecure channel:

**Setup:** Agree on curve parameters $(a, b, p)$ and a base point $G$ of order $n$.

**Key Exchange:**

I. Alice chooses a private key $d_A$ and computes her public key $Q_A = d_A \cdot G$.
II. Bob chooses a private key $d_B$ and computes his public key $Q_B = d_B \cdot G$.
III. Alice computes the shared secret $S = d_A \cdot Q_B = d_A \cdot d_B \cdot G$.
IV. Bob computes the shared secret $S = d_B \cdot Q_A = d_B \cdot d_A \cdot G$.

Both arrive at the same point $S$ due to the commutativity of scalar multiplication.

### Example

Consider the curve $y^2 \equiv x^3 + 2x + 3 \pmod{97}$.

**Verify non-singularity:** $4(2)^3 + 27(3)^2 = 32 + 243 = 275 \equiv 275 \mod 97 = 81 \neq 0$ ✓

**Point verification:** Check that $P = (3, 6)$ lies on the curve:

$$6^2 = 36 \quad \text{and} \quad 3^3 + 2(3) + 3 = 27 + 6 + 3 = 36$$

$$36 \equiv 36 \pmod{97} \quad \checkmark$$

**ECDH example** with base point $G = (3, 6)$:

- Alice picks $d_A = 7$, computes $Q_A = 7G$.
- Bob picks $d_B = 11$, computes $Q_B = 11G$.
- Shared secret: $S = 7 \cdot Q_B = 11 \cdot Q_A = 77G$.

### Advantages

- **Small key sizes:** A 256-bit ECC key provides comparable security to a 3072-bit RSA key, resulting in faster computations and lower bandwidth.
- **Efficiency:** Point operations on elliptic curves are computationally efficient, making ECC well-suited for constrained devices (smart cards, IoT).
- **Strong security guarantees:** The ECDLP is believed to be harder than integer factorization or the discrete logarithm problem in $\mathbb{Z}_p^*$ for equivalent key sizes.
- **Widely adopted standards:** ECC is used in TLS, SSH, Bitcoin, and many other protocols.

### Limitations

- **Implementation complexity:** Correct and secure implementation of ECC requires careful handling of side-channel attacks, invalid curve attacks, and point validation.
- **Patent history:** Early ECC algorithms were encumbered by patents (now mostly expired), which historically slowed adoption.
- **Quantum vulnerability:** Like RSA, ECC is vulnerable to quantum computers running Shor's algorithm, though larger key sizes are needed for equivalent quantum resistance.
- **Parameter selection:** Choosing secure curve parameters is critical; poorly chosen curves can have exploitable weaknesses.
