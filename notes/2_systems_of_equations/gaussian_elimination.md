# Gaussian Elimination

Gaussian elimination solves a linear system by applying elementary row operations to its augmented matrix. Each operation preserves the solution set while eliminating a coefficient below a pivot. The process produces an upper-triangular system, which can be solved from the last equation upward by back substitution when the pivots are usable and the solution is unique. The same row-operation framework also helps determine matrix rank and can be extended to compute an inverse. For singular or rectangular systems, row-echelon structure reveals whether equations are dependent or inconsistent, rather than necessarily producing one solution vector.

From a conceptual viewpoint, Gaussian elimination provides a structured approach to eliminating unknowns step-by-step. Geometrically, each linear equation represents a hyperplane in $n$-dimensional space, and the solution of the system corresponds to the intersection point(s) of these hyperplanes. Gaussian elimination successively "clears out" the variables, enabling a direct path to the solution (or revealing inconsistencies or infinite solution sets if they exist).

![Eliminating coefficients to obtain a triangular linear system](https://github.com/user-attachments/assets/54011276-5a17-4666-8fbf-91d92ee9c30e)

## Mathematical formulation

Consider a system of $n$ linear equations with $n$ unknowns:

$$
A\mathbf{x} = \mathbf{b},
$$
where

$$
A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n}\\
a_{21} & a_{22} & \cdots & a_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{bmatrix}
$$

$$
\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ \cdots \\ x_n \end{bmatrix}
$$

$$
\mathbf{b} = \begin{bmatrix} b_1 \\ b_2 \\ \cdots \\ b_n \end{bmatrix}
$$

We form the augmented matrix $[A|\mathbf{b}]$:

$$
[A|\mathbf{b}] = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\
a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn} & b_n
\end{bmatrix}
$$

The goal of Gaussian elimination is to perform a series of row operations to transform $[A|\mathbf{b}]$ into an upper-triangular form:

$$
[U|\mathbf{c}] = \begin{bmatrix}
u_{11} & u_{12} & \cdots & u_{1n} & c_1 \\
0 & u_{22} & \cdots & u_{2n} & c_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \cdots & u_{nn} & c_n
\end{bmatrix}
$$

where $U$ is an upper-triangular matrix. Once in this form, the solution $\mathbf{x}$ can be found by back substitution.

## Derivation

The derivation of Gaussian elimination closely mirrors the logic of systematic elimination of variables from a set of equations:

**Step 1: Elimination of $x_1$ from equations 2 through $n$.**

Suppose the first pivot (the leading element in the first row) is $a_{11}$. By using row operations, we can eliminate the $x_1$-term from all equations below the first. This is achieved by subtracting suitable multiples of the first row from subsequent rows.

**Step 2: Elimination of $x_2$ from equations 3 through $n$.**

After the first step, the second row now has a leading coefficient (pivot) in the second column. Using this pivot, we eliminate the $x_2$-term from all equations below the second.

**Step 3: Continue this process.** until the last pivot $a_{nn}$ (in the $n$-th row) is in place. If at any stage a pivot is zero, we interchange rows (partial pivoting) to bring a nonzero pivot into the pivot position.

The end result is an upper-triangular system that can be solved starting from the last equation and moving upward (back substitution).

### Elimination multipliers and pivoting

At stage $k$, for an unnormalized pivot row, set $m_{ik}=a_{ik}/a_{kk}$ for each $i>k$ and perform

$$
R_i\leftarrow R_i-m_{ik}R_k,\qquad b_i\leftarrow b_i-m_{ik}b_k.
$$

The same row operation must act on the right-hand side to preserve the solution set. Dividing the pivot row by its pivot first is an equivalent convention; the component formulas below use that normalized form.

Partial pivoting selects the largest available magnitude in the current column **before** dividing. For example, $\begin{bmatrix}0&1\\1&1\end{bmatrix}$ is nonsingular but has a zero first pivot; swapping its rows lets elimination proceed. A tiny pivot can similarly create large multipliers and amplify rounding, even when it is not exactly zero.

In exact arithmetic, a reduced row $[0\ \cdots\ 0\mid c]$ with $c\ne0$ proves inconsistency. A zero coefficient row with zero right-hand side introduces a redundant equation; if fewer than $n$ independent pivots remain in a consistent square system, free variables produce infinitely many solutions. Numerical singularity uses a scale-dependent threshold rather than an exact determinant test, so a software rejection can also indicate a nearly singular problem.

For dense matrices, factorization costs about $2n^3/3$ floating point operations, while a triangular solve costs $O(n^2)$. This distinction leads directly to storing and reusing an [LU factorization](lu_decomposition.md).

## Algorithm steps

**Input**: An augmented matrix $[A|\mathbf{b}]$ representing the system $A\mathbf{x} = \mathbf{b}$.

**Output**: A solution vector $\mathbf{x}$ if the system has a unique solution. In general the procedure can also reveal no solution or infinitely many solutions (a zero row in the reduced matrix). The implementation handles square systems only and returns just $\mathbf{x}$ (not the triangular matrix); when no usable pivot is found (the largest candidate is not larger than $n\,\varepsilon_{\text{mach}}\max_{ij}|a_{ij}|$) it raises an error for a singular or nearly singular matrix, without distinguishing "no solution" from "infinitely many". The helper `solve_gaussian_elimination` additionally rounds the result to 8 decimals.

**Step-by-Step Procedure**:

