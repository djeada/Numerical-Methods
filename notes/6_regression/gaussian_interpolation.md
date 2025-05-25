## Gaussian Interpolation

**Gaussian Interpolation**, often associated with **Gauss’s forward and backward interpolation formulas**, is a technique that refines the approach of polynomial interpolation when data points are equally spaced. Instead of using the Newton forward or backward interpolation formulas directly from one end of the data interval, Gaussian interpolation centers the interpolation around a midpoint of the data set. This approach can provide better accuracy when the point at which we need to interpolate lies somewhere in the "interior" of the given data points rather than near the boundaries.

In essence, Gaussian interpolation is a variant of Newton’s divided difference interpolation but employs a "central" reference point and finite differences structured around a central node. By choosing a midpoint as a reference and using appropriately shifted indices, Gaussian interpolation formulas often yield more stable and accurate approximations for values near the center of the data set.

Imagine you have a set of equally spaced points and corresponding function values:

![output(29)](https://github.com/user-attachments/assets/074c2f58-7d0a-44ac-b12f-cb43c9417bfc)

Newton’s forward or backward interpolation builds a polynomial starting from one end (like x_0 or x_n). Gaussian interpolation, however, selects a point near the center of the interval, say x_m (the midpoint), and builds the interpolation polynomial outward from this center. This symmetric approach can lead to a polynomial that better represents the function near that central area, potentially reducing error.

### Mathematical Formulation

Assume we have **equally spaced abscissae**

$$
x_0,x_1,x_2,\dots ,x_n, \qquad 
h = x_{i+1}-x_i (\text{constant step}).
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
\boxed{t=\dfrac{x-x_m}{h}}.
$$

Difference operators near the centre

*Forward* and *backward* first differences are

$$
\Delta y_i = y_{i+1}-y_i, 
$$

$$
\nabla y_i = y_i-y_{i-1},
$$

with higher‐order differences generated recursively, e.g.
$\Delta^2 y_i = \Delta(\Delta y_i)=y_{i+2}-2y_{i+1}+y_i$.

For a central scheme we evaluate these differences on the rows immediately **adjacent to** $x_m$:

$$
\Delta y_{m-1}, \Delta y_m,  \Delta^2 y_{m-1}, \nabla y_{m+1},\ldots
$$

so that every term in the polynomial is as symmetric about $x_m$ as possible.

Gauss central formulas

| Variant                                                  | Interpolating polynomial                                                                                                                              |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gauss forward**<br>(row just **left** of the centre)   | $\displaystyle f(x)\approx y_m + t\Delta y_{m-1} + \frac{t(t-1)}{2!}\Delta^{2} y_{m-1} + \frac{t(t+1)(t-1)}{3!}\Delta^{3} y_{m-2} + \cdots$ |
| **Gauss backward**<br>(row just **right** of the centre) | $\displaystyle f(x)\approx y_m + t\nabla y_{m+1} + \frac{t(t+1)}{2!}\nabla^{2} y_{m+1} + \frac{t(t+1)(t-1)}{3!}\nabla^{3} y_{m+2} + \cdots$ |

* The factorial products $t(t\!\pm\!1)(t\!\mp\!1)\ldots$ mirror the binomial coefficients that arise when the Newton forward/backward polynomial is **re-indexed** so that $x_m$ is treated as the origin.
* Each successive term draws its difference from one step farther away, preserving symmetry and minimising round-off error when $x$ lies near the mid-range.

By recasting Newton’s formulas about the central node and writing everything in powers of $t$, Gauss’s forward/backward polynomials provide a more accurate—and numerically stable—interpolant whenever the desired $x$ is closer to the middle of the tabulated data than to either end.

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
\Delta y_i = y_{i+1}-y_i,
$$

$$
\nabla y_i = y_i-y_{i-1}
$$

with higher orders obtained recursively, e.g.

$$
\Delta^{2}y_i = \Delta(\Delta y_i)=y_{i+2}-2y_{i+1}+y_i, \quad
\nabla^{2}y_i = \nabla(\nabla y_i)=y_i-2y_{i-1}+y_{i-2},
$$

and so on.

II.  **Choosing the central origin and defining the reduced argument**

Pick the index

  $$
  m =
  \begin{cases}
     n/2, & n\text{ even},\\[4pt]
     (n-1)/2, & n\text{ odd},
  \end{cases}
  \qquad\Longrightarrow\qquad x_m\approx\text{mid-table}.
  $$

* Introduce the dimensionless distance of the target point $x$ from the centre:

  $$
  t = \dfrac{x-x_m}{h}.
  $$

  > $t=0$ at the centre, $t=\pm1$ exactly one grid step away, etc.

III.  **Re-expanding Newton’s forward/backward polynomial about $x_m$**

1. **Start from Newton’s forward series with base row $x_{m-1}$ (one step left of the centre):**

   $$
   f(x)
   = y_{m-1}
     + p\Delta y_{m-1}
     + \frac{p(p-1)}{2!}\Delta^{2}y_{m-1}
     + \frac{p(p-1)(p-2)}{3!}\Delta^{3}y_{m-1}
     + \cdots ,
   $$

   where $p = \dfrac{x-x_{m-1}}{h}=t+1$.

2. **Rewrite every occurrence of $p$ in terms of $t$.**
   Because $p = t+1$,

   $$
   \begin{aligned}
   p &= t+1,\\
   p(p-1) &= (t+1)t, \\
   p(p-1)(p-2) &= (t+1)t(t-1),\quad\text{etc.}
   \end{aligned}
   $$

3. **Shift the constant term from $y_{m-1}$ to $y_m$.**
   Note that $y_m = y_{m-1} + \Delta y_{m-1}$.
   Substitute $y_{m-1}=y_m-\Delta y_{m-1}$ into the series and regroup.
   After cancelling like terms one obtains the **Gauss forward central formula**

   $$
   \boxed{%
   f(x)\approx
   y_m
   + t\Delta y_{m-1}
   + \frac{t(t-1)}{2!}\Delta^{2}y_{m-1}
   + \frac{t(t+1)(t-1)}{3!}\Delta^{3}y_{m-2}
   + \cdots }.
   $$

4. **Analogous manipulation starting from Newton’s backward series one row to the right of the centre ($x_{m+1}$) yields**

   $$
   \boxed{%
   f(x)\approx
   y_m
   + t\nabla y_{m+1}
   + \frac{t(t+1)}{2!}\nabla^{2}y_{m+1}
   + \frac{t(t+1)(t-1)}{3!}\nabla^{3}y_{m+2}
   + \cdots }.
   $$

These are precisely **Gauss’s forward and backward central-difference polynomials**.

IV.  **Why the factorial products look symmetric**

* Each coefficient in the forward (or backward) series is now a **central factorial** such as
  $t(t-1), t(t+1)(t-1),\ldots$.
  These arise automatically when you substitute $p=t\pm1$ and regroup.

* The difference rows used—$\Delta y_{m-1}, \Delta^{2}y_{m-1}, \Delta^{3}y_{m-2}, \ldots$ on the left,
  or $\nabla y_{m+1}, \nabla^{2}y_{m+1}, \ldots$ on the right—step out symmetrically from the centre, so the truncated polynomial minimises the error for any $x$ with $|t|\lesssim 1$ (i.e.\ near the middle of the table).

* In the limit $t\to0$ both polynomials reduce to $f(x_m)$ as expected; as $|t|$ approaches 1 they smoothly match Newton’s ordinary forward/backward formulas, ensuring continuity across the entire tabulated interval.


### Algorithm Steps — fully detailed, one-by-one

---

**Input**

* equally spaced nodes and ordinates
  $\{(x_i,y_i)\}_{i=0}^{n}, y_i=f(x_i)$ with step $h=x_{i+1}-x_i$;
* a target abscissa $x$ that lies inside the table.

---

#### I. Identify the central reference row

1. **Locate the mid-index**

   $$
   m=
   \begin{cases}
      n/2, & n\ \text{even},\\[4pt]
      (n-1)/2, & n\ \text{odd}.
   \end{cases}
   $$

   Hence $x_m$ is as close as possible to the table’s midpoint.
2. **Reduced argument**

   $$
   t=\dfrac{x-x_m}{h}.
   $$
3. **Decide forward vs. backward form**
   *If $t<0$* (the target lies to the **left** of the centre) → use the **Gauss–forward** polynomial;
   *if $t>0$* (to the **right**) → use **Gauss–backward**.

---

#### II. Build the central-difference table

1. Set up the usual forward-difference triangle for $y_0,y_1,\dots ,y_n$.
2. Extract the rows you will need:

   | order | forward form uses   | backward form uses  |
   | ----- | ------------------- | ------------------- |
   | 1st   | $\Delta y_{m-1}$    | $\nabla y_{m+1}$    |
   | 2nd   | $\Delta^{2}y_{m-1}$ | $\nabla^{2}y_{m+1}$ |
   | 3rd   | $\Delta^{3}y_{m-2}$ | $\nabla^{3}y_{m+2}$ |
   | …     | …                   | …                   |

   Only as many orders as you intend to keep are required.

---

#### III. Insert $t$ and the differences into Gauss’s formula

*Forward ( $t<0$ )*

$$
f(x)\approx
y_m
+t\Delta y_{m-1}
+\frac{t(t-1)}{2!}\Delta^{2}y_{m-1}
+\frac{t(t+1)(t-1)}{3!}\Delta^{3}y_{m-2}
+\cdots
$$

*Backward ( $t>0$ )*

$$
f(x)\approx
y_m
+t\nabla y_{m+1}
+\frac{t(t+1)}{2!}\nabla^{2}y_{m+1}
+\frac{t(t+1)(t-1)}{3!}\nabla^{3}y_{m+2}
+\cdots
$$

---

#### IV. Accumulate the series to the desired order

1. Evaluate the terms sequentially and keep a running sum.
2. **Stopping criterion options**

   * truncate after a pre-chosen order $k$;
   * or stop when $|\text{next term}|<\varepsilon$ for a tolerance $\varepsilon$.
3. The resulting sum is the interpolated value $\displaystyle \hat f(x)$.

> **Accuracy tip:** for points with $|t|\le 1$ the first three or four terms usually give error of the same order as the fourth or fifth finite difference, so adding higher orders seldom pays off unless the data are extremely smooth.

---

**Output**

$$
\boxed{ \hat f(x)=\text{sum obtained in Step IV}}
$$

This algorithm preserves every assumption explicitly (equal spacing, central index, choice of $t$) and shows exactly where each quantity enters the computation.


### Example — fully worked numeric illustration

**Given data (step $h=1$)**

| $i$ | $x_i$ | $y_i=f(x_i)$ |
| --- | ----- | ------------ |
| 0   | 0     | 2.0          |
| 1   | 1     | 3.5          |
| 2   | 2     | 5.0          |
| 3   | 3     | 5.8          |
| 4   | 4     | 6.0          |

We wish to interpolate $f(1.5)$.

---

#### I.  Choose the central row and reduced argument

* Mid-index $m=2\Rightarrowx_m = 2$.
* Reduced distance from the centre

$$
t=\frac{x-x_m}{h}= \frac{1.5-2}{1}= -0.5.
$$

Because $t<0$ the **Gauss-forward** (left-hand) polynomial is appropriate.

---

#### II.  Construct the needed central differences

Forward‐difference table (only rows required by the formula are shown):

| order | symbol                                                          | value  |
| ----- | --------------------------------------------------------------- | ------ |
| 0     | $y_m$                                                           | $5.0$  |
| 1     | $\Delta y_{m-1}=y_2-y_1$                                        | $1.5$  |
| 2     | $\Delta^{2}y_{m-1}= \Delta y_{2}-\Delta y_{1}=0.8-1.5$          | $-0.7$ |
| 3     | $\Delta^{3}y_{m-2}= \Delta^{2}y_{1}-\Delta^{2}y_{0}= -0.7-0$    | $-0.7$ |
| 4     | $\Delta^{4}y_{m-2}= \Delta^{3}y_{1}-\Delta^{3}y_{0}=0.1-(-0.7)$ | $0.8$  |

*(Full differences: $\Delta y_0=1.5,\ \Delta y_1=1.5,\ \Delta y_2=0.8,\ \Delta y_3=0.2$;
$\Delta^{2}y_0=0,\ \Delta^{2}y_1=-0.7,\ \Delta^{2}y_2=-0.6$;
$\Delta^{3}y_0=-0.7,\ \Delta^{3}y_1=0.1$.)*

---

#### III.  Insert $t$ and differences into the Gauss-forward series

$$
\begin{aligned}
f(x) \approx
& y_m
+ t\Delta y_{m-1}
+ \frac{t(t-1)}{2!}\Delta^{2}y_{m-1}\\
& + \frac{t(t+1)(t-1)}{3!}\Delta^{3}y_{m-2}
+ \frac{t(t+1)(t-1)(t-2)}{4!}\Delta^{4}y_{m-2}.
\end{aligned}
$$

Plug in $t=-0.5$ and the table values:

| term                                                                                        | numerical value |
| ------------------------------------------------------------------------------------------- | --------------- |
| $y_m$                                                                                       | $5.0000$        |
| $t\Delta y_{m-1}=(-0.5)(1.5)$                                                             | $-0.7500$       |
| $\dfrac{t(t-1)}{2}\Delta^{2}y_{m-1}= \dfrac{(-0.5)(-1.5)}{2}(-0.7)$                       | $-0.2625$       |
| $\dfrac{t(t+1)(t-1)}{6}\Delta^{3}y_{m-2}= \dfrac{(-0.5)(0.5)(-1.5)}{6}(-0.7)$             | $-0.0438$       |
| $\dfrac{t(t+1)(t-1)(t-2)}{24}\Delta^{4}y_{m-2}= \dfrac{(-0.5)(0.5)(-1.5)(-2.5)}{24}(0.8)$ | $-0.0313$       |

#### IV.  Accumulate the series

* Up to 3rd-order term:

  $$
  f(1.5)\approx5.0000-0.7500-0.2625-0.0438
             = 3.9437.
  $$

* Including the 4th-order term:

  $$
  f(1.5)\approx3.9437-0.0313= \boxed{3.9124}.
  $$

Adding still higher orders would change the value by only a few $10^{-3}$ here, so
$f(1.5)\approx3.91$ is a good Gaussian-interpolated estimate based on the given table.

> **Check:**  The estimate lies between the tabulated $f(1)=3.5$ and $f(2)=5.0$, closer to the latter—as expected for $x=1.5$.

### Advantages

* **Higher accuracy near the table centre** – because the polynomial is built sym­metrically around the midpoint, truncation error is smaller whenever the target $x$ lies roughly one step to either side of that centre, often outperforming Newton’s end-based forward/backward formulas.
* **Better numerical stability** – central factorial terms such as $t(t\!\pm\!1)$ keep successive coefficients similar in magnitude, reducing round-off amplification compared with the large binomial factors that appear when you measure everything from an end point.
* **Seamless extension of Newton’s schemes** – the table of ordinary forward differences can be reused; you merely “fold” it around the middle row and read off the required $\Delta$ or $\nabla$ values, so implementation effort is modest if a difference table already exists.

### Disadvantages

* **Requires equal spacing** – the classic Gauss forward/backward formulas rely on a constant step $h$; with uneven $x_i$ the method does not apply without re-derivation or switching to divided-difference polynomials.
* **Extra bookkeeping** – one must identify the correct central row, decide forward vs. backward form, and track which difference (e.g.\ $\Delta^{3}y_{m-2}$ or $\nabla^{3}y_{m+2}$) feeds each term; this is more fiddly than the straight left-to-right pattern of Newton’s forward series.
* **No particular benefit away from the centre** – if the target $x$ is closer to an end of the table $(|t|\gg1)$, Gauss’s central formula reverts in effect to the ordinary Newton formulas but with more complicated indexing, so you gain little (and may lose stability if you retain unnecessary terms).
t, there may be no significant advantage over standard methods.
