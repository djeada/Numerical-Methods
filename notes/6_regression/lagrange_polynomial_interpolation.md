## Lagrange Polynomial Interpolation

Lagrange Polynomial Interpolation is a form of interpolation which uses the Lagrange basis polynomials, denoted as $P_i(x)$, to form an interpolating polynomial, $L(x)$, which passes through all the given points $(x_i, y_i)$.

## Mathematical Formulation

Given $n+1$ distinct points $(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)$, the goal of Lagrange interpolation is to find a polynomial $L(x)$ of degree $n$, such that $L(x_i) = y_i$.

The polynomial $L(x)$ is given by:

$$L(x) = \sum_{i=0}^{n} y_i P_i(x)$$

Here $P_i(x)$ is the $i$-th Lagrange basis polynomial given by:

$$P_i(x) = \prod_{j=0, j\neq i}^{n} \frac{x - x_j}{x_i - x_j}$$

## Derivation

Given $n+1$ points $(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)$, we want to find an $n$-th degree polynomial $L(x)$ such that $L(x_i) = y_i$ for all $i=0,1,2,...,n$.

We can express $L(x)$ as:

$$L(x) = \sum_{i=0}^{n} y_i P_i(x)$$

Where $P_i(x)$ is the $i$-th Lagrange basis polynomial given by:

$$P_i(x) = \prod_{j=0, j\neq i}^{n} \frac{x - x_j}{x_i - x_j}$$

For a specific $i$, all terms in the product $P_i(x)$ will be zero at $x=x_j$ for all $j\neq i$. Hence $L(x_j) = y_j$ for all $j$.

## Algorithm Steps

1. Given a set of $(x_i, y_i)$ points, initialize $L(x) = 0$.

2. For each point $x_i$, calculate the Lagrange basis polynomial $P_i(x)$:

    - Initialize $P_i(x) = 1$.
    - For each $x_j$ where $j \neq i$, calculate the term $\frac{x - x_j}{x_i - x_j}$ and multiply it with the current value of $P_i(x)$.

3. Calculate $L(x)$ by adding the product of $y_i$ and $P_i(x)$ to the current value of $L(x)$ for each point $x_i$.

4. The final $L(x)$ is the Lagrange interpolating polynomial.

## Example

Given three points A(-1, 1), B(2, 3), and C(3,5), we want to interpolate a polynomial using the Lagrange method.

The Lagrange basis polynomials are calculated as:

$$P_1(x) = \frac{(x - x_2)(x - x_3)}{(x_1-x_2)(x_1-x_3)} = \frac{(x - 2)(x - 3)}{(-1-2)(-1-3)} = \frac{1}{12}(x^2 - 5x + 6)$$

$$P_2(x) = \frac{(x - x_1)(x - x_3)}{(x_2-x_1)(x_2-x_3)} = \frac{(x + 1)(x - 3)}{(2 + 1)(2-3)} = -\frac{1}{3}(x^2 - 2x - 3)$$

$$P_3(x) = \frac{(x - x_1)(x - x_2)}{(x_3-x_1)(x_3-x_2)} = \frac{(x + 1)(x - 2)}{(3 + 1)(3-2)} =\frac{1}{4}(x^2 -x - 2)$$

The Lagrange interpolating polynomial is then:

$$L(x) = 1 \cdot P_1(x) + 3 \cdot P_2(x) + 5 \cdot P_3(x)$$

![Lagrange Polynomial Plot](https://user-images.githubusercontent.com/37275728/188961030-379f428f-a0c4-403a-a6bd-e4a5393f38e0.png)

## Advantages

1. **Exact Fit**: The Lagrange interpolation polynomial fits exactly to the given data points.
2. **Ease of Use**: The formulation of the Lagrange interpolation polynomial is straightforward and requires no solution of linear equations unlike other interpolation methods.

## Limitations

1. **Runge's Phenomenon**: Lagrange interpolation can suffer from oscillations between points, especially for high degree polynomials.
2. **Inefficiency**: If a new data point is added, the entire polynomial needs to be recalculated.
