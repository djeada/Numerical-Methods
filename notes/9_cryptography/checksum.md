## Checksum Algorithms

Checksum algorithms are methods for computing a small, fixed-size value from a block of data. They serve as a simple mechanism to detect accidental changes or corruption in data during transmission or storage. While not cryptographically secure, checksums are fundamental to error detection in digital systems.

### Luhn Algorithm

The Luhn algorithm (also known as the "modulus 10" algorithm) is a checksum formula used to validate identification numbers such as credit card numbers, IMEI numbers, and national identification numbers.

#### Mathematical Formulation

Given a number string $d_1 d_2 \ldots d_n$:

I. Starting from the rightmost digit (the check digit), double every second digit.
II. If a doubled digit exceeds 9, subtract 9.
III. Sum all the resulting digits.
IV. The number is valid if the total modulo 10 is zero.

For computing a check digit for payload $d_1 d_2 \ldots d_{n-1}$:

$$\text{check digit} = (10 - (S \mod 10)) \mod 10$$

where $S$ is the Luhn sum of the payload digits.

#### Example

Validate the number 79927398713:

| Position (from right) | Digit | Action | Result |
|----------------------|-------|--------|--------|
| 1 | 3 | Keep | 3 |
| 2 | 1 | Double: $1 \times 2 = 2$ | 2 |
| 3 | 7 | Keep | 7 |
| 4 | 8 | Double: $8 \times 2 = 16 - 9 = 7$ | 7 |
| 5 | 9 | Keep | 9 |
| 6 | 3 | Double: $3 \times 2 = 6$ | 6 |
| 7 | 7 | Keep | 7 |
| 8 | 2 | Double: $2 \times 2 = 4$ | 4 |
| 9 | 9 | Keep | 9 |
| 10 | 9 | Double: $9 \times 2 = 18 - 9 = 9$ | 9 |
| 11 | 7 | Keep | 7 |

Sum = $3 + 2 + 7 + 7 + 9 + 6 + 7 + 4 + 9 + 9 + 7 = 70$

Since $70 \mod 10 = 0$, the number is valid.

### CRC-32

The Cyclic Redundancy Check (CRC-32) is a widely used error-detection algorithm based on polynomial division over $\text{GF}(2)$ (the Galois field with two elements).

#### Mathematical Formulation

A message $M(x)$ is treated as a polynomial over $\text{GF}(2)$. The CRC is computed as:

$$\text{CRC} = M(x) \cdot x^{32} \mod G(x)$$

where $G(x)$ is the generator polynomial. The standard CRC-32 generator is:

$$G(x) = x^{32} + x^{26} + x^{23} + x^{22} + x^{16} + x^{12} + x^{11} + x^{10} + x^8 + x^7 + x^5 + x^4 + x^2 + x + 1$$

In the reflected (LSB-first) implementation, the polynomial constant is $\texttt{0xEDB88320}$.

#### Algorithm Steps

1. Initialize a 32-bit CRC register to $\texttt{0xFFFFFFFF}$.
2. For each byte of input, XOR it with the low byte of the CRC register.
3. For each of the 8 bits, if the LSB is 1, shift right and XOR with the polynomial; otherwise, just shift right.
4. After processing all bytes, XOR the CRC register with $\texttt{0xFFFFFFFF}$.

### Fletcher-16

The Fletcher checksum is a position-dependent checksum that uses two running sums to detect both value and positional errors.

#### Mathematical Formulation

Given a byte sequence $b_1, b_2, \ldots, b_n$:

$$S_1 = \sum_{i=1}^{n} b_i \mod 255$$

$$S_2 = \sum_{i=1}^{n} S_1^{(i)} \mod 255$$

where $S_1^{(i)}$ is the value of $S_1$ after processing byte $i$.

The Fletcher-16 checksum is:

$$\text{Fletcher-16} = S_2 \cdot 256 + S_1$$

### Adler-32

Adler-32 is a checksum algorithm similar to Fletcher but uses modulus 65521 (the largest prime less than $2^{16}$) for better distribution properties.

#### Mathematical Formulation

Given a byte sequence $b_1, b_2, \ldots, b_n$:

$$A = 1 + \sum_{i=1}^{n} b_i \mod 65521$$

$$B = \sum_{i=1}^{n} A^{(i)} \mod 65521$$

The Adler-32 checksum is:

$$\text{Adler-32} = B \cdot 65536 + A$$

#### Example

Compute Adler-32 for the ASCII string "Wikipedia":

Starting with $A = 1$, $B = 0$:

| Character | ASCII | A (mod 65521) | B (mod 65521) |
|-----------|-------|---------------|---------------|
| W | 87 | 88 | 88 |
| i | 105 | 193 | 281 |
| k | 107 | 300 | 581 |
| i | 105 | 405 | 986 |
| p | 112 | 517 | 1503 |
| e | 101 | 618 | 2121 |
| d | 100 | 718 | 2839 |
| i | 105 | 823 | 3662 |
| a | 97 | 920 | 4582 |

$$\text{Adler-32} = 4582 \times 65536 + 920 = \texttt{0x11E60398}$$

### Advantages

- **Speed:** Checksum algorithms are computationally inexpensive and suitable for real-time verification.
- **Simplicity:** Implementations are straightforward and require minimal resources.
- **Wide adoption:** CRC-32 and Luhn are industry standards used in networking protocols, storage systems, and financial systems.
- **Position sensitivity:** Fletcher and Adler checksums detect reordering errors that simpler sum-based methods miss.

### Limitations

- **Not cryptographically secure:** Checksums are designed for error detection, not for security. An adversary can easily craft data with a desired checksum.
- **Limited error detection:** Simple checksums may fail to detect certain patterns of multi-bit errors.
- **No error correction:** Checksums can only detect errors, not correct them (unlike error-correcting codes such as Reed–Solomon).
- **Collision probability:** As fixed-size outputs, checksums inherently have collisions where different inputs produce the same value.
