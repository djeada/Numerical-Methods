# Elliptic Curves

Elliptic curve cryptography (ECC) is a public-key cryptographic approach based on the algebraic structure of elliptic curves over finite fields. The security of ECC relies on the difficulty of the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**, which makes it possible to achieve strong security with smaller key sizes compared to RSA.

## Mathematical formulation

An elliptic curve over a prime finite field $\mathbb{F}_p$ (where $p > 3$) is defined by the short Weierstrass equation:

$$
y^2 \equiv x^3 + ax + b \pmod{p}
$$

where $a, b \in \mathbb{F}_p$ and the curve is **non-singular**, meaning the discriminant is nonzero:

$$
4a^3 + 27b^2 \not\equiv 0 \pmod{p}
$$

The assumption $p>3$ lets a general nonsingular Weierstrass equation be transformed to this short form by changes of variables that divide by $2$ and $3$. In characteristic $2$ or $3$, those transformations are unavailable in general and other forms are used; some particular curves can still have a short equation, so the restriction concerns the general formulation supported here. The implementation rejects $p\leq3$ and singular curves. Primality of $p$ is assumed, not tested, and modular inverses rely on that assumption.

The set of points on the curve, together with a special **point at infinity** $\mathcal{O}$, forms an abelian group under point addition.

### Keeping the two moduli distinct

| Symbol | Meaning | Arithmetic role |
| --- | --- | --- |
| $p$ | Prime defining the coordinate field $\mathbb F_p$ | Reduce point coordinates and slope calculations modulo $p$ |
| $G$ | Chosen base point | Generates the subgroup used in the example or protocol |
| $n$ | Order of $G$, so $nG=\mathcal O$ | Scalars acting on $G$ repeat modulo $n$ |
| $\mathcal O$ | Point at infinity | Identity of the point-addition group |
| $\lambda$ | Slope used by the addition or doubling formula | A field element, computed using inverses modulo $p$ |

The field modulus and subgroup order need not be equal. In particular, reducing a point coordinate modulo $n$ would not be the same operation as reducing a scalar multiple of $G$ modulo its order. The small worked example later makes both moduli visible.

## Point addition

Given two distinct points $P = (x_P, y_P)$ and $Q = (x_Q, y_Q)$ on the curve with $P \neq -Q$, their sum $R = P + Q = (x_R, y_R)$ is computed as:

$$
\lambda = \frac{y_Q - y_P}{x_Q - x_P} \mod p
$$

$$
x_R = \lambda^2 - x_P - x_Q \mod p
$$

$$
y_R = \lambda(x_P - x_R) - y_P \mod p
$$

Special cases:

- $P + \mathcal{O} = P$ (identity element).
- $P + (-P) = \mathcal{O}$, where $-P = (x_P, -y_P \mod p)$.

### Division means a modular inverse

All coordinates and slope calculations take place in $\mathbb F_p$, not in floating point arithmetic. For a nonzero denominator $d$, division means multiplication by $d^{-1}\bmod p$, where $dd^{-1}\equiv1\pmod p$. The inverse exists because $p$ is prime. Extended Euclid computes it; Fermat's identity $d^{p-2}\equiv d^{-1}\pmod p$ is another mathematical formula.

To derive the addition coordinates, write the line through $P$ and $Q$ as $y=\lambda(x-x_P)+y_P$ and substitute it into the curve equation. The resulting cubic has roots $x_P$, $x_Q$, and the third intersection coordinate $x_T$. Its $x^2$ coefficient gives $x_P+x_Q+x_T=\lambda^2$. Thus $x_T=\lambda^2-x_P-x_Q$. Reflecting the third intersection across the horizontal axis gives $P+Q$, yielding the stated $y_R$ formula. This algebraic construction remains valid over the finite field even though a real-plane drawing is only an analogy.

If $x_P=x_Q$, do not attempt to invert a zero denominator: use doubling when $P=Q$ and $y_P\ne0$, or return $\mathcal O$ for opposite points. These cases make the group law complete as a mathematical definition.

## Point doubling

When $P = Q$ (and $y_P \neq 0$), the tangent line formula gives:

$$
\lambda = \frac{3x_P^2 + a}{2y_P} \mod p
$$

$$
x_R = \lambda^2 - 2x_P \mod p
$$

$$
y_R = \lambda(x_P - x_R) - y_P \mod p
$$

If $y_P = 0$, then $2P = \mathcal{O}$.

### A doubling calculation

For the later example curve and $P=(3,6)$, the numerator is $3(3)^2+2=29$ and the denominator is $12$. Since $12^{-1}\equiv89\pmod{97}$,

$$
\lambda\equiv29\cdot89\equiv59\pmod{97},
$$

$$
x_{2P}\equiv59^2-6\equiv80\pmod{97},\qquad y_{2P}\equiv59(3-80)-6\equiv10\pmod{97}.
$$

Therefore $2P=(80,10)$. Every reduction is performed modulo $97$; ordinary division would give unrelated coordinates.

## Scalar multiplication

Scalar multiplication computes $kP = P + P + \cdots + P$ ($k$ times) efficiently using the **double-and-add** algorithm:

1. Initialize $R = \mathcal{O}$ (point at infinity) and $T = P$.
2. For each bit of $k$ from the least significant to the most significant:
   - If the current bit is 1: Add: $R = R + T$.
   - Double: $T = 2T$.
3. Return $R$.

(The equivalent most-significant-bit-first variant doubles $R$ and then conditionally adds $P$; the implementation uses the form above.)

This runs in $O(\log k)$ point operations, making it efficient even for large scalars.

