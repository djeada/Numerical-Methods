## Ordinary Differential Equations (ODEs)

An **ordinary differential equation (ODE)** is an equation that involves:

I. One independent variable, often denoted by $t$ (in many applications, $t$ represents time).

II. One dependent variable (or unknown function), which we may denote by $y(t)$.

III. The derivatives of the dependent variable with respect to the independent variable.

Formally, an ODE can be written as

$$F\bigl(t, y(t), y'(t), y''(t), \dots, y^{(n)}(t)\bigr) = 0$$

where $y^{(n)}(t)$ denotes the $n$-th derivative of $y$ with respect to $t$. The integer $n$ is called the **order** of the ODE.

The term *ordinary* differentiates it from a **partial differential equation (PDE)**, in which derivatives with respect to multiple independent variables can appear.

### Classification and Terminology

- **Order**: The order of an ODE is the order of the highest derivative appearing in the equation.
- **Degree**: The degree of an ODE is the exponent of the highest-order derivative after the equation has been simplified and cleared of any fractional or irrational expressions in the derivatives.
- **Linearity vs. Nonlinearity**: 

A (single) ODE is **linear** if it can be expressed in the form

$$a_n(t)y^{(n)}(t) + a_{n-1}(t)y^{(n-1)}(t) + \cdots + a_1(t)y'(t) + a_0(t)y(t) = g(t)$$

where $a_0(t), \dots, a_n(t)$ and $g(t)$ are functions of $t$ only (i.e., do not depend on $y$ or its derivatives). If any product of the dependent variable and/or its derivatives or any power other than $1$ of $y$ or its derivatives appears, then the ODE is **nonlinear**.

- **Homogeneous vs. Nonhomogeneous** (Inhomogeneous) for Linear ODEs: A linear ODE is called **homogeneous** if $g(t) \equiv 0$. Otherwise, it is **nonhomogeneous** or **inhomogeneous** if $g(t) \neq 0$.
- **Autonomous vs. Nonautonomous**: An **autonomous** ODE is one in which the independent variable $t$ does not appear explicitly in the function $F$. For instance, $y' = f(y)$ is autonomous. A **nonautonomous** ODE explicitly depends on $t$, for example $y' = f(t, y)$.

### Understanding Differential Equations

Differential equations capture the relationship between a function (representing a quantity of interest) and its rates of change. These arise naturally in numerous domains:

- In **physics**, Newton’s laws of motion lead to second-order ODEs in time describing the positions of objects.
- In **biology**, population growth can often be modeled by first-order ODEs.
- In **engineering**, circuits and systems obey Kirchhoff’s laws or mass-spring-damper systems described by second-order ODEs.
- In **economics**, growth models and dynamic systems can be formulated as ODEs.

#### Initial Conditions and Boundary Conditions

To find a unique solution, one often needs:

- **Initial conditions**, e.g., for a first-order ODE $y'(t) = f(t,y)$, one typically specifies $y(t_0) = y_0$.
- For higher-order ODEs, more initial values (or boundary values) are required. For example, a second-order ODE might need $y(t_0) = y_0$ and $y'(t_0) = v_0$.

The combination of a differential equation and enough conditions to fix a unique solution is called an **initial value problem (IVP)** or **boundary value problem (BVP)**, depending on whether the conditions are specified at a single point (IVP) or at different points (BVP).

#### Existence and Uniqueness of Solutions

A crucial theoretical aspect of ODEs is ensuring whether a solution to a given IVP exists and whether it is unique. One fundamental result for first-order ODEs is the **Picard–Lindelöf theorem (also known as the Existence and Uniqueness Theorem)**, which states that if:

I. $f(t,y)$ is continuous in a region around $(t_0, y_0)$,

II. $f$ satisfies a Lipschitz condition in $y$ (i.e., there exists a constant $L$ such that

$$\bigl| f(t, y_1) - f(t, y_2) \bigr| \le L \bigl| y_1 - y_2 \bigr|$$

for all $y_1, y_2$ in that region), then there exists a time interval $(t_0 - \delta, t_0 + \delta)$ on which there is a unique solution $y(t)$ satisfying $y(t_0) = y_0$.

### Main Concepts in Ordinary Differential Equations

We revisit the key concepts with further mathematical detail:

#### Order

If an ODE contains derivatives up to the $n$-th derivative, it is called an **$n$-th order** ODE. For example:

- $\frac{dy}{dt} = f(t, y)$ is a first-order ODE.
- $\frac{d^2y}{dt^2} + a(t)\frac{dy}{dt} + b(t)y = 0$ is a second-order ODE.

#### Degree

The **degree** is determined by writing the ODE in polynomial form in its highest-order derivative. For example, the ODE

$$\left(y''\right)^2 + \left(y'\right)^3 + y = 0$$
is **not** in polynomial form due to the squared second derivative and cubed first derivative. However, if we could (somehow) algebraically solve for the highest-order derivative and rewrite it linearly or as a polynomial expression without fractional exponents, then the exponent of that highest-order derivative would tell us the degree. Many ODEs (especially linear ones) are understood in simpler terms: the degree is typically $1$ for linear ODEs.

#### Linearity

A **linear** ODE of order $n$ has the form

$$a_n(t)y^{(n)} + a_{n-1}(t)y^{(n-1)} + \cdots + a_1(t)y' + a_0(t)y = g(t),$$

where each $a_k(t)$ (for $k = 0,1,\dots,n$) and $g(t)$ depend only on $t$. No products like $(y')^2$ or $yy''$ occur, nor do terms such as $\sin(y)$. If such terms do occur, the ODE is **nonlinear**.

#### Homogeneity

- A linear ODE is **homogeneous** if $g(t) = 0$. The homogeneous form is

  $$a_n(t)y^{(n)} + a_{n-1}(t)y^{(n-1)} + \cdots + a_1(t)y' + a_0(t)y = 0.$$
- It is **nonhomogeneous (or inhomogeneous)** if $g(t) \neq 0$.

#### Autonomous ODEs

- An **autonomous** ODE does not explicitly depend on $t$. Formally, it takes a form such as $y' = f(y)$.
- The solutions and their qualitative behavior can often be studied using **phase-line analysis** (for first-order autonomous ODEs) or **phase-plane analysis** (for second-order systems), etc.

### Mathematical Forms of Ordinary Differential Equations

Below are some standard forms that frequently appear.

#### General First-Order ODE

$$\frac{dy}{dt} = f\bigl(t, y(t)\bigr), \quad y(t_0) = y_0$$

- **Goal**: Find a function $y(t)$ that satisfies the differential equation for $t$ in some interval containing $t_0$ and also satisfies the initial condition $y(t_0) = y_0$.

#### First-Order Linear ODE

$$\frac{dy}{dt} + p(t)y = g(t).$$

This is a subset of the above form but is special because its solution technique is well-known. A classic approach is the **Integrating Factor** method:

I. Multiply both sides by the integrating factor

$$\mu(t) = e^{\int p(t)dt}.$$

II. Rewrite the left-hand side as the derivative of $\mu(t)y(t)$.

III. Integrate both sides w.r.t. $t$ to solve for $y(t)$.

#### Second-Order Linear ODE

$$\frac{d^2y}{dt^2} + a(t)\frac{dy}{dt} + b(t)y = g(t)$$

- **Homogeneous** if $g(t) = 0$.
- **Nonhomogeneous** if $g(t) \neq 0$.

#### Constant-Coefficient Case

When $a$ and $b$ are constants, the ODE

$$y'' + ay' + by = g(t)$$

can be solved using:

I. **Characteristic equation** for the associated homogeneous part:

$$r^2 + ar + b = 0$$

II. The solution of the homogeneous ODE depends on the discriminant $\Delta = a^2 - 4b$:

- If $\Delta > 0$, two distinct real roots $r_1$ and $r_2$. 
- If $\Delta = 0$, a repeated real root $r$.
- If $\Delta < 0$, two complex conjugate roots $\alpha \pm i\beta$.

III. A **particular solution** $y_p(t)$ must be found (e.g., via the method of undetermined coefficients or variation of parameters) for the nonhomogeneous case.

IV. The **general solution** is $y(t) = y_h(t) + y_p(t)$.

#### Autonomous ODE

$$\frac{dy}{dt} = f\bigl(y(t)\bigr).$$

Analyzing equilibrium (steady-state) solutions where $f(y)=0$ is a powerful tool for studying the long-term behavior (qualitative analysis).

### Solutions of Ordinary Differential Equations

#### General Remarks

A **solution** to an ODE on an interval $I$ is a function $y(t)$ that:

I. Is differentiable up to the required order on $I$.

II. Substitutes into the ODE to satisfy it identically for all $t \in I$.

#### General vs. Particular Solutions

- A **general solution** often contains constants (like $C_1, C_2, \ldots$) that can be set by initial or boundary conditions.
- A **particular solution** is a single, specific solution that satisfies both the ODE and a given set of boundary/initial conditions.

### 5.3 Classic Examples

I. **First-Order Linear with Constant Coefficient**  

$$\frac{dy}{dt} = ay \quad \longrightarrow \quad \frac{dy}{y} = adt$$

Integrating both sides:

$$\ln|y| = at + C \quad \longrightarrow \quad y(t) = C_1 e^{a t}$$

If $y(t_0) = y_0$, then $C_1 = y_0 e^{-a t_0}$.

II. **Second-Order Homogeneous with Constant Coefficients**  

$$y'' + ay' + by = 0.$$
The characteristic equation is $r^2 + ar + b = 0$. Let $\Delta = a^2 - 4b$. 
- If $\Delta > 0$ with roots $r_1, r_2$, the general solution is

 $$y(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t}.$$
- If $\Delta = 0$ with repeated root $r$, the general solution is

 $$y(t) = \bigl(C_1 + C_2t\bigr) e^{r t}.$$
- If $\Delta < 0$ with complex roots $\alpha \pm i\beta$, the general solution is

 $$y(t) = e^{\alpha t}\bigl(C_1 \cos(\beta t) + C_2 \sin(\beta t)\bigr).$$

III. **Second-Order Nonhomogeneous with Constant Coefficients**  

$$y'' + ay' + by = g(t).$$

One finds the **general solution** as

$$y(t) = y_h(t) + y_p(t),$$
where $y_h(t)$ is the general solution of the homogeneous equation, and $y_p(t)$ is any particular solution of the original nonhomogeneous equation.

### Examples of Ordinary Differential Equations

I. **Newton’s Second Law of Motion**  

Often written as $F = ma$. Since $a = \frac{d^2 x}{dt^2}$,

$$m\frac{d^2x}{dt^2} = F(x, t).$$

This is a **second-order** ODE. If $F$ depends only on $x$ and $t$ (and possibly $v = x'$), it may be nonlinear or linear (if $F$ is linear in $x$, $x'$, etc.).

II. **Population Dynamics**  

The logistic model:

$$\frac{dP}{dt} = rP \left(1 - \frac{P}{K}\right),$$
is a **first-order** **nonlinear** **autonomous** ODE describing population growth with a carrying capacity $K$.

III. **RC Circuit (First-Order Linear ODE)**  

Consider a resistor $R$ in series with a capacitor $C$. The voltage $V_C(t)$ across the capacitor satisfies:

$$C\frac{dV_C}{dt} + \frac{V_C(t)}{R} = \frac{V_{\text{in}}(t)}{R}.$$

Rearranged:

$$\frac{dV_C}{dt} + \frac{1}{RC}V_C(t) = \frac{V_{\text{in}}(t)}{RC}.$$

This is a first-order linear ODE.

### Applications

ODEs are ubiquitous in mathematical modeling across disciplines:

- **Quantum mechanics** uses the Schrödinger equation, which can reduce to ordinary differential equations in specific cases.  
- The motion of particles and rigid bodies is described by Newton's laws or through **Lagrangian/Hamiltonian formulations**, involving ordinary differential equations.  
- **System dynamics** and control theory rely on transfer functions and state-space models based on ordinary differential equations.  
- Electrical circuits, such as **RLC circuits** and operational amplifiers, are modeled using ordinary differential equations to describe voltage and current over time.  
- The spread of infectious diseases is modeled with the **SIR framework**, a system of ordinary differential equations for population groups.  
- **Biochemical reactions** are often described by the Michaelis–Menten equations, which are ordinary differential equations for reaction rates.  
- **Macroeconomic systems** use dynamical models to study growth and other phenomena through ordinary differential equations.  
- **Option pricing** models, while typically based on partial differential equations, can simplify to ordinary differential equations under certain assumptions.  
- **Chemical kinetics** describes reaction rates using ordinary differential equations for product formation.  

### Limitations and Complexities

- **Analytical solutions** often do not exist for many ordinary differential equations, especially nonlinear ones, requiring the use of numerical methods like Euler’s method and Runge–Kutta methods.  
- **High-order and nonlinear ODEs** become increasingly complex to solve, leading to reliance on qualitative methods such as stability analysis and phase-plane diagrams instead of closed-form solutions.  
- **Simplifying assumptions** underpin many ODE models, such as linearization or ignoring certain effects, but these assumptions can limit the solution's applicability when they do not hold.  
- **Parameter sensitivity** in real-world models means small changes in parameters can result in drastically different outcomes, as seen in chaotic systems.  
