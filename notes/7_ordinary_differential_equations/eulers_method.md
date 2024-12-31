## Euler's Method

Euler's Method is a numerical technique applied in the realm of initial value problems for ordinary differential equations (ODEs). The simplicity of this method makes it a popular choice in cases where the differential equation lacks a closed-form solution. The method might not always provide the most accurate result, but it offers a good trade-off between simplicity and accuracy.

### Mathematical Formulation

Consider an initial value problem (IVP) represented as:

$$u' = f(t, u),$$
$$u(t_0) = u_0.$$

This IVP can be solved by Euler's method, where the method employs the following approximation:

$$u_{n+1} = u_n + h*f(t_n, u_n),$$

where:
- $u_{n+1}$ is the approximate value of $u$ at $t = t_n + h$,
- $u_n$ is the approximate value of $u$ at $t = t_n$,
- $h$ is the step size,
- $f(t_n, u_n)$ is the derivative of $u$ at $t = t_n$.

### Derivation

Let's start with the Taylor series:

$$ u(t+h)=u(t)+h u'(t) + O(h^2) $$

We may alternatively rewrite the above equation as follows:

$$ u(t+h)=u(t)+ h f(u(t),t)+ O(h^2).$$

Which is roughly equivalent to:

$$ u(t+h)=u(t)+ h f(u(t),t)$$

### Algorithm Steps

1. Start with initial conditions $t_0$ and $u_0$.
2. Calculate $u_{n+1}$ using the formula: $u_{n+1} = u_n + h*f(t_n, u_n)$.
3. Repeat the above step for a given number of steps or until the final value of $t$ is reached.

### Example

$$ u'(t)=u(t),$$

$$ u(0)=1$$

$$u(0.1)=?$$

Let's choose the step value: $h = 0.05$

We start at $t=0$:

$$  u(0.05) \approx u(0)+0.05u'(0) $$

$$  u(0.05) \approx1+0.05u(0) $$

$$  u(0.05) \approx1+0.05 \cdot 1 $$

$$  u(0.05) \approx 1.05 $$

Now that we know $u(0.05)$, we can calculate the second step:

$$  u(0.1) \approx u(0.05)+0.05u'(0.05) $$

$$  u(0.1) \approx1.05+0.05u(0.05) $$

$$  u(0.1) \approx1.05+0.05 \cdot 1.05 $$

$$  u(0.1) \approx 1.1025 $$

### Advantages  

- Euler's method is **easy** to implement and serves as a foundational technique for introducing numerical solution methods for ODEs.  
- It can provide **reasonable approximations** for well-behaved functions when the step size is sufficiently small.  
- The simplicity of the method makes it computationally inexpensive for basic problems and suitable for initial experimentation.  

### Limitations  

- **Accuracy** is limited, as the method can introduce significant errors if the step size is too large or if the function has rapid changes.  
- The **cumulative error** from each step can grow significantly, making the method unsuitable for long-time integration.  
- **Stability** is an issue, as Euler's method may fail to converge or produce reliable results for stiff or oscillatory ODEs.  
- The method lacks the ability to adapt step sizes dynamically, which can lead to inefficiencies or inaccuracies in varying conditions.  
