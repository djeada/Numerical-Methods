# Lagrange Evaluation for Secret Sharing

Lagrange evaluation is a technique from polynomial interpolation that finds a direct cryptographic application in **Shamir's Secret Sharing**. It allows a secret to be divided into multiple shares such that only a sufficient number of shares can reconstruct the original secret, while any smaller number of shares reveals no information about it.

## Mathematical Formulation

Given $n$ data points $(x_0, y_0), (x_1, y_1), \ldots, (x_{n-1}, y_{n-1})$, the Lagrange interpolating polynomial is:

$$
P(x) = \sum_{i=0}^{n-1} y_i \cdot L_i(x)
$$

where each **Lagrange basis polynomial** is defined as:

$$
L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n-1} \frac{x - x_j}{x_i - x_j}
$$

When working over a finite field $\mathbb{Z}_p$ (integers modulo a prime $p$), division is replaced by multiplication with the modular inverse:

$$
L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n-1} (x - x_j) \cdot (x_i - x_j)^{-1} \mod p
$$

## Shamir's Secret Sharing

Shamir's Secret Sharing uses Lagrange interpolation over a finite field to split a secret $s$ into $n$ shares with a threshold $t$:

**Share Generation:**

I. Choose a prime $p>\max(s,n)$ for an integer encoding $0\leq s<p$, and a threshold $1\leq t\leq n$.
II. Construct a random polynomial of degree **at most** $t-1$:

$$
f(x) = s + a_1 x + a_2 x^2 + \cdots + a_{t-1} x^{t-1} \mod p
$$

Choose $a_1,\ldots,a_{t-1}$ independently and uniformly from all of $\mathbb F_p$, including zero. The highest coefficient is allowed to vanish; forcing it to be nonzero changes the distribution and can compromise perfect secrecy. Coordinates $1,\ldots,n$ are distinct and nonzero modulo $p$ because $n<p$.

III. Compute $n$ shares as points on the polynomial:

$$
\text{share}_i = (i, f(i) \mod p), \quad i = 1, 2, \ldots, n
$$

**Secret Reconstruction:**

Given at least $t$ shares, reconstruct the secret by evaluating the Lagrange interpolating polynomial at $x = 0$:

$$
s = P(0) = \sum_{i=0}^{t-1} y_i \cdot L_i(0) \mod p
$$

### Why Reconstruction and Privacy Both Hold

Any $t$ shares at distinct coordinates determine a unique polynomial of degree at most $t-1$ over the field. The same Lagrange argument used over the real numbers applies because each difference $x_i-x_j$ is nonzero modulo the prime and therefore has an inverse. Evaluating that polynomial at zero returns its constant term $s$; share coordinates themselves must be nonzero, since the share at zero would reveal the secret directly.

For privacy, fix $k<t$ observed shares and consider any candidate secret $s'\in\mathbb F_p$. There are exactly $p^{t-1-k}$ coefficient vectors consistent with those shares and constant term $s'$. One way to see the count is to add the constraint $f(0)=s'$: the resulting $k+1$ distinct interpolation constraints leave $t-(k+1)$ free polynomial coefficients. Since all original coefficient vectors are equally likely, every possible secret gives the same probability $p^{-k}$ to the observed shares. Their distribution is independent of the secret.

This is information-theoretic privacy under independent uniform coefficient sampling; it is separate from whether the shares are authentic or the dealer is honest. More than $t$ consistent shares can be checked against the reconstructed polynomial, but unauthenticated corrupted shares are not automatically identified by basic interpolation. See [Shamir, How to Share a Secret](https://dspace.mit.edu/entities/publication/91c51bfc-5678-409c-80c5-44ce8fcdbadf) for the original construction.

## Algorithm Steps

**Generating Shares:**

1. Choose a prime $p$ larger than the secret $s$ and larger than $n$.
2. Generate $t - 1$ random coefficients $a_1, \ldots, a_{t-1}$ in $\mathbb{Z}_p$.
3. Define the polynomial $f(x) = s + a_1 x + \cdots + a_{t-1} x^{t-1}$.
4. For each participant $i = 1, \ldots, n$, compute the share $(i, f(i) \mod p)$.

**Reconstructing the Secret:**

1. Collect at least $t$ shares $(x_1, y_1), \ldots, (x_t, y_t)$.
2. For each share $i$, compute the Lagrange basis $L_i(0)$ in $\mathbb{Z}_p$.
3. Compute the secret as $s = \sum_{i=1}^{t} y_i \cdot L_i(0) \mod p$.

## Example

Suppose we want to share the secret $s = 42$ with $n = 5$ shares and threshold $t = 3$ using the prime $p = 97$.

**Step 1:** Construct a random polynomial of degree 2:

$$
f(x) = 42 + 15x + 23x^2 \mod 97
$$

**Step 2:** Generate 5 shares:

| Share $i$ | $f(i) \mod 97$ |
| --- | --- |
| 1 | $(42 + 15 + 23) \mod 97 = 80$ |
| 2 | $(42 + 30 + 92) \mod 97 = 67$ |
| 3 | $(42 + 45 + 207) \mod 97 = 294 \mod 97 = 3$ |
| 4 | $(42 + 60 + 368) \mod 97 = 470 \mod 97 = 82$ |
| 5 | $(42 + 75 + 575) \mod 97 = 692 \mod 97 = 13$ |

**Step 3:** Reconstruct using any 3 shares, e.g., shares 1, 3, 5:

Using Lagrange interpolation at $x = 0$, we recover $s = 42$.

For the selected coordinates $1,3,5$, the basis weights are

$$
L_1(0)=\frac{(-3)(-5)}{(1-3)(1-5)}=15\cdot8^{-1}\equiv14\pmod{97},
$$

$$
L_3(0)=\frac{(-1)(-5)}{(3-1)(3-5)}=5\cdot(-4)^{-1}\equiv23\pmod{97},
$$

$$
L_5(0)=\frac{(-1)(-3)}{(5-1)(5-3)}=3\cdot8^{-1}\equiv61\pmod{97}.
$$

Here $8^{-1}\equiv85$ and $(-4)^{-1}\equiv24$ modulo $97$. The weights sum to $98\equiv1$, and

$$
s\equiv80(14)+3(23)+13(61)=1982\equiv42\pmod{97}.
$$

The subscripts in this calculation label the selected share coordinates rather than consecutive array indices. All divisions use field inverses, and all three shares must come from the same polynomial and field.

## Advantages

- **Information-theoretic security:** Fewer than $t$ shares reveal absolutely no information about the secret, regardless of computational power.
- **Flexibility:** Shares can be distributed among any number of participants with an adjustable threshold.
- **Simplicity:** The underlying mathematics relies on polynomial interpolation, which is well understood and efficient.

## Limitations

- **Single point of failure during generation:** The dealer who creates the shares temporarily knows the secret and all shares.
- **No verifiability:** In the basic scheme, participants cannot verify that their shares are consistent (addressed by extensions like Feldman's VSS).
- **Requires a trusted dealer:** The dealer must be honest; a malicious dealer can distribute invalid shares.
- **Finite field size:** The prime $p$ must be larger than both the secret and the number of shares.
