## Gaussian elimination

To solve a linear system of equations, the Gaussian elimination approach is just a systematic application of the concept of equation substitution.

The first step is to put a matrix with coeeficients (A) and vector with values into one so called "augmented matrix".

$$
\begin{eqnarray*}
  -x + 5y &=& 12 \\
   x - 7y &=& 35
\end{eqnarray*} 
$$

$$
[A|\boldsymbol{b}] = 
\left[
  \begin{array}{rr|r}
    -1 & 5 & 12 \\
    1 & -7 & 35  \\
  \end{array}
\right]
$$

Now our goal is to convert this matrix to it's upper triangular form. We can achieve that by performing any of the following operations:

* Swap two rows.

* Multiply a row by a scalar that is not zero.

* Subtraction of a (non-zero) multiple of one row by a multiple of another.
