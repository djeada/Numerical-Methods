## Lagrange Evaluation for Secret Sharing

Lagrange evaluation is a technique from polynomial interpolation that finds a direct cryptographic application in **Shamir's Secret Sharing**. It allows a secret to be divided into multiple shares such that only a sufficient number of shares can reconstruct the original secret, while any smaller number of shares reveals no information about it.

### Mathematical Formulation

Given $n$ data points $(x_0, y_0), (x_1, y_1), \ldots, (x_{n-1}, y_{n-1})$, the Lagrange interpolating polynomial is:

$$P(x) = \sum_{i=0}^{n-1} y_i \cdot L_i(x)$$

where each **Lagrange basis polynomial** is defined as:

$$L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n-1} \frac{x - x_j}{x_i - x_j}$$

When working over a finite field $\mathbb{Z}_p$ (integers modulo a prime $p$), division is replaced by multiplication with the modular inverse:

$$L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n-1} (x - x_j) \cdot (x_i - x_j)^{-1} \mod p$$

### Shamir's Secret Sharing

Shamir's Secret Sharing uses Lagrange interpolation over a finite field to split a secret $s$ into $n$ shares with a threshold $t$:

**Share Generation:**

I. Choose a prime $p > s$.
II. Construct a random polynomial of degree $t - 1$:

$$f(x) = s + a_1 x + a_2 x^2 + \cdots + a_{t-1} x^{t-1} \mod p$$

where $a_1, a_2, \ldots, a_{t-1}$ are random integers from $\mathbb{Z}_p$.

III. Compute $n$ shares as points on the polynomial:

$$\text{share}_i = (i, f(i) \mod p), \quad i = 1, 2, \ldots, n$$

**Secret Reconstruction:**

Given at least $t$ shares, reconstruct the secret by evaluating the Lagrange interpolating polynomial at $x = 0$:

$$s = P(0) = \sum_{i=0}^{t-1} y_i \cdot L_i(0) \mod p$$

### Algorithm Steps

**Generating Shares:**

1. Choose a prime $p$ larger than the secret $s$ and larger than $n$.
2. Generate $t - 1$ random coefficients $a_1, \ldots, a_{t-1}$ in $\mathbb{Z}_p$.
3. Define the polynomial $f(x) = s + a_1 x + \cdots + a_{t-1} x^{t-1}$.
4. For each participant $i = 1, \ldots, n$, compute the share $(i, f(i) \mod p)$.

**Reconstructing the Secret:**

1. Collect at least $t$ shares $(x_1, y_1), \ldots, (x_t, y_t)$.
2. For each share $i$, compute the Lagrange basis $L_i(0)$ in $\mathbb{Z}_p$.
3. Compute the secret as $s = \sum_{i=1}^{t} y_i \cdot L_i(0) \mod p$.

### Example

Suppose we want to share the secret $s = 42$ with $n = 5$ shares and threshold $t = 3$ using the prime $p = 97$.

**Step 1:** Construct a random polynomial of degree 2:

$$f(x) = 42 + 15x + 23x^2 \mod 97$$

**Step 2:** Generate 5 shares:

| Share $i$ | $f(i) \mod 97$ |
|-----------|-----------------|
| 1 | $(42 + 15 + 23) \mod 97 = 80$ |
| 2 | $(42 + 30 + 92) \mod 97 = 67$ |
| 3 | $(42 + 45 + 207) \mod 97 = 294 \mod 97 = 3$ |
| 4 | $(42 + 60 + 368) \mod 97 = 470 \mod 97 = 82$ |
| 5 | $(42 + 75 + 575) \mod 97 = 692 \mod 97 = 13$ |

**Step 3:** Reconstruct using any 3 shares, e.g., shares 1, 3, 5:

Using Lagrange interpolation at $x = 0$, we recover $s = 42$.

### Advantages

- **Information-theoretic security:** Fewer than $t$ shares reveal absolutely no information about the secret, regardless of computational power.
- **Flexibility:** Shares can be distributed among any number of participants with an adjustable threshold.
- **Simplicity:** The underlying mathematics relies on polynomial interpolation, which is well understood and efficient.

### Limitations

- **Single point of failure during generation:** The dealer who creates the shares temporarily knows the secret and all shares.
- **No verifiability:** In the basic scheme, participants cannot verify that their shares are consistent (addressed by extensions like Feldman's VSS).
- **Requires a trusted dealer:** The dealer must be honest; a malicious dealer can distribute invalid shares.
- **Finite field size:** The prime $p$ must be larger than both the secret and the number of shares.
