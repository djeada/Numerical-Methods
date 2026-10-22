# Checksum Algorithms

Checksum algorithms are methods for computing a small, fixed-size value from a block of data. They serve as a simple mechanism to detect accidental changes or corruption in data during transmission or storage. While not cryptographically secure, checksums are fundamental to error detection in digital systems.

## Comparing the checksum conventions

| Algorithm | Input representation | Initial state | Main arithmetic |
| --- | --- | --- | --- |
| Luhn | Decimal digits, including a check-digit position | Sum starts at zero | Alternating digit transform and a sum modulo $10$ |
| CRC-32, reflected convention below | Bytes processed bit by bit | Register `0xFFFFFFFF` | Shifts and XOR, followed by a final XOR |
| Fletcher-16 | Bytes | $S_1=S_2=0$ | Two running sums modulo $255$ |
| Adler-32 | Bytes | $A=1$, $B=0$ | Two running sums modulo $65521$ |

The input representation and initialization are part of the algorithm. The same visible text can produce a different result if it is encoded into different bytes, and a different CRC convention can produce a different checksum even when it uses the same generator polynomial.

## Luhn algorithm

The Luhn algorithm (also known as the "modulus 10" algorithm) is a checksum formula used to validate identification numbers such as credit card numbers, IMEI numbers, and national identification numbers.

### Mathematical formulation

Given a number string $d_1 d_2 \ldots d_n$:

I. Starting from the rightmost digit (the check digit), double every second digit.
II. If a doubled digit exceeds 9, subtract 9.
III. Sum all the resulting digits.
IV. The number is valid if the total modulo 10 is zero.

For computing a check digit for payload $d_1 d_2 \ldots d_{n-1}$:

$$
\text{check digit} = (10 - (S \mod 10)) \mod 10
$$

where $S$ is the Luhn sum of the payload digits.

### Check-digit parity and detection limits

For validation, the rightmost check digit is kept unchanged, and doubling starts at the next digit to its left. For generation, reserve that final position first: equivalently, append a zero placeholder and compute the transformed payload sum $S$. Applying the validation parity directly to the unextended payload would double the wrong positions.

The doubled-digit transform is $T(d)=2d$ for $d<5$ and $T(d)=2d-9$ for $d\geq5$. Subtracting nine is the same as adding the two decimal digits of a doubled value between $10$ and $18$. The check digit $c=(-S)\bmod10$ then makes $S+c$ divisible by ten. For payload `7992739871`, the transformed sum is $67$, so $c=3$ and the completed number is `79927398713`.

Luhn detects every single-digit substitution but not every adjacent transposition: swapping `09` and `90` can preserve the sum. Passing the check establishes consistency with the checksum, not that an identification number is issued, active, or authentic.

### Example

Validate the number 79927398713:

| Position (from right) | Digit | Action | Result |
| --- | --- | --- | --- |
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

## CRC-32

The Cyclic Redundancy Check (CRC-32) is a widely used error-detection algorithm based on polynomial division over $\text{GF}(2)$ (the Galois field with two elements).

### Mathematical formulation

A message bit string is treated as a polynomial $M(x)$ over $\operatorname{GF}(2)$. In the basic zero-initialized polynomial construction, the raw remainder is:

$$
R(x) = M(x)x^{32}\bmod G(x)
$$

where $G(x)$ is the generator polynomial. The standard CRC-32 generator is:

$$
G(x) = x^{32} + x^{26} + x^{23} + x^{22} + x^{16} + x^{12} + x^{11} + x^{10} + x^8 +
x^7 + x^5 + x^4 + x^2 + x + 1
$$

In the reflected (LSB-first) implementation, the polynomial constant is $\texttt{0xEDB88320}$.

### Algorithm steps

1. Initialize a 32-bit CRC register to $\texttt{0xFFFFFFFF}$.
2. For each byte of input, XOR it with the low byte of the CRC register.
3. For each of the 8 bits, if the LSB is 1, shift right and XOR with the polynomial; otherwise, just shift right.
4. After processing all bytes, XOR the CRC register with $\texttt{0xFFFFFFFF}$.

### Connecting the polynomial and register views

Over $\operatorname{GF}(2)$, coefficients are bits and subtraction is XOR. Multiplication by $x$ shifts a bit pattern; polynomial long division removes a leading term by XORing a shifted copy of the generator. In the basic construction, appending the remainder produces $C(x)=M(x)x^{32}+R(x)$, which is divisible by $G(x)$ because addition and subtraction coincide.

