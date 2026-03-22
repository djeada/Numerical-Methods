## Gaussian Interpolation

**Gaussian Interpolation**, often associated with **Gauss’s forward and backward interpolation formulas**, is a technique that refines polynomial interpolation for equally spaced data points. Rather than building the interpolating polynomial from one end of the data interval (as Newton’s forward or backward formulas do), Gaussian interpolation centres the construction around a midpoint. This yields better accuracy when the target $x$ lies in the interior of the tabulated range rather than near its boundaries.

In essence, it is a re-indexing of Newton’s finite-difference interpolation that uses a “central” reference node and differences arranged symmetrically around it. By choosing the midpoint as the origin and shifting indices accordingly, the resulting formulas often produce more stable and accurate approximations for values near the centre of the data set.

Imagine you have a set of equally spaced points and corresponding function values:

![output(29)](https://github.com/user-attachments/assets/074c2f58-7d0a-44ac-b12f-cb43c9417bfc)

Newton’s forward or backward interpolation builds a polynomial starting from one end (like x_0 or x_n). Gaussian interpolation, however, selects a point near the center of the interval, say x_m (the midpoint), and builds the interpolation polynomial outward from this center. This symmetric approach can lead to a polynomial that better represents the function near that central area, potentially reducing error.

### Mathematical Formulation

Assume we have **equally spaced abscissae**

$$
x_0,x_1,x_2,\dots ,x_n, \qquad 
h = x_{i+1}-x_i (\text{constant step})
$$

Let the “mid-table’’ node be $x_m$ where

$$
m =
\begin{cases}
\dfrac{n}{2}, & n\ \text{even},\\
\dfrac{n-1}{2}, & n\ \text{odd}
\end{cases}
$$

 Shifted argument

To measure how far the interpolation point $x$ sits from the centre we introduce the dimensionless variable

$$
\boxed{t=\dfrac{x-x_m}{h}}
$$

Difference operators near the centre

*Forward* and *backward* first differences are

$$
\Delta y_i = y_{i+1}-y_i
$$

$$
\nabla y_i = y_i-y_{i-1}
$$

with higher‐order differences generated recursively, e.g.

$$\Delta^2 y_i = \Delta(\Delta y_i)=y_{i+2}-2y_{i+1}+y_i$$

For a central scheme we evaluate these differences on the rows immediately **adjacent to** $x_m$:

$$
\Delta y_{m-1}, \Delta y_m,  \Delta^2 y_{m-1}, \nabla y_{m+1},\ldots
$$

so that every term in the polynomial is as symmetric about $x_m$ as possible.

Gauss central formulas

| Variant | Best for | Interpolating polynomial |
| ------- | -------- | ------------------------ |
| **Gauss forward** | $t\ge 0$ | $\displaystyle f(x)\approx y_m + t\,\Delta y_m + \frac{t(t-1)}{2!}\,\Delta^{2} y_{m-1} + \frac{(t\!+\!1)\,t\,(t\!-\!1)}{3!}\,\Delta^{3} y_{m-1} + \frac{(t\!+\!1)\,t\,(t\!-\!1)(t\!-\!2)}{4!}\,\Delta^{4} y_{m-2} + \cdots$ |
| **Gauss backward** | $t< 0$ | $\displaystyle f(x)\approx y_m + t\,\Delta y_{m-1} + \frac{(t\!+\!1)\,t}{2!}\,\Delta^{2} y_{m-1} + \frac{(t\!+\!1)\,t\,(t\!-\!1)}{3!}\,\Delta^{3} y_{m-2} + \frac{(t\!+\!2)(t\!+\!1)\,t\,(t\!-\!1)}{4!}\,\Delta^{4} y_{m-2} + \cdots$ |

Both formulas are algebraically equivalent—they produce the **same** unique polynomial through all $n+1$ data points—but the ordering of the factorial products is arranged so that the truncation error is smallest when $|t|$ lies in the favourable range.

**General $k$-th term.**  Let $\Delta^k y_{b_k}$ denote the $k$-th forward difference at base index $b_k$:

| | Difference base index $b_k$ | Coefficient numerator (product of $k$ factors) |
|---|---|---|
| **Forward** | $m - \lfloor k/2 \rfloor$ | $\displaystyle\prod_{j\,=\,-\lfloor(k-1)/2\rfloor}^{\lfloor k/2\rfloor}(t-j)$ |
| **Backward** | $m - \lceil k/2 \rceil$ | $\displaystyle\prod_{j\,=\,-\lfloor k/2\rfloor}^{\lfloor(k-1)/2\rfloor}(t-j)$ |

Each coefficient is the product above divided by $k!$.

The forward formula follows a **zigzag** path through the difference table—right then alternately up-right: $\Delta y_m,\;\Delta^2 y_{m-1},\;\Delta^3 y_{m-1},\;\Delta^4 y_{m-2},\ldots$ The backward formula starts up-right then alternately right: $\Delta y_{m-1},\;\Delta^2 y_{m-1},\;\Delta^3 y_{m-2},\;\Delta^4 y_{m-2},\ldots$

### Derivation 

I.  **Equally-spaced data and difference operators**

Nodes and spacing

$$
x_i = x_0 + ih,\qquad h = x_{i+1}-x_i (\text{constant}),\qquad i=0,\dots n
$$

Function values

$$
y_i = f(x_i)
$$

Forward and backward differences

$$
\Delta y_i = y_{i+1}-y_i
$$

$$
\nabla y_i = y_i-y_{i-1}
$$

with higher orders obtained recursively, e.g.

$$
\Delta^{2}y_i = \Delta(\Delta y_i)=y_{i+2}-2y_{i+1}+y_i, \quad
\nabla^{2}y_i = \nabla(\nabla y_i)=y_i-2y_{i-1}+y_{i-2}
$$

and so on.

II. **Choosing the central origin and defining the reduced argument**

Pick the index

$$
m =
\begin{cases}
   n/2, & n\text{ even},\\[4pt]
   (n-1)/2, & n\text{ odd}.
\end{cases}
\qquad\Longrightarrow\qquad x_m\approx\text{mid-table}
$$

Introduce the dimensionless distance of the target point $x$ from the centre:

$$
t = \dfrac{x-x_m}{h}.
$$

> $t=0$ at the centre, $t=\pm1$ exactly one grid step away, etc.

III.  **Deriving the Gauss formulas via Newton’s divided-difference formula**

The key insight is that both Gauss formulas follow from Newton’s divided-difference interpolation by choosing a specific ordering of the data points around the centre.

**Newton’s divided-difference formula.** For any ordering of the nodes $x_{i_0}, x_{i_1}, x_{i_2}, \ldots$ the interpolating polynomial can be written

$$
f(x) = f[x_{i_0}] + (x-x_{i_0})\,f[x_{i_0},x_{i_1}] + (x-x_{i_0})(x-x_{i_1})\,f[x_{i_0},x_{i_1},x_{i_2}] + \cdots
$$

Because divided differences are symmetric, the ordering does not change the final polynomial—only the structure of the intermediate terms.

**Equally-spaced simplification.** With step $h$ the divided differences reduce to forward differences:

$$
f[x_i,x_{i+1},\ldots,x_{i+k}]=\frac{\Delta^{k}y_i}{k!\,h^{k}}
$$

and the product of $x$-factors becomes a product in $t$:

$$
(x-x_j) = (t - j^{\prime})\,h,
\qquad j^{\prime}=\frac{x_j-x_m}{h}
$$

**Gauss forward ordering.** Incorporate nodes in the order $x_m,x_{m+1},x_{m-1},x_{m+2},x_{m-2},\ldots$:

$$
\begin{aligned}
k=1:&\quad (x-x_m) = t\,h
  &&\Longrightarrow \frac{t}{1!}\,\Delta y_m \\
k=2:&\quad (x-x_m)(x-x_{m+1}) = t(t-1)\,h^{2}
  &&\Longrightarrow \frac{t(t-1)}{2!}\,\Delta^{2}y_{m-1} \\
k=3:&\quad \cdots\times(x-x_{m-1}) = t(t-1)(t+1)\,h^{3}
  &&\Longrightarrow \frac{(t+1)\,t\,(t-1)}{3!}\,\Delta^{3}y_{m-1} \\
k=4:&\quad \cdots\times(x-x_{m+2}) = t(t-1)(t+1)(t-2)\,h^{4}
  &&\Longrightarrow \frac{(t+1)\,t\,(t-1)(t-2)}{4!}\,\Delta^{4}y_{m-2}
\end{aligned}
$$

giving the **Gauss forward central formula**:

$$
\boxed{f(x)\approx y_m + t\,\Delta y_m + \frac{t(t-1)}{2!}\Delta^2 y_{m-1} + \frac{(t+1)\,t\,(t-1)}{3!}\Delta^3 y_{m-1} + \frac{(t+1)\,t\,(t-1)(t-2)}{4!}\Delta^4 y_{m-2} + \cdots}
$$

**Gauss backward ordering.** Incorporate nodes as $x_m,x_{m-1},x_{m+1},x_{m-2},x_{m+2},\ldots$:

$$
\begin{aligned}
k=1:&\quad (x-x_m) = t\,h
  &&\Longrightarrow \frac{t}{1!}\,\Delta y_{m-1} \\
k=2:&\quad (x-x_m)(x-x_{m-1}) = t(t+1)\,h^{2}
  &&\Longrightarrow \frac{(t+1)\,t}{2!}\,\Delta^{2}y_{m-1} \\
k=3:&\quad \cdots\times(x-x_{m+1}) = t(t+1)(t-1)\,h^{3}
  &&\Longrightarrow \frac{(t+1)\,t\,(t-1)}{3!}\,\Delta^{3}y_{m-2} \\
k=4:&\quad \cdots\times(x-x_{m-2}) = t(t+1)(t-1)(t+2)\,h^{4}
  &&\Longrightarrow \frac{(t+2)(t+1)\,t\,(t-1)}{4!}\,\Delta^{4}y_{m-2}
\end{aligned}
$$

giving the **Gauss backward central formula**:

$$
\boxed{f(x)\approx y_m + t\,\Delta y_{m-1} + \frac{(t+1)\,t}{2!}\Delta^2 y_{m-1} + \frac{(t+1)\,t\,(t-1)}{3!}\Delta^3 y_{m-2} + \frac{(t+2)(t+1)\,t\,(t-1)}{4!}\Delta^4 y_{m-2} + \cdots}
$$

**Complexity and error**

* **Computational cost.** Building the full difference table for $n+1$ points requires $O(n^{2})$ additions. Evaluating the truncated series to order $k$ then takes $O(k)$ multiplications and additions, so the total work is dominated by the table construction.
* **Truncation error.** If the series is truncated after the $k$-th difference term, the remainder has the same form as in Newton’s formula: $R_k=O(h^{k+1}f^{(k+1)}(\xi))$ for some $\xi$ in the data interval. Because the differences are centred, the leading error coefficient is typically smaller than for the end-based Newton formulas when $|t|<1$.
* **Round-off.** Central factorial products $t(t\!\pm\!1)(t\!\mp\!1)\cdots$ stay moderate in magnitude for $|t|\le 1$, so subtractive cancellation is less severe than when large binomial-like coefficients multiply small differences.

IV.  **Why the factorial products look symmetric**

* Each coefficient in the forward (or backward) series is a **central factorial** such as $t(t-1),\ (t+1)t(t-1),\ldots$. These arise automatically from the alternating node ordering $x_m, x_{m\pm1}, x_{m\mp1},\ldots$
* The difference rows used—$\Delta y_m, \Delta^{2}y_{m-1}, \Delta^{3}y_{m-1}, \ldots$ for the forward formula, or $\Delta y_{m-1}, \Delta^{2}y_{m-1}, \Delta^{3}y_{m-2}, \ldots$ for the backward—step out symmetrically from the centre, so the truncated polynomial minimises the error for any $x$ with $|t|\lesssim 1$ (i.e.\ near the middle of the table).
* In the limit $t\to0$ both polynomials reduce to $f(x_m)$ as expected; as $|t|$ approaches 1 they smoothly match Newton’s ordinary forward/backward formulas, ensuring continuity across the entire tabulated interval.

### Algorithm Steps

**Input**

Equally spaced nodes and ordinates

$$\{(x_i,y_i)\}_{i=0}^{n},\quad y_i=f(x_i)$$

with step $h=x_{i+1}-x_i$ and a target abscissa $x$ that lies inside the table.

I. **Identify the central reference row**

Locate the mid-index**

$$
m=
\begin{cases}
   n/2, & n\ \text{even},\\[4pt]
   (n-1)/2, & n\ \text{odd}.
\end{cases}
$$

Hence $x_m$ is as close as possible to the table’s midpoint.

Reduced argument

$$
t=\dfrac{x-x_m}{h}.
$$

**Decide forward vs. backward form**

* If $t\ge 0$ (the target lies to the **right** of the centre) → use the **Gauss–forward** polynomial;
* if $t<0$ (to the **left**) → use **Gauss–backward**.

II. **Build the central-difference table**

Set up the usual forward-difference triangle for $y_0,y_1,\dots ,y_n$.

Extract the rows you will need:

| order | forward form uses   | backward form uses  |
| ----- | ------------------- | ------------------- |
| 1st   | $\Delta y_{m}$      | $\Delta y_{m-1}$    |
| 2nd   | $\Delta^{2}y_{m-1}$ | $\Delta^{2}y_{m-1}$ |
| 3rd   | $\Delta^{3}y_{m-1}$ | $\Delta^{3}y_{m-2}$ |
| 4th   | $\Delta^{4}y_{m-2}$ | $\Delta^{4}y_{m-2}$ |
| …     | …                   | …                   |

Only as many orders as you intend to keep are required.

III. **Insert $t$ and the differences into Gauss’s formula**

Forward ( $t\ge 0$ )

$$
f(x)\approx
y_m
+t\,\Delta y_{m}
+\frac{t(t-1)}{2!}\,\Delta^{2}y_{m-1}
+\frac{(t+1)\,t\,(t-1)}{3!}\,\Delta^{3}y_{m-1}
+\frac{(t+1)\,t\,(t-1)(t-2)}{4!}\,\Delta^{4}y_{m-2}
+\cdots
$$

Backward ( $t<0$ )

$$
f(x)\approx
y_m
+t\,\Delta y_{m-1}
+\frac{(t+1)\,t}{2!}\,\Delta^{2}y_{m-1}
+\frac{(t+1)\,t\,(t-1)}{3!}\,\Delta^{3}y_{m-2}
+\frac{(t+2)(t+1)\,t\,(t-1)}{4!}\,\Delta^{4}y_{m-2}
+\cdots
$$

IV. **Accumulate the series to the desired order**

Evaluate the terms sequentially and keep a running sum.

Stopping criterion options:

* truncate after a pre-chosen order $k$;
* or stop when $|\text{next term}|<\varepsilon$ for a tolerance $\varepsilon$.
  
The resulting sum is the interpolated value $\displaystyle \hat f(x)$.

> **Accuracy tip:** for points with $|t|\le 1$ the first three or four terms usually give error of the same order as the fourth or fifth finite difference, so adding higher orders seldom pays off unless the data are extremely smooth.

**Output**

$$
\boxed{ \hat f(x)=\text{sum obtained in Step IV}}
$$

This algorithm preserves every assumption explicitly (equal spacing, central index, choice of $t$) and shows exactly where each quantity enters the computation.

### Example

**Given data (step $h=1$)**

| $i$ | $x_i$ | $y_i=f(x_i)$ |
| --- | ----- | ------------ |
| 0   | 0     | 2.0          |
| 1   | 1     | 3.5          |
| 2   | 2     | 5.0          |
| 3   | 3     | 5.8          |
| 4   | 4     | 6.0          |

We wish to interpolate $f(1.5)$

I. **Choose the central row and reduced argument**

* Mid-index $m=2 \to x_m = 2$.
* Reduced distance from the centre

$$
t=\frac{x-x_m}{h}= \frac{1.5-2}{1}= -0.5.
$$

Because $t<0$ the **Gauss-backward** polynomial is appropriate.

II.  **Construct the needed central differences**

Forward-difference table (only rows required by the formula are shown):

| order | symbol                                                          | value  |
| ----- | --------------------------------------------------------------- | ------ |
| 0     | $y_m$                                                           | $5.0$  |
| 1     | $\Delta y_{m-1}=y_2-y_1$                                        | $1.5$  |
| 2     | $\Delta^{2}y_{m-1}= \Delta y_{2}-\Delta y_{1}=0.8-1.5$          | $-0.7$ |
| 3     | $\Delta^{3}y_{m-2}= \Delta^{2}y_{1}-\Delta^{2}y_{0}= -0.7-0$    | $-0.7$ |
| 4     | $\Delta^{4}y_{m-2}= \Delta^{3}y_{1}-\Delta^{3}y_{0}=0.1-(-0.7)$ | $0.8$  |

Full differences: $\Delta y_0=1.5,\ \Delta y_1=1.5,\ \Delta y_2=0.8,\ \Delta y_3=0.2$;

$\Delta^{2}y_0=0,\ \Delta^{2}y_1=-0.7,\ \Delta^{2}y_2=-0.6$;

$\Delta^{3}y_0=-0.7,\ \Delta^{3}y_1=0.1$.

III.  **Insert $t$ and differences into the Gauss-backward series**

$$
f(x)\approx y_m + t\,\Delta y_{m-1} + \frac{(t+1)\,t}{2!}\,\Delta^2y_{m-1} + \frac{(t+1)\,t\,(t-1)}{3!}\,\Delta^3y_{m-2} + \frac{(t+2)(t+1)\,t\,(t-1)}{4!}\,\Delta^4y_{m-2}
$$

Plug in $t=-0.5$ and the table values:

| term                                                                                        | numerical value |
| ------------------------------------------------------------------------------------------- | --------------- |
| $y_m$                                                                                       | $5.0000$        |
| $t\,\Delta y_{m-1}=(-0.5)(1.5)$                                                             | $-0.7500$       |
| $\dfrac{(t+1)\,t}{2}\,\Delta^{2}y_{m-1}= \dfrac{(0.5)(-0.5)}{2}(-0.7)$                       | $0.0875$       |
| $\dfrac{(t+1)\,t\,(t-1)}{6}\,\Delta^{3}y_{m-2}= \dfrac{(0.5)(-0.5)(-1.5)}{6}(-0.7)$             | $-0.0438$       |
| $\dfrac{(t+2)(t+1)\,t\,(t-1)}{24}\,\Delta^{4}y_{m-2}= \dfrac{(1.5)(0.5)(-0.5)(-1.5)}{24}(0.8)$ | $0.0188$       |

IV. **Accumulate the series**

Up to 3rd-order term:

$$
f(1.5)\approx5.0000-0.7500+0.0875-0.0438 = 4.2937
$$

Including the 4th-order term:

$$
f(1.5)\approx4.2937+0.0188= \boxed{4.3125}.
$$

> **Verification:** This is the unique polynomial interpolant through all five data points. The same result is produced by `scipy.interpolate.BarycentricInterpolator` and by evaluating the degree-4 Newton forward formula from $x_0$, confirming correctness.

**Comparison with simple linear interpolation**

Using only the two nearest neighbours $f(1)=3.5$ and $f(2)=5.0$:

$$
f_{\text{linear}}(1.5)=\frac{3.5+5.0}{2}=4.25.
$$

The Gaussian result $f(1.5)\approx4.3125$ is slightly higher because the higher-order differences capture the concavity of the data (the increments $\Delta y_i$ are decreasing). Linear interpolation ignores this curvature entirely, illustrating why a central-difference polynomial can be substantially more accurate when more data points are available.

### Advantages

* **Higher accuracy near the table centre** – because the polynomial is built sym­metrically around the midpoint, truncation error is smaller whenever the target $x$ lies roughly one step to either side of that centre, often outperforming Newton’s end-based forward/backward formulas.
* **Better numerical stability** – central factorial terms such as $t(t\!\pm\!1)$ keep successive coefficients similar in magnitude, reducing round-off amplification compared with the large binomial factors that appear when you measure everything from an end point.
* **Seamless extension of Newton’s schemes** – the table of ordinary forward differences can be reused; you merely “fold” it around the middle row and read off the required $\Delta$ or $\nabla$ values, so implementation effort is modest if a difference table already exists.

### Disadvantages

* **Requires equal spacing** – the classic Gauss forward/backward formulas rely on a constant step $h$; with uneven $x_i$ the method does not apply without re-derivation or switching to divided-difference polynomials.
* **Extra bookkeeping** – one must identify the correct central row, decide forward vs. backward form, and track which difference (e.g.\ $\Delta^{3}y_{m-2}$ or $\nabla^{3}y_{m+2}$) feeds each term; this is more fiddly than the straight left-to-right pattern of Newton’s forward series.
* **No particular benefit away from the centre** – if the target $x$ is closer to an end of the table $(|t|\gg1)$, Gauss’s central formula reverts in effect to the ordinary Newton formulas but with more complicated indexing, so you gain little (and may lose stability if you retain unnecessary terms).
