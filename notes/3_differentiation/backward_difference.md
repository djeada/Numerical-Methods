# Backward Difference Method

The backward difference method estimates a derivative using the function value at the target point $x$ and a preceding point $x-h$, with $h>0$. It is a finite difference method: the slope over a nonzero interval replaces the limiting slope that defines the derivative. This stencil is useful at the right boundary of a dataset or when a time-dependent measurement is available only at the present and earlier times. The coordinate $x$ need not represent time, so “backward” describes the sampling direction, rather than a special physical assumption. Compared with a forward difference, it uses the opposite neighboring point; compared with a central difference, it needs data on only one side. The sections below derive its error and explain when a smaller step helps.

## Mathematical formulation

The backward difference approximation of the first derivative of a function $f$ at a point $x$ with a step size $h$ is mathematically expressed as:

$$
f'(x) \approx \frac{f(x) - f(x - h)}{h}
$$

This formula is derived from the fundamental definition of the derivative, which represents the rate of change of a function at a specific point. In the context of finite differences, the backward difference method estimates this rate by calculating the difference in function values between the point $x$ and a preceding point $x - h$, then dividing by the step size $h$. Geometrically, this approximation corresponds to the slope of the secant line that connects the points $(x - h, f(x - h))$ and $(x, f(x))$. By focusing on the interval leading up to $x$, the backward difference method provides an estimate of the derivative using the current value and one preceding value. This sampling pattern is suitable when later points are unavailable, including a right domain boundary or a time series observed only up to the present.

When derived using Taylor's theorem, the truncation error can be written with an explicit Lagrange remainder evaluated at an intermediate point $\xi\in(x-h,x)$:

$$
\frac{f(x)-f(x-h)}{h} = f'(x) - \frac{h}{2}f''(\xi),
$$

so the error is $\mathcal{O}(h)$, the same order as the forward difference but with the opposite sign of the leading term. As with the forward difference, roundoff error grows like $\varepsilon/h$, and the best step size is of order $\sqrt{\varepsilon}\approx 10^{-8}$ in double precision.

## Derivation and a more accurate boundary formula

For $f\in C^2([x-h,x])$, Taylor's theorem gives

$$
f(x-h)=f(x)-hf'(x)+\frac{h^2}{2}f''(\xi),\qquad \xi\in(x-h,x).
$$

Move $f(x-h)$ to the other side and divide by $h$. This produces the formula and signed remainder above. In particular, for $f(x)=x^2$ the approximation is $2x-h$ exactly, so the error in the example is $-0.01$, rather than an unexplained discrepancy.

If an additional past value is available, the second-order backward stencil is

$$
f'(x)\approx\frac{3f(x)-4f(x-h)+f(x-2h)}{2h}.
$$

To see the cancellation, expand $f(x-h)$ and $f(x-2h)$ about $x$: the constant coefficients sum to zero, the coefficient of $hf'(x)$ is $2$, and the coefficient of $h^2f''(x)$ is zero. After division by $2h$, the leading error is $-h^2f^{(3)}(x)/3$ under sufficient smoothness. This gains an order of accuracy while still using only current and past samples.

The step-size rule $h\sim\sqrt{\varepsilon}$ assumes function values and derivatives of comparable scale. More generally, balancing an error model $C_1h+C_2\varepsilon/h$ gives $h_{\mathrm{opt}}=\sqrt{C_2\varepsilon/C_1}$. Data noise replaces or adds to the rounding term, and the available sample spacing may prevent choosing this ideal value.

## Example

Consider the function $f(x) = x^2$. We aim to approximate the derivative of this function at the point $x = 2$ using the backward difference method with a step size $h = 0.01$. Applying the backward difference formula, we perform the following calculation:

$$
f'(2) \approx \frac{f(2) - f(2 - 0.01)}{0.01} = \frac{4 - 3.9601}{0.01} = 3.99
$$

In this example, the exact derivative of $f(x) = x^2$ at $x = 2$ is $f'(2) = 2 \times 2 = 4$. The approximation obtained using the backward difference method is $3.99$, which is remarkably close to the exact value. This demonstrates the method's effectiveness in providing accurate derivative estimates, especially when the function is smooth and the step size $h$ is appropriately chosen. However, it's important to recognize that the approximation's accuracy depends on the function's behavior and the selected step size.

## Advantages of the backward difference method

- The **ease of implementation and understanding** makes the backward difference method straightforward to apply, requiring only simple arithmetic and basic knowledge of numerical methods.
- **Minimal data requirements** ensure that the method only needs function values at $x$ and $x - h$, making it suitable for scenarios with limited or discrete data where future function values are unavailable.
- The method’s **applicability in real-time systems** allows for derivative estimation using only past and present data, which is useful in streaming data applications or real-time monitoring scenarios.

## Limitations of the backward difference method

- **Approximation error** is inherent in the method. While reducing the step size $h$ improves accuracy, excessively small $h$ can lead to numerical instability and increased roundoff errors due to floating-point precision limits.
- The method has **lower accuracy compared to the central difference method**, with an error of order $O(h)$. This means it is generally less precise for the same step size compared to the central difference method’s $O(h^2)$ accuracy.
- The **inapplicability at domain endpoints** restricts its direct use at the beginning of a domain, where $x - h$ may fall outside the interval. This limitation requires alternative methods for boundary points in numerical computations.
- **Sensitivity to function behavior** limits its reliability when the function is not smooth over the interval $[x - h, x]$, as rapid changes or discontinuities can compromise the accuracy of the approximation.