For this operation count, take $k>0$; $0P=\mathcal O$, and negative scalars can be handled using $(-k)P=-(kP)$. The least-significant-bit algorithm doubles the current power-of-two multiple $T$ and adds it to $R$ exactly when that power appears in the binary expansion of $k$. A basic branch-based implementation illustrates the group arithmetic but does not automatically have constant-time behavior.

## Input validation

The group-law functions only need the coefficient $a$, so they cannot check the curve or the points by default. Passing the optional keyword `b` to `point_add`, `point_double`, `scalar_multiply` or `ecdh_shared_secret` makes them verify that the curve is non-singular and that every supplied point satisfies the curve equation, raising `ValueError` otherwise. Checking the curve equation rejects off-curve inputs, but it is only part of public-key validation. For a subgroup of known order $n$, full validation also checks the field encoding, rejects the identity, and verifies the required subgroup membership, for example $nQ=\mathcal O$ in a prime-order subgroup. The optional `b` check alone does not establish all of these properties. All of these functions always reject $p \le 3$.

## Elliptic curve diffie–hellman (ECDH)

ECDH is a key-agreement protocol that allows two parties to establish a shared secret over an insecure channel:

**Setup:** Agree on curve parameters $(a, b, p)$ and a base point $G$ of order $n$.

For a prime-order subgroup, choose private scalars uniformly from $1,\ldots,n-1$. The order $n$ is the smallest positive integer with $nG=\mathcal O$; it is distinct from the field modulus $p$, which governs coordinate arithmetic.

**Key Exchange:**

I. Alice chooses a private key $d_A$ and computes her public key $Q_A = d_A \cdot G$.
II. Bob chooses a private key $d_B$ and computes his public key $Q_B = d_B \cdot G$.
III. Alice computes the shared secret $S = d_A \cdot Q_B = d_A \cdot d_B \cdot G$.
IV. Bob computes the shared secret $S = d_B \cdot Q_A = d_B \cdot d_A \cdot G$.

Both arrive at the same point because $d_A(d_BG)=(d_Ad_B)G=(d_Bd_A)G=d_B(d_AG)$. A complete key-agreement protocol validates peer keys, authenticates the exchange, and derives symmetric key material from the shared result with an appropriate key-derivation function. Bare ECDH supplies the algebraic shared secret, but does not authenticate who supplied the public key. [NIST SP 800-56A Rev. 3](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) describes the key-establishment and validation requirements.

## Example

Consider the curve $y^2 \equiv x^3 + 2x + 3 \pmod{97}$.

**Verify non-singularity:** $4(2)^3 + 27(3)^2 = 32 + 243 = 275 \equiv 275 \mod 97 = 81 \neq 0$ ✓

**Point verification:** Check that $P = (3, 6)$ lies on the curve:

$$
6^2 = 36 \quad \text{and} \quad 3^3 + 2(3) + 3 = 27 + 6 + 3 = 36
$$

$$
36 \equiv 36 \pmod{97} \quad \checkmark
$$

**ECDH example** with base point $G = (3, 6)$:

- Alice picks $d_A = 7$, computes $Q_A = 7G$.
- Bob picks $d_B = 11$, computes $Q_B = 11G$.
- Shared secret: $S = 7 \cdot Q_B = 11 \cdot Q_A = 77G$.

For this small base point, repeated addition gives $2G=(80,10)$, $3G=(80,87)$, $4G=(3,91)$, and $5G=\mathcal O$. Thus its order is only $n=5$, and scalars reduce modulo five: $Q_A=7G=2G=(80,10)$, $Q_B=11G=G=(3,6)$, and $S=77G=2G=(80,10)$. The displayed integers $7$ and $11$ illustrate scalar reduction; private-key sampling in a subgroup of order five would use $1,2,3,4$. This toy subgroup makes the arithmetic inspectable and has no cryptographic security.

## Advantages

- **Small key sizes:** An appropriately chosen 256-bit elliptic-curve group and a 3072-bit RSA modulus are commonly compared at roughly 128-bit classical security. This is an estimated classical work-factor comparison, not a claim that the keys have equal bit lengths or that every ECC operation is faster. Smaller public representations can reduce bandwidth.
- **Efficiency:** Point operations on elliptic curves are computationally efficient, making ECC well-suited for constrained devices (smart cards, IoT).
- **Classical security assumption:** For suitable prime-order elliptic-curve groups, the best known generic classical discrete-logarithm attacks take roughly the square root of the subgroup order in group operations. Security depends on the chosen curve, subgroup, protocol, and implementation; comparing different problems solely by key bit length does not establish that one is universally harder.
- **Widely adopted standards:** ECC is used in TLS, SSH, Bitcoin, and many other protocols.

## Limitations

- **Implementation complexity:** Correct and secure implementation of ECC requires careful handling of side-channel attacks, invalid curve attacks, and point validation.
- **Patent history:** Early ECC algorithms were encumbered by patents (now mostly expired), which historically slowed adoption.
- **Quantum vulnerability:** Like RSA, conventional ECC is vulnerable to a sufficiently capable quantum computer running Shor's algorithm. Increasing the elliptic-curve key size does not make the underlying problem post-quantum secure; quantum-resistant schemes use different hardness assumptions. See [Proos and Zalka, Shor's discrete logarithm quantum algorithm for elliptic curves](https://arxiv.org/abs/quant-ph/0301141) for the algorithmic basis.
- **Parameter selection:** Choosing secure curve parameters is critical; poorly chosen curves can have exploitable weaknesses.
