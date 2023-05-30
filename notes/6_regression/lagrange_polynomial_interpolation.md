### Lagrange Polynomial Interpolation

Lagrange polynomial interpolation gives us a single polynomial that connects all of the data points.

That polynomial is denoted as $L(x)$. It is true that $L(x_i) = y_i$ for all points $(x_i, y_i)$ .

$$L(x) = \sum_{i = 1}^n y_i P_i(x).$$

Each polynomial appearing in the sum is called a Lagrange basis polynomials, $P_i(x)$.

$$P_i(x) = \prod_{j = 1, j\ne i}^n\frac{x - x_j}{x_i - x_j},$$

### Example

We are given three points A(-1, 1), B(2, 3) and C(3,5).\\

$$P_1(x) = \frac{(x - x_2)(x - x_3)}{(x_1-x_2)(x_1-x_3)} = \frac{(x - 2)(x - 3)}{(-1-2)(-1-3)} = \frac{1}{12}(x^2 - 5x + 6)$$

$$P_2(x) = \frac{(x - x_1)(x - x_3)}{(x_2-x_1)(x_2-x_3)} = \frac{(x + 1)(x - 3)}{(2 + 1)(2-3)} = -\frac{1}{3}(x^2 - 2x - 3)$$

$$P_3(x) = \frac{(x - x_1)(x - x_2)}{(x_3-x_1)(x_3-x_2)} = \frac{(x + 1)(x - 2)}{(3 + 1)(3-2)} =\frac{1}{4}(x^2 -x - 2)$$

$$ L(x) = 1 \cdot P_1(x) + 3 \cdot P_2(x) + 5 \cdot P_3(x) $$

$$ L(x) = 1 \cdot P_1(x) + 3 \cdot P_2(x) + 5 \cdot P_3(x) $$

$$ L(x) = \frac{1}{3} x^2 + \frac{1}{3} x + 1 $$

![Screenshot from 2022-09-07 21-27-20](https://user-images.githubusercontent.com/37275728/188961030-379f428f-a0c4-403a-a6bd-e4a5393f38e0.png)
