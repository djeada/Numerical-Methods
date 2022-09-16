# Secant Method

The Secant method is a modification to Netwon method.

It replaces the derivative with a difference approximation. 

$$f'(x_n) \approx \frac{f(x_n) - f(x_{n-1})}{x_n - x_{n-1}}$$

So the formula changes from the original:

$$ x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)} $$

to the secat form:

$$x_{n+1} = x_n - f(x_n) \left ( \frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})} \right )$$
