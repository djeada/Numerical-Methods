##  Linear systems

Let's consider a following system of equations:

$$
\begin{eqnarray*}
  -x + 5y &=& 12 \\
   x - 7y &=& 35
\end{eqnarray*} 
$$

Those equations can be also written in a matrix form:

$$
\left(
  \begin{array}{rr}
    -1 & 5 \\
    1 & -7  \\
  \end{array}
\right)\left(
  \begin{array}{c}
    x \\
    y \\
  \end{array}
\right) = \left(
  \begin{array}{c}
    12 \\
    35 \\
  \end{array}
\right)
$$

Generally we can have any number of variables:

$$
\left(
  \begin{array}{cccc}
    A_{11} & A_{12} & \dots & A_{1n} \\
    A_{21} & A_{22} & \dots & A_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    A_{n1} & A_{n2} & \dots & A_{nn} \\
  \end{array}
\right)\left(
         \begin{array}{c}
           x_1 \\
           x_2 \\
           \vdots \\
           x_n \\
         \end{array}
       \right)  = \left(
                   \begin{array}{c}
                     b_1 \\
                     b_2 \\
                     \vdots \\
                     b_n \\
                   \end{array}
                 \right)
$$
