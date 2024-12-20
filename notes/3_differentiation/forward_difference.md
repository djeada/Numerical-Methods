## Forward Difference Method

- The forward difference method is a finite difference method used for approximating derivatives.
- It is based on the difference between the function values at two points, and it approximates the derivative at a point using the function value at that point and the function value at a following point.

![Untitled](https://github.com/user-attachments/assets/6643da65-3308-4cac-b597-a1da3608a6e2)

### Mathematical Formulation

The forward difference approximation of the first derivative of a function $f$ at a point $x$ with step size $h$ is given by:

$$f'(x) \approx \frac{f(x + h) - f(x)}{h}$$

This formula is derived from the definition of the derivative, and it represents the slope of the line passing through the points $(x, f(x))$ and $(x + h, f(x + h))$.

### Example

Suppose we have a function $f(x) = x^2$, and we want to approximate the derivative at the point $x = 2$ with a step size $h = 0.01$. Using the forward difference method, we get:

$$f'(2) \approx \frac{f(2 + 0.01) - f(2)}{0.01} = \frac{4.0401 - 4}{0.01} \approx 4.01$$

The exact derivative of $f(x) = x^2$ at the point $x = 2$ is $f'(2) = 2*2 = 4$, so the approximation is close.

### Advantages

- The forward difference method is easy to implement and understand.
- It only requires the function values at two points, so it can be used when the function is difficult to evaluate or when only discrete data is available.

### Limitations

- The forward difference method is only an approximation, and it introduces some amount of error. The error decreases as the step size $h$ gets smaller, but making $h$ too small can lead to numerical instability due to the limitations of floating-point arithmetic.
- The method is less accurate when the function is rapidly changing or not smooth.
