## Picard's Iteration Method

Picard's method, alternatively known as the method of successive approximations, is a tool primarily used for solving initial-value problems for first-order ordinary differential equations (ODEs). The approach hinges on an iterative process that approximates the solution of an ODE. Though this method is notably simple and direct, it can sometimes converge slowly, depending on the specifics of the problem at hand.

### Mathematical Formulation of Picard's Method

Picard's method originates from the idea of expressing the solution to an ODE as an infinite series. We then approximate this solution by truncating the series after a certain number of terms. Given a first-order ODE of the general form $y' = f(x, y)$, complemented by the initial condition $y(x_0) = y_0$, we can express the iterative formula for Picard's method as follows:

$$y_{n+1}(x) = y_0 + \int_{x_0}^{x} f(t, y_n(t)) dt$$

### Derivation

Picard's method of successive approximations is based on the principle of transforming the differential equation into an equivalent integral equation, which can then be solved iteratively. Let's take a look at how it's derived.

Consider a first-order ordinary differential equation (ODE):

$$ y'(t) = f(t, y(t)),$$

with an initial condition: 

$$ y(t_0) = y_0$$

The main idea of Picard's method is to rewrite the ODE as an equivalent integral equation by integrating both sides with respect to $t$ over the interval $[t_0, t]$:

$$\int_{t_0}^t y'(t) dt = \int_{t_0}^t f(t, y(t)) dt$$

The left-hand side of the equation becomes $y(t) - y(t_0)$ by the fundamental theorem of calculus, which we can rewrite using our initial condition to obtain:

$$y(t) = y_0 + \int_{t_0}^t f(s, y(s)) ds$$

Now we can see the integral equation form of the initial value problem. 

To solve this equation using Picard's method, we generate a sequence of functions ${y_n(t)}$ iteratively as:

$$y_{n+1}(t) = y_0 + \int_{t_0}^t f(s, y_n(s)) ds,$$

where $y_0(t)$ is the initial guess (often taken as the constant function $y_0(t) = y_0$).

Each approximation $y_{n+1}(t)$ is defined in terms of the previous approximation $y_n(t)$, creating an iterative process which can be repeated until a desired level of accuracy is achieved.

### Algorithm steps

1. Start with an initial approximation $y_0(x)$.
2. Calculate the next approximation $y_{n+1}(x) = y_0 + \int_{x_0}^{x} f(t, y_n(t)) dt$.
3. Repeat step 2 for a pre-determined number of iterations $n$ or until the approximation of the solution meets the required accuracy.

### Example Application

Consider the first-order ODE

$$y' = x + y, \quad y(0) = 1$$

We will use **Picard iteration** (also called the **method of successive approximations**) to approximate the solution. Recall that if $y$ solves the initial value problem, then $y$ must satisfy the integral equation

$$y(x) = y(0) + \int_{0}^{x} \bigl(t + y(t)\bigr) dt$$

Because $y(0) = 1$, this becomes

$$y(x) = 1 + \int_{0}^{x} \bigl(t + y(t)\bigr) dt$$

#### Step 1: Choose an initial guess

A simple choice for the initial approximation is a constant function that satisfies the initial condition:
$$y_0(x) = 1$$

#### Step 2: Form the iteration

Define the $(n+1)$-th approximation $y_{n+1}(x)$ by

$$y_{n+1}(x) = 1 + \int_{0}^{x} \bigl(t + y_n(t)\bigr) dt$$

#### Step 3: Compute the first few iterates

I. **First iterate $\mathbf{y_1}$:**

Starting from $y_0(t) = 1$,
$$y_1(x) = 1 + \int_0^x \bigl(t + y_0(t)\bigr) dt = 1 + \int_0^x \bigl(t + 1\bigr) dt$$

Compute the integral:

$$\int_0^x \bigl(t + 1\bigr) dt = \left[\tfrac{1}{2}t^2 + t\right]_{t=0}^{t=x} = \tfrac{1}{2}x^2 + x$$

Hence

$$y_1(x) = 1 + \left(\tfrac{1}{2}x^2 + x\right) = 1 + x + \tfrac{1}{2}x^2$$

II. **Second iterate $\mathbf{y_2}$:**

Now substitute $y_1(t) = 1 + t + \tfrac{1}{2}t^2$ into the integral:

$$y_2(x) = 1 + \int_0^x \bigl(t + y_1(t)\bigr) dt = 1 + \int_0^x \Bigl(t + \bigl(1 + t + \tfrac{1}{2}t^2\bigr)\Bigr) dt = 1 + \int_0^x \bigl(1 + 2t + \tfrac{1}{2}t^2\bigr) dt$$
Compute this integral:
$$\int_0^x \bigl(1 + 2t + \tfrac{1}{2}t^2\bigr) dt = \left[ t + t^2 + \tfrac{1}{6}t^3\right]_{t=0}^{t=x} = x + x^2 + \tfrac{1}{6}x^3$$

