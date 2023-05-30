## Gradient Descent

- Gradient descent is a first-order iterative optimization algorithm for finding the minimum of a differentiable function.
- It's commonly used in machine learning and artificial intelligence to minimize loss functions.

## Mathematical Formulation

Given a function $f(x)$ that we want to minimize, the gradient descent method iteratively moves in the direction of steepest descent, defined by the negative of the gradient of the function at the current point. The update rule is given by:

$$x_{n+1} = x_n - \alpha \nabla f(x_n)$$ 

Where:
- $x_n$ is the current point.
- $\alpha$ is the learning rate, a positive scalar that determines the size of the step.
- $\nabla f(x_n)$ is the gradient of the function at the current point $x_n$.

## Algorithm Steps

1. **Initialization**: Start with an initial guess $x_0$.

2. **Gradient Evaluation**: Calculate the gradient of the function at the current point, $\nabla f(x_n)$.

3. **Update**: Compute the next point $x_{n+1}$ by moving from the current point $x_n$ in the direction of the negative gradient. This is done using the update rule: $x_{n+1} = x_n - \alpha \nabla f(x_n)$.

4. **Convergence Check**: Repeat steps 2-3 until the change in values is below a pre-defined threshold or maximum iterations have been reached.

## Example

Consider a simple function $f(x) = x^2$, which we want to minimize. 

We start with an initial guess $x_0 = 5$ and a learning rate $\alpha = 0.1$.

1. **Initialization**: Start with $x_0 = 5$.

2. **Gradient Evaluation**: Calculate the gradient at the current point, $f'(x_0) = 2x_0 = 10$.

3. **Update**: Update the current point using the update rule: $x_1 = x_0 - \alpha f'(x_0) = 5 - 0.1 * 10 = 4$.

4. **Repeat the process**: Using $x_1$ as the new point, repeat steps 2-3. The gradient at $x_1$ is $f'(x_1) = 2 * 4 = 8$. Update the point again: $x_2 = x_1 - \alpha f'(x_1) = 4 - 0.1 * 8 = 3.2$.

5. **Convergence**: This process continues until the change in the value of $x_n$ is less than a pre-specified tolerance or the maximum number of iterations is reached. For this simple function, gradient descent will eventually find that the minimum occurs at $x = 0$.

## Advantages

- Gradient descent is straightforward and easy to implement.
- It's particularly efficient for problems with large numbers of variables or parameters.
- It can handle functions that are not easily differentiable using other numerical methods.

## Limitations

- It can be sensitive to the choice of learning rate: too small can lead to slow convergence, too large can cause divergence.
- It may converge to a local minimum in non-convex optimization problems.
- The performance may degrade for ill-conditioned problems (where the shape of the error surface is narrow in some directions and wide in others).
