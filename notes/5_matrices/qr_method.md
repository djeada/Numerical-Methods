## QR Method

The QR method is a numerical method that is used to calculate all eigenvalues of a matrix, without necessarily obtaining the eigenvectors at the same time.

## Key Concepts

- The QR method involves an iterative process of matrix factorization and transformation.
- The process leverages the property that similar matrices have the same eigenvalues.

## Mathematical Formulation

1. Given a square matrix $A$, it is possible to represent it as the product of two matrices - an orthogonal matrix $Q$ and an upper triangular matrix $R$.

$$
A = QR
$$

where a matrix $M$ is orthogonal if its inverse is equal to its transpose, i.e., $M^{-1} = M^T$ or $M^TM = I$.

2. Two matrices $A$ and $B$ are considered similar if they can be expressed as:

$$
A = C^{-1}BC
$$

where $C$ is an invertible matrix. Notably, similar matrices have the same eigenvalues.

3. The QR method applies these two concepts iteratively to obtain a matrix $A_k$ which is similar to $A$ but closer to upper triangular form. This is done by reversing the order of multiplication of $Q$ and $R$ after each QR factorization:

$$
A_0 = A
$$

$$
A_k = R_kQ_k = Q^{-1}_kA_kQ_k
$$

Note: $A_{k-1} = Q_kR_k$.

4. This process will eventually converge to an upper triangular matrix, where the eigenvalues of the original matrix $A$ can be read off from the diagonal:

$$
A_k = R_kQ_k = \left[ {\begin{array}{ccc}
\lambda_1 & X & \dots & X\\
0 & \lambda_2 & \dots & X\\
\vdots & \vdots & \ddots &\vdots\\
0 & 0 & \dots & \lambda_n\\
\end{array} } \right]
$$

## Algorithm Steps

1. Start with the initial square matrix $A$.

2. Compute the QR factorization of $A$ using the Gram-Schmidt process, Householder reflections, or Givens rotations to get matrices $Q$ and $R$ such that $A = QR$.

For example, in the Gram-Schmidt process, we take the columns of $A$ and convert them into an orthogonal basis. Suppose $A = [a_1, a_2, ..., a_n]$, the columns of $Q$ are obtained by:

$$
q_1 = \frac{a_1}{\|a_1\|}, \quad q_2 = \frac{a_2 - (q_1^Ta_2)q_1}{\|a_2 - (q_1^Ta_2)q_1\|}, \quad \dots, \quad q_n = \frac{a_n - \sum_{j=1}^{n-1} (q_j^Ta_n)q_j}{\|a_n - \sum_{j=1}^{n-1} (q_j^Ta_n)q_j\|}
$$

Matrix $R$ is then an upper triangular matrix that's computed by $R = Q^TA$.

3. Recompute $A$ as $A = RQ$.

4. Repeat steps 2 and 3 until $A$ converges to an upper triangular form.

5. The diagonal elements of the resulting matrix will be the eigenvalues of the original matrix.

## Example

Consider a 2x2 matrix $A$ given by:

$$
A = 
\begin{bmatrix}
4 & 1 \\
2 & 3
\end{bmatrix}
$$

1. Compute the QR factorization of $A$.

Start by taking the first column as $a_1$. Normalize it to get the first column of $Q$:

$$
q_1 = \frac{a_1}{\|a_1\|} = \frac{1}{\sqrt{20}}\begin{bmatrix}4\\2\end{bmatrix} = \begin{bmatrix}0.8944\\0.4472\end{bmatrix}
$$

Next, orthogonalize the second column of $A$ relative to $q_1$ to get $a_2'$:

$$
a_2' = a_2 - (q_1^Ta_2)q_1 = \begin{bmatrix}1\\3\end{bmatrix} - (\begin{bmatrix}0.8944 & 0.4472\end{bmatrix} \begin{bmatrix}1\\3\end{bmatrix})\begin{bmatrix}0.8944\\0.4472\end{bmatrix} = \begin{bmatrix}-0.8944\\2.2361\end{bmatrix}
$$

Normalize $a_2'$ to get the second column of $Q$:

$$
q_2 = \frac{a_2'}{\|a_2'\|} = \frac{1}{\sqrt{6}}\begin{bmatrix}-0.8944\\2.2361\end{bmatrix} = \begin{bmatrix}-0.3651\\0.9309\end{bmatrix}
$$

This gives us matrix $Q$:

$$
Q = 
\begin{bmatrix}
0.8944 & -0.3651 \\
0.4472 & 0.9309
\end{bmatrix}
$$

Now, compute $R = Q^TA$:

$$
R = 
\begin{bmatrix}
0.8944 & 0.4472 \\
-0.3651 & 0.9309
\end{bmatrix}^T 
\begin{bmatrix}
4 & 1 \\
2 & 3
\end{bmatrix} =
\begin{bmatrix}
4.4721 & 1.7889 \\
0 & 2.2361
\end{bmatrix}
$$

2. Recompute $A$ as $A = RQ$:

$$
A = 
\begin{bmatrix}
4.4721 & 1.7889 \\
0 & 2.2361
\end{bmatrix}
\begin{bmatrix}
0.8944 & -0.3651 \\
0.4472 & 0.9309
\end{bmatrix} =
\begin{bmatrix}
4 & 1 \\
2 & 3
\end{bmatrix}
$$

This result should be equal to the initial $A$. If not, repeat the process until $A$ converges to an upper triangular matrix. The process converges for this example in the first step itself. The diagonal elements of the resulting matrix $A$ will be the eigenvalues of the original matrix.

## Advantages

- The QR method is effective for finding all eigenvalues of a matrix.
- It is numerically stable and converges quickly in most cases.

## Limitations

- The QR method does not directly compute the eigenvectors.
- While it is generally stable and efficient, the QR method may still be slower for very large matrices than some alternatives.
