## Linear interpolation

Linear interpolation is one of the most basic and commonly used interpolation methods. The idea is to approximate the value of a function between two known data points by assuming that the function behaves linearly (like a straight line) between these points. Although this assumption may be simplistic, it often provides a reasonable approximation, especially when the data points are close together or the underlying function is relatively smooth.

**Conceptual Illustration**:

Imagine you have two points on a graph:

![Example Illustration](https://user-images.githubusercontent.com/37275728/188960814-569c5a91-82b4-415c-9840-f5ebd4cc421d.png)

Linear interpolation draws a straight line between the two known data points $(x_i,y_i)$ and $(x_{i+1},y_{i+1})$, and then estimates the value at $x$ by following this line.

### Mathematical Formulation

Given two known data points $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$, and a target $x$-value with $x_i \leq x \leq x_{i+1}$, the line connecting these points has a slope $\alpha$ given by:

$$\alpha = \frac{y_{i+1} - y_i}{x_{i+1} - x_i}.$$

To find the interpolated value $y$ at $x$, start from $y_i$ and move along the line for the interval $(x - x_i)$:

$$y = y_i + \alpha (x - x_i).$$

Substituting $\alpha$:

$$y = y_i + (x - x_i) \frac{y_{i+1} - y_i}{x_{i+1} - x_i}.$$

This formula provides the interpolated $y$-value directly.

### Derivation

![Derivation Illustration](https://user-images.githubusercontent.com/37275728/188960726-ac99ac89-f1b8-4b82-9761-5093cb91d4db.png)

I. **Slope Calculation:**

The slope $\alpha$ of the line passing through $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$ is:

$$\alpha = \frac{y_{i+1} - y_i}{x_{i+1}-x_i}.$$

II. **Linear Equation:**

A line passing through $(x_i, y_i)$ with slope $\alpha$ is:

$$y - y_i = \alpha (x - x_i).$$

III. **Substitution:**

Replace $\alpha$ with its expression:

$$y - y_i = \frac{y_{i+1} - y_i}{x_{i+1}-x_i} (x - x_i).$$

IV. **Final Formula:**

Simplifying:

$$y = y_i + \frac{(y_{i+1} - y_i)}{x_{i+1}-x_i} (x - x_i).$$

### Alternative Form

The interpolation formula can be rewritten as a weighted average of the two $y$-values:

$$y = \frac{x_{i+1} - x}{x_{i+1} - x_i} \, y_i + \frac{x - x_i}{x_{i+1} - x_i} \, y_{i+1}.$$

The two weights sum to one and are non-negative for $x \in [x_i, x_{i+1}]$, so the result is a **convex combination** of $y_i$ and $y_{i+1}$. At $x = x_i$ the first weight is 1, recovering $y_i$; at $x = x_{i+1}$ the second weight is 1, recovering $y_{i+1}$.

### Error Analysis

If the function $f$ being interpolated has a continuous second derivative on $[x_i, x_{i+1}]$ (i.e. $f \in C^2[x_i, x_{i+1}]$), the interpolation error is bounded by:

$$|f(x) - y| \leq \frac{1}{8} h^2 \max_{\xi \in [x_i, x_{i+1}]} |f''(\xi)|,$$

where $h = x_{i+1} - x_i$ is the interval width. Because the error is $O(h^2)$, halving the spacing between data points reduces the maximum error by a factor of four.

### Algorithm Steps

I. Identify the interval $[x_i, x_{i+1}]$ that contains the target $x$.

II. Compute the slope:

$$\frac{y_{i+1} - y_i}{x_{i+1}-x_i}.$$

III. Substitute into the linear interpolation formula:

$$y = y_i + \frac{(y_{i+1} - y_i)}{x_{i+1}-x_i} (x - x_i).$$

The result is the interpolated value $y$ at the desired $x$.

### Example

**Given Points**: $A(-2,0)$ and $B(2,2)$. Suppose we want to find $y$ at $x=1$.

I. Compute the slope:

$$\alpha = \frac{2 - 0}{2 - (-2)} = \frac{2}{4} = 0.5.$$

II. Substitute $x=1$:

$$y = 0 + 0.5 (1 - (-2)) = 0.5 \times 3 = 1.5.$$

So, the line passing through $(-2,0)$ and $(2,2)$ gives $y=1.5$ when $x=1$.

**Verification at the endpoints:**

- At $x = -2$: $y = 0 + 0.5(-2 - (-2)) = 0 + 0 = 0$ ✓
- At $x = 2$: $y = 0 + 0.5(2 - (-2)) = 0.5 \times 4 = 2$ ✓

**Error bound:** If we know only that $|f''(\xi)| \leq M$ for all $\xi \in [-2, 2]$, then $h = 2 - (-2) = 4$ and the maximum interpolation error is:

$$|f(x) - y| \leq \frac{1}{8}(4)^2 M = 2M.$$

### Example 2

**Estimating $\sin(\pi/4)$ from two known values of $\sin(x)$.**

Known points: $(0,\, 0)$ and $(\pi/2,\, 1)$, since $\sin(0) = 0$ and $\sin(\pi/2) = 1$. Estimate $f(\pi/4) = \sin(\pi/4)$.

I. Compute the slope:

$$\alpha = \frac{1 - 0}{\pi/2 - 0} = \frac{2}{\pi} \approx 0.6366.$$

II. Substitute $x = \pi/4$:

$$y = 0 + \frac{2}{\pi}\left(\frac{\pi}{4} - 0\right) = \frac{2}{\pi} \cdot \frac{\pi}{4} = \frac{1}{2} = 0.5.$$

III. Compare with the exact value:

$$\sin\!\left(\frac{\pi}{4}\right) = \frac{\sqrt{2}}{2} \approx 0.7071.$$

The absolute error is $|0.7071 - 0.5| = 0.2071$.

IV. Check against the error bound. Here $h = \pi/2$ and $|f''(x)| = |\!-\!\sin(x)| \leq 1$ on $[0, \pi/2]$, so:

$$\text{max error} \leq \frac{1}{8}\left(\frac{\pi}{2}\right)^2 \cdot 1 \approx 0.3084.$$

Indeed $0.2071 < 0.3084$ ✓. This illustrates that for highly curved functions, linear interpolation can have significant error even though the bound is still respected.

### Advantages

- The method offers **simplicity**, as the calculation involves straightforward arithmetic, making it easy and quick to apply.
- **Minimal data requirements** make it practical, needing only two data points to estimate intermediate values.
- It provides a **local approximation**, working well when the function is nearly linear within the specified interval.
- When applied piecewise over consecutive intervals, the result is a **continuous interpolant** (a connected chain of line segments).

### Limitations

- The **linear assumption** can lead to poor results if the actual relationship between points is not close to linear.
- Linear interpolation uses **no derivative information**, ignoring the slope or curvature of the function, which could enhance accuracy.
- **Accuracy diminishes** as the interval between points increases or as the function becomes more non-linear, leading to potential errors in approximation.
- The piecewise-linear interpolant is **not differentiable at the knot points** (the data points), producing "kinks" where adjacent line segments meet.
