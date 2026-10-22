# Central Difference Method

The central difference method estimates a derivative using function values at equal distances on either side of the target point. It combines the forward and backward difference formulas so that their leading curvature errors cancel. For a sufficiently smooth function, this symmetry gives a second-order approximation instead of the first-order approximation produced by either two-point one-sided formula. The method is useful when a closed-form derivative is unavailable or expensive and samples can be taken on both sides. Its greater truncation accuracy does not remove rounding or measurement error; those effects still influence the useful step size.

![central difference method Illustration](https://github.com/user-attachments/assets/367d9eb0-a68b-47d4-bace-f0279fd8b1f8)

## Mathematical formulation and derivation

The central difference approximation of the first derivative of a function $f$ at a point $x$ with step size $h$ is given by:

$$
f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}
$$

This formula can be motivated as the average of the forward and backward difference formulas.

Assume $f$ is three times differentiable on $[x-h,x+h]$. By Taylor’s theorem, for some $\xi_1\in(x,x+h)$ and $\xi_2\in(x-h,x)$,

> **Note on $\xi_1,\xi_2$**
> Here we use the **Lagrange remainder** form of Taylor’s theorem. The derivatives in the polynomial part are evaluated at $x$, but the remainder term is evaluated at an intermediate point $\xi$ between the expansion point and the evaluation point. In general, replacing $\xi$ by $x$ is not valid (it would only be exact in special cases, e.g., when higher derivatives are constant).
> For a quick refresher on this notation, see [Taylor Series](taylor_series.md).

$$
f(x + h) = f(x) + hf'(x) + \frac{h^2}{2}f''(x) + \frac{h^3}{6}f^{(3)}(\xi_1)
$$

$$
f(x - h) = f(x) - hf'(x) + \frac{h^2}{2}f''(x) - \frac{h^3}{6}f^{(3)}(\xi_2)
$$

### Forward and backward differences

The forward difference approximation is:

$$
\frac{f(x+h)-f(x)}{h} = f'(x) + \frac{h}{2}f''(x) + \frac{h^2}{6}f^{(3)}(\xi_1)
$$

Thus

$$
\frac{f(x+h)-f(x)}{h} = f'(x) + \mathcal{O}(h)
$$

Similarly, the backward difference approximation is:

$$
\frac{f(x)-f(x-h)}{h} = f'(x) - \frac{h}{2}f''(x) + \frac{h^2}{6}f^{(3)}(\xi_2)
$$

Thus

$$
\frac{f(x)-f(x-h)}{h} = f'(x) + \mathcal{O}(h)
$$

### Central difference (second-order)

Average the two approximations:

$$
\begin{aligned}
\frac12\left[\frac{f(x+h)-f(x)}{h}+\frac{f(x)-f(x-h)}{h}\right]
&=\frac12\left(f'(x)+\frac h2f''(x)+\frac{h^2}{6}f^{(3)}(\xi_1)\right)\\
&\quad+\frac12\left(f'(x)-\frac h2f''(x)+\frac{h^2}{6}f^{(3)}(\xi_2)\right)\\
&=f'(x)+\frac{h^2}{12}\left(f^{(3)}(\xi_1)+f^{(3)}(\xi_2)\right).
\end{aligned}
$$

The $\pm\tfrac{h}{2}f''(x)$ terms cancel exactly, leaving only an $\mathcal{O}(h^2)$ remainder.

Rewriting the left-hand side:

$$
\frac{1}{2}\left(\tfrac{f(x+h)-f(x)}{h} +
\tfrac{f(x)-f(x-h)}{h}\right) = \frac{f(x+h)-f(x-h)}{2h}
$$

Hence

$$
\frac{f(x+h)-f(x-h)}{2h} = f'(x) +
\underbrace{\frac{h^2}{12}\bigl(f^{(3)}(\xi_1)+f^{(3)}(\xi_2)\bigr)}_{\displaystyle \mathcal{O}(h^2)}
$$

If $f^{(3)}$ is continuous, then there exists some $\xi\in(x-h,x+h)$ such that

$$
\frac{f^{(3)}(\xi_1)+f^{(3)}(\xi_2)}{2} = f^{(3)}(\xi)
$$

and therefore

$$
\frac{f(x+h)-f(x-h)}{2h} = f'(x) + \frac{h^2}{6}f^{(3)}(\xi) = f'(x) + \mathcal{O}(h^2)
$$

Equivalently,

$$
f'(x) = \frac{f(x+h)-f(x-h)}{2h} + \mathcal{O}(h^2)
$$

Dropping the explicit remainder term gives the familiar approximation:

$$
\boxed{ f'(x)\approx \frac{f(x+h)-f(x-h)}{2h} }
$$

which is **second-order accurate** (error $\propto h^2$) because the leading $h^1$ terms have cancelled.

## Error in central difference method

The error in the central difference method is of the order $\mathcal{O}(h^2)$, which implies that the truncation error decreases quadratically as the step size $h$ approaches zero. This quadratic rate of convergence makes the central difference method significantly more accurate than the forward or backward difference methods, which typically have an error of order $\mathcal{O}(h)$.

However, while reducing $h$ improves truncation error, it must be balanced against floating-point roundoff. Extremely small values of $h$ can lead to subtractive cancellation in $f(x+h)-f(x-h)$, limiting the practical accuracy achievable with this method.

Quantitatively, the roundoff error is roughly $\varepsilon\,|f(x)|/h$ (with $\varepsilon\approx 2.2\times10^{-16}$ in double precision), while the truncation error is $\frac{h^2}{6}|f^{(3)}|$. Balancing the two gives an optimal step of order $h\sim\varepsilon^{1/3}\approx 10^{-5}$ (scaled by $(|f|/|f^{(3)}|)^{1/3}$), with a best attainable error of about $\varepsilon^{2/3}\approx 10^{-11}$. This is both a larger step and a smaller error than the $\sqrt{\varepsilon}$ step and $\sqrt{\varepsilon}$ error of the one-sided differences.

## Checking the order and reusing symmetry

For $f(x)=x^2$, the third derivative vanishes, so the central difference is **exact in exact arithmetic for every nonzero $h$**. The example below illustrates cancellation, but does not by itself demonstrate a nonzero second-order error. For $f(x)=x^3$,

$$
\frac{(x+h)^3-(x-h)^3}{2h}=3x^2+h^2,
$$

so halving $h$ reduces the error by exactly a factor of four before floating point effects become important.

The same symmetric Taylor expansions can be **added**, rather than subtracted, to estimate a second derivative:

$$
f''(x)\approx\frac{f(x+h)-2f(x)+f(x-h)}{h^2}.
$$

With a bounded fourth derivative this has error $O(h^2)$. Its rounding and data errors are amplified by $1/h^2$, so its useful step size differs from the first-derivative formula.

For a sufficiently smooth first derivative, write $D_h=f'(x)+ch^2+O(h^4)$ and $D_{h/2}=f'(x)+ch^2/4+O(h^4)$. Eliminating $c$ gives Richardson extrapolation:

$$
f'(x)\approx\frac{4D_{h/2}-D_h}{3},
$$

with fourth-order truncation accuracy. The improvement assumes smoothness and accurate function samples; extrapolation does not remove measurement noise or rounding error.

## Unequally spaced neighboring samples

The symmetric formula assumes the same spacing on both sides. If the available samples are at $x-h_-$, $x$, and $x+h_+$, with $h_-,h_+>0$, differentiate the quadratic interpolant through those three points instead. This gives

$$
\begin{aligned}
f'(x)\approx{}&-\frac{h_+}{h_-(h_-+h_+)}f(x-h_-)\\
&+\frac{h_+-h_-}{h_-h_+}f(x)\\
&+\frac{h_-}{h_+(h_-+h_+)}f(x+h_+).
\end{aligned}
$$

The weights reproduce constants, linear functions, and quadratics exactly. Setting $h_-=h_+=h$ removes the middle term and recovers the usual central difference. With sufficient smoothness and comparable shrinking spacings, the formula retains second-order truncation accuracy. Simply replacing the denominator of the symmetric formula by $h_-+h_+$ does not generally achieve this, because the unequal one-sided errors no longer cancel.

## Example

Suppose we have a function $f(x) = x^2$, and we want to approximate the derivative at the point $x = 2$ with a step size $h = 0.01$. Using the central difference method, we get:

$$
f'(2) \approx
\frac{f(2 + 0.01) - f(2 - 0.01)}{2 \times 0.01} = \frac{4.0401 - 3.9601}{0.02} = 4.00
$$

The exact derivative of $f(x) = x^2$ at the point $x = 2$ is $f'(2) = 2 \times 2 = 4$, so the approximation is accurate. This example demonstrates how the central difference method can effectively approximate derivatives with high precision for smooth functions, while also highlighting the importance of an appropriate step size $h$.

## Advantages

- The method offers **higher accuracy** compared to forward or backward difference methods by using function values on both sides of the point, reducing the leading error term in derivative approximations.
- **Simplicity in implementation** makes it easy to apply, with straightforward formulas that are accessible for numerical analysis and computational tasks.
- The central difference method is **applicable to discrete data**, allowing for its use when analytical derivatives are difficult or impossible, such as in data fitting, signal processing, and numerical simulations.

## Limitations

- There is always an **approximation error**. Decreasing the step size $h$ reduces truncation error, but excessively small $h$ can cause numerical issues due to floating-point roundoff.
- The method requires **function values on both sides** of the point, so it cannot be applied directly at domain boundaries unless the function is defined beyond those boundaries (or one uses one-sided/ghost-point techniques).