The common reflected CRC-32 convention described by the register steps also specifies an all-ones initial register, bit reflection, and a final all-ones XOR. Those conventions modify the raw polynomial construction; the raw expression alone does not fully specify the reported checksum. With the leading $x^{32}$ coefficient omitted, the ordinary polynomial constant is `0x04C11DB7`; the reflected shift-right constant is `0xEDB88320`.

A useful check vector for these conventions is the ASCII byte string `123456789`, whose CRC-32 is `0xCBF43926`. The empty byte string gives zero. Byte order when storing that integer is another format choice, separate from bit reflection. [RFC 1952](https://www.rfc-editor.org/rfc/rfc1952) specifies the gzip CRC-32 convention and gives sample update code.

## Fletcher-16

The Fletcher checksum is a position-dependent checksum that uses two running sums to detect both value and positional errors.

### Mathematical formulation

Given a byte sequence $b_1, b_2, \ldots, b_n$:

$$
S_1 = \sum_{i=1}^{n} b_i \mod 255
$$

$$
S_2 = \sum_{i=1}^{n} S_1^{(i)} \mod 255
$$

where $S_1^{(i)}$ is the value of $S_1$ after processing byte $i$.

The Fletcher-16 checksum is:

$$
\text{Fletcher-16} = S_2 \cdot 256 + S_1
$$

Initialize both sums to zero and update $S_1\leftarrow(S_1+b_i)\bmod255$, then $S_2\leftarrow(S_2+S_1)\bmod255$ for each byte. Expanding the nested sum shows

$$
S_2=\sum_{i=1}^n(n-i+1)b_i\bmod255.
$$

Earlier bytes contribute to more running sums, which makes the result position-sensitive. For bytes $(1,2,3)$, the successive first sums are $1,3,6$, giving $S_1=6$, $S_2=10$, and checksum `0x0A06`. Reordering the last two bytes changes $S_2$ to $11$, although other changes can cancel modulo $255$ and escape detection.

## Adler-32

Adler-32 is a checksum algorithm similar to Fletcher but uses modulus 65521 (the largest prime less than $2^{16}$) for better distribution properties.

### Mathematical formulation

Given a byte sequence $b_1, b_2, \ldots, b_n$:

$$
A = \left(1 + \sum_{i=1}^{n} b_i\right)\bmod65521
$$

$$
B = \sum_{i=1}^{n} A^{(i)} \mod 65521
$$

The Adler-32 checksum is:

$$
\text{Adler-32} = B \cdot 65536 + A
$$

Initialize $A=1$ and $B=0$. After each byte, update $A\leftarrow(A+b_i)\bmod65521$, followed by $B\leftarrow(B+A)\bmod65521$. Thus $B=[n+\sum_i(n-i+1)b_i]\bmod65521$; the extra $n$ comes from the initial value of $A$. The empty input has Adler-32 value $1$. The byte encoding matters: a checksum operates on bytes, not abstract characters. [RFC 1950](https://www.rfc-editor.org/rfc/rfc1950) defines these initialization and update conventions.

### Example

Compute Adler-32 for the ASCII string "Wikipedia":

Starting with $A = 1$, $B = 0$:

| Character | ASCII | A (mod 65521) | B (mod 65521) |
| --- | --- | --- | --- |
| W | 87 | 88 | 88 |
| i | 105 | 193 | 281 |
| k | 107 | 300 | 581 |
| i | 105 | 405 | 986 |
| p | 112 | 517 | 1503 |
| e | 101 | 618 | 2121 |
| d | 100 | 718 | 2839 |
| i | 105 | 823 | 3662 |
| a | 97 | 920 | 4582 |

$$
\text{Adler-32} = 4582 \times 65536 + 920 = \texttt{0x11E60398}
$$

## Advantages

- **Speed:** Checksum algorithms are computationally inexpensive and suitable for real-time verification.
- **Simplicity:** Implementations are straightforward and require minimal resources.
- **Wide adoption:** CRC-32 and Luhn are industry standards used in networking protocols, storage systems, and financial systems.
- **Position sensitivity:** Fletcher and Adler checksums detect many reordering errors that a simple sum misses, because their second accumulators weight positions differently. They do not detect every possible reordering or correlated change.

## Limitations

- **Not cryptographically secure:** Checksums are designed for error detection, not for security. An adversary can easily craft data with a desired checksum.
- **Limited error detection:** Simple checksums may fail to detect certain patterns of multi-bit errors.
- **No error correction:** Checksums can only detect errors, not correct them (unlike error-correcting codes such as Reed–Solomon).
- **Collision probability:** As fixed-size outputs, checksums inherently have collisions where different inputs produce the same value.