Therefore,

$$y_2(x) = 1 + \bigl(x + x^2 + \tfrac{1}{6}x^3\bigr) = 1 + x + x^2 + \tfrac{1}{6}x^3$$

In principle, you continue in this manner—substituting $y_n(x)$ back into the integral equation—to obtain $y_{n+1}(x)$. You either stop when you get a satisfactory approximation or when you reach your maximum number of iterations.

#### Observing a Pattern

Notice how each iteration adds higher-order polynomial terms in $x$. In fact, this process is **building the power-series expansion** of the true solution around $x=0$. More and more terms (with increasing powers of $x$) appear as you iterate.

#### The Exact Solution

Although Picard iteration is a good way to *approximate* or *numerically* solve the ODE, we can also solve it directly by standard methods for first-order linear ODEs. Indeed, rewriting

$$y' - y = x$$

the integrating factor is $e^{-x}$. Multiplying the equation by $e^{-x}$ gives

$$\frac{d}{dx}\bigl(e^{-x}y\bigr) = x e^{-x}$$

Integrate both sides from $0$ to $x$:

$$e^{-x}   y(x) - e^{-0} y(0) = \int_0^x t e^{-t} dt$$

Since $y(0) = 1$, the left-hand side is $e^{-x} y(x) - 1$. The right-hand side can be computed by integration by parts (or looked up in a table):

$$\int_0^x t   e^{-t}   dt = \bigl[-(t+1)e^{-t}\bigr]_{0}^{x} = - (x+1) e^{-x} + 1$$

Hence,

$$e^{-x}y(x) - 1 = - (x+1) e^{-x} + 1 \quad\Longrightarrow\quad e^{-x}y(x) = 2 - (x+1)e^{-x}$$

Multiply both sides by $e^{x}$ to solve for $y(x)$:

$$y(x) = 2 e^x - (x+1)$$

A quick check: at $x=0$, $y(0) = 2\cdot 1 - (0+1) = 1$, matching the initial condition.

#### Connecting Back to the Iterates

If you **expand the exact solution** $y(x) = 2e^x - (x+1)$ in a Maclaurin series around $x=0$,

$$2e^x = 2\Bigl(1 + x + \tfrac{x^2}{2!} + \tfrac{x^3}{3!} + \cdots\Bigr) = 2 + 2x + x^2 + \tfrac{x^3}{3} + \cdots$$

$$2e^x - (x+1) = (2-1) + (2x - x) + x^2 + \tfrac{x^3}{3} + \cdots = 1 + x + x^2 + \tfrac{x^3}{3} + \cdots$$

Picard iteration naturally generates the **partial sums** of this series:

$$y_1(x) = 1 + x + \tfrac{1}{2}x^2, \quad y_2(x) = 1 + x + x^2 + \tfrac{1}{6}x^3, \quad y_3(x) = 1 + x + x^2 + \tfrac{1}{3}x^3 + \cdots,$$

and so on. Each iterate gets you closer to the true (infinite series) solution; numerically, you see that the coefficients of each power of $x$ converge to those in the exact expansion.

In this example, the partial sums $y_0, y_1, y_2,  dots$ quickly converge to the **exact solution** 

$$y(x) = 2 e^x - (x+1)$$

If one needs a purely numerical approach (especially for more complicated $f(x,y)$), continuing the iteration until it stabilizes (or up to a certain tolerance/number of terms) provides a valid approximate solution.

### Advantages

- Picard's method provides a **straightforward iterative process** for solving ODEs and is particularly useful in theoretical contexts for proving the existence and uniqueness of solutions.  
- The **series-based solution** derived from Picard's method allows for a clear understanding of the solution's structure and behavior in mathematical terms.  
- It can serve as a foundation for teaching **iterative techniques** and for introducing students to numerical and analytical solution methods.  
- The method is well-suited for equations where both the function $f(x, y)$ and its **integral** are smooth, ensuring convergence in many standard cases.  

### Limitations

- Each iteration of **Picard's method** involves evaluating an integral, which becomes computationally demanding for complicated or multidimensional functions.  
- **Convergence** is not guaranteed for functions $f(x, y)$ that are discontinuous, unbounded, or violate Lipschitz conditions in the region of interest.  
- The method tends to converge slowly for **stiff or nonlinear ODEs**, making it less practical for such problems compared to other numerical methods.  
- Applying Picard's method can be impractical for ODEs requiring **high precision**, as the number of iterations to achieve accuracy grows significantly.  
- The approach is not suitable for equations where **numerical solutions** are desired quickly, as alternative methods like Runge-Kutta or finite difference techniques are often more efficient.  