**Step 1: Form the augmented matrix.**

$$
[A|\mathbf{b}] = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\
a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn} & b_n
\end{bmatrix}
$$

**Step 2: Forward elimination.** (to reach upper-triangular form):

For $i = 1$ to $n$:

II.I. **Partial Pivoting (always performed by the implementation)**: Find the row (pivotRow) below (and including) the current row $i$ that has the largest absolute value in column $i$. Swap the current row $i$ with pivotRow to reduce numerical instability.

II.II. **Pivot Normalization**: Divide the entire $i$-th row by $a_{ii}$ (the pivot) to make the pivot element equal to 1.

II.III. **Elimination**: For each row $j > i$, subtract $a_{ji}$ times the $i$-th row from the $j$-th row to make the elements below the pivot zero.

After these steps, the matrix is in row echelon form:

$$
[U|\mathbf{c}] = \begin{bmatrix}
1 & * & \cdots & * & * \\
0 & 1 & \cdots & * & * \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \cdots & 1 & *
\end{bmatrix}
$$

where $*$ represents arbitrary numbers obtained during the process.

**Step 3: Back substitution.**

Starting from the last equation:

For $i = n$ down to 1:

$$
x_i = c_i - \sum_{k=i+1}^{n} u_{ik} x_k.
$$

Since $u_{ii}=1$ after normalization, $x_i$ can be directly computed. (If not normalized, divide by $u_{ii}$.)

This process yields the solution vector $\mathbf{x}$.

## Example

**Given System**:

$$
\begin{aligned}
  2x + y - z &= 8, \\
  -3x - y + 2z &= -11, \\
  -2x + y + 2z &= -3.
\end{aligned}
$$

**Step 1: Augmented matrix.**

$$
[A|\mathbf{b}] = \begin{bmatrix}
2 & 1 & -1 & 8 \\
-3 & -1 & 2 & -11 \\
-2 & 1 & 2 & -3
\end{bmatrix}
$$

**Step 2: Forward elimination.**

For this hand calculation, retain the original row order to keep the fractions simple; the implementation with partial pivoting would swap rows 1 and 2 first and reach the same solution by different intermediate matrices. The first pivot in this unpivoted calculation is $a_{11}=2$. Normalize the first row by dividing by 2:

$$
\begin{bmatrix}
1 & 0.5 & -0.5 & 4 \\
-3 & -1 & 2 & -11 \\
-2 & 1 & 2 & -3
\end{bmatrix}
$$

Eliminate $x$-terms in row 2 and row 3 using row 1:
For row 2: Add 3 times row 1:

$$
(3)R_1 + R_2 \to R_2 \implies
R_2 = \begin{bmatrix}
0 & 0.5 & 0.5 & 1
\end{bmatrix}
$$

For row 3: Add 2 times row 1:

$$
(2)R_1 + R_3 \to R_3 \implies
R_3 = \begin{bmatrix}
0 & 2 & 1 & 5
\end{bmatrix}
$$

Now the matrix is:

$$
\begin{bmatrix}
1 & 0.5 & -0.5 & 4 \\
0 & 0.5 & 0.5 & 1 \\
0 & 2 & 1 & 5
\end{bmatrix}
$$

Next pivot is $a_{22} = 0.5$. Normalize the second row by dividing by 0.5:

$$
\begin{bmatrix}
1 & 0.5 & -0.5 & 4 \\
0 & 1 & 1 & 2 \\
0 & 2 & 1 & 5
\end{bmatrix}
$$

Eliminate below the second pivot:

For row 3: subtract 2 times row 2 from row 3:

$$
R_3 - 2R_2 \implies R_3 = \begin{bmatrix}
0 & 0 & -1 & 1
\end{bmatrix}
$$

Now the matrix is in upper-triangular form:

$$
[U|\mathbf{c}] = \begin{bmatrix}
1 & 0.5 & -0.5 & 4 \\
0 & 1 & 1 & 2 \\
0 & 0 & -1 & 1
\end{bmatrix}
$$

**Step 3: Back substitution.**

From the last equation: $-1 \cdot z = 1 \implies z = -1$.
Substitute $z = -1$ into second equation:

$y + 1(-1) = 2 \implies y = 3$.

Substitute $y = 3, z = -1$ into first equation:

$x + 0.5(3) -0.5(-1) = 4 \implies x + 1.5 + 0.5 = 4 \implies x = 2$.

The solution is $\mathbf{x} = (2, 3, -1)^\top$.

## Advantages

- Gaussian elimination has **general applicability** to any $n \times n$ system of linear equations, and the general procedure can also identify cases where no solution or infinitely many solutions exist, including non-square systems (the implementation in this repository handles square systems only and reports a singular matrix as an error).
- The method serves as a **foundation for advanced techniques** like LU decomposition and QR decomposition, forming a building block for many numerical algorithms.
- It can be used to **determine the rank of a matrix** and to compute the inverse of a matrix when applicable by applying the procedure to the augmented matrix $[A | I]$.

## Limitations

- **Numerical instability** is a concern due to roundoff errors, particularly without pivoting. Partial or full pivoting mitigates this issue but may require additional computational steps.
- The method’s **computational cost**, proportional to $O(n^3)$ operations, can become prohibitive for large-scale systems, making it less efficient than iterative methods for such cases.
- A **zero pivot element** halts the process unless row interchanges are performed. Pivoting is necessary to avoid division by zero and to maintain algorithmic stability.
