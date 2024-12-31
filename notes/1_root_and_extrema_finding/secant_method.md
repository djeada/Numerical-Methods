## Secant Method

The Secant Method is a root-finding algorithm used in numerical analysis to approximate the zeros of a given function $f(x)$. It can be regarded as a derivative-free variant of Newton's method. Instead of computing the derivative $f'(x)$ at each iteration (as done in Newton’s method), it approximates the derivative by using two previously computed points. This approach allows the Secant Method to be applied even when the function is not easily differentiable, and under suitable conditions, it often converges faster than simpler bracket-based methods (like the bisection method).

Conceptually, the Secant Method constructs a secant line between two points $(x_{n-1}, f(x_{n-1}))$ and $(x_n, f(x_n))$ on the graph of $f(x)$. The root approximation is then taken as the $x$-intercept of this secant line. By iteratively updating these points, the method “zeroes in” on a root.

**Conceptual Illustration**:

Imagine plotting the function $f(x)$:

![secant_method](https://github.com/user-attachments/assets/5e904eb0-1c4f-499a-9937-39fcdb210fde)

The intersection of the secant line with the x-axis gives the next approximation $x_{n+1}$. Repeating this procedure leads to progressively better approximations of the root, assuming the method converges.

### Mathematical Formulation

Consider a continuous function $f(x)$ for which we want to solve $f(x)=0$. The Secant Method starts with two initial approximations $x_0$ and $x_1$, and then generates a sequence $\{x_n\}$ according to:

$$x_{n+1} = x_n - f(x_n)\frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}$$

This formula approximates the derivative $f'(x_n)$ by the finite difference:

$$f'(x_n) \approx \frac{f(x_n)-f(x_{n-1})}{x_n - x_{n-1}}$$

By replacing $f'(x_n)$ with the above approximation in the Newton's method formula, we arrive at the Secant Method formula.

### Derivation

I. **Starting from Newton’s Method**:  

Newton’s method update rule is:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}.$$

II. **Approximating the Derivative**:  

If the derivative $f'(x_n)$ is difficult to compute or unknown, we can use a finite difference approximation based on the two most recent points:

$$f'(x_n) \approx \frac{f(x_n)-f(x_{n-1})}{x_n - x_{n-1}}.$$

III. **Substitute into Newton’s Formula**:

Replacing $f'(x_n)$ with this approximation gives:

$$x_{n+1} = x_n - \frac{f(x_n)}{\frac{f(x_n)-f(x_{n-1})}{x_n - x_{n-1}}}.$$

IV. **Simplify the Expression**:

By rearranging, we get:

$$x_{n+1} = x_n - f(x_n) \frac{x_n - x_{n-1}}{f(x_n)-f(x_{n-1})}.$$

This is the Secant Method iteration formula.

### Algorithm Steps

**Input:**

- A function $f(x)$.
- Two initial points $x_0$ and $x_1$.
- A tolerance $\epsilon > 0$ or a maximum number of iterations $n_{\max}$.

**Initialization:**

Set $n=1$ (since we already have $x_0$ and $x_1$).

**Iteration:**

I. Evaluate $f(x_{n})$ and $f(x_{n-1})$.

II. Compute:

$$x_{n+1} = x_n - f(x_n) \frac{x_n - x_{n-1}}{f(x_n)-f(x_{n-1})}$$

III. Check for convergence:

- If $|x_{n+1}-x_n|< \epsilon$ or $|f(x_{n+1})|< \epsilon$, stop.
- If $n > n_{\max}$, stop.

IV. Update indices: $n = n+1$ and repeat step I.

**Output:**

- Approximate root $x_{n+1}$.
- Number of iterations performed.

### Example

**Given Function:**

$$f(x)=x^2 -4.$$

We know the roots are $x=\pm 2$. Suppose we do not know the roots in advance and start with:

$$x_0=0, \quad x_1=1$$

**Iteration 1:**

- $f(x_0)=f(0)=0^2-4=-4$.
- $f(x_1)=f(1)=1^2-4=-3$.

Update:

$$x_2 = x_1 - f(x_1)\frac{x_1 - x_0}{f(x_1)-f(x_0)} = 1 -(-3)\frac{1-0}{(-3)-(-4)} = 1 -(-3)\frac{1}{-3+4} = 1-( -3 \times 1 ) = 1 +3 =4.$$

Check carefully:  

Actually, let's compute step-by-step to avoid confusion:

$$x_2 = 1 - (-3)\frac{1-0}{-3-(-4)} = 1 - (-3)\frac{1}{-3+4} = 1 - (-3)\frac{1}{1} = 1+3 =4.$$

**Iteration 2:**

Now:

- $x_1=1, x_2=4$.
- $f(1)=-3, f(4)=4^2-4=16-4=12.$

Update:

$$x_3 = x_2 - f(x_2)\frac{x_2 - x_1}{f(x_2)-f(x_1)} = 4 - 12\frac{4-1}{12-(-3)} = 4 - 12\frac{3}{15}=4 -12 \times 0.2 =4 -2.4=1.6.$$

**Iteration 3:**

Now:

- $x_2=4, x_3=1.6$.
- $f(4)=12, f(1.6)=1.6^2-4=2.56-4=-1.44.$

Update:

$$x_4 = x_3 - f(x_3)\frac{x_3 - x_2}{f(x_3)-f(x_2)} = 1.6 - (-1.44)\frac{1.6-4}{-1.44-12} $$

$$= 1.6 -(-1.44)\frac{-2.4}{-13.44} $$

$$= 1.6 -(-1.44)\frac{-2.4}{-13.44}$$

Compute inside:

$$\frac{-2.4}{-13.44}=0.1786\text{(approx)}, \quad (-1.44)\times0.1786=-0.2572$$

So:

$$x_4 = 1.6 - (-0.2572)=1.6+0.2572=1.8572$$

Repeating further will bring the sequence closer to $x=2$.

However, let's simplify by noting that if we start closer to the root, the method converges faster. For example, if we start with $x_0=0$ and $x_1=1$, after the first step we got $x_2=4$, which moved us away initially, but subsequent steps pull the approximation toward $x=2$. Adjusting initial guesses (e.g., starting with $x_0=1$ and $x_1=3$) might yield quicker convergence to the root $x=2$.

### Advantages

- The secant method avoids requiring an **analytic derivative**, unlike Newton’s method, which is particularly useful for functions that are difficult or impossible to differentiate analytically.
- Convergence in the secant method is typically **faster than linear convergence**, which is common in the bisection method, though it is not as fast as the quadratic convergence seen in Newton's method.
- The secant method is easy to **implement due to its simple iterative formula**, which relies only on function evaluations and does not require derivative or interval-based calculations.

### Limitations

- Convergence is not **guaranteed**, as poor initial guesses can cause divergence or failure to find a root.
- Functions with **multiple roots** pose challenges because the secant method may converge to an unintended root if the initial guesses are closer to a different zero.
- The method’s **stability and efficiency are highly dependent** on the initial guesses, $x_0$ and $x_1$, which play a critical role in determining whether the method converges and how quickly.
- The secant method does not offer **quadratic convergence** like Newton’s method, resulting in slower convergence rates compared to derivative-based methods when derivatives are available and feasible to compute.
