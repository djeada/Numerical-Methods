
## QR method

The QR method is used to find all eigenvalues of a matrix, without finding the eigenvectors at the same time.\\

1. The eigenvalues and corresponding eigenvectors of similar matrices are the same.

Two square matrices A and B are similar if:

$$A = C^{-1}BC$$

where C is an invertible matrix.

2. You can present any matrix as a product of two other matrices. 

$$A = QR \quad (1)$$

Here we want to get an orthogonal matrix Q and an upper triangular matrix R.

A matrix M is an orthogonal matrix if: $M^{-1} = M^T$. Thus $M^*M = I$.

Let us rewrite equation (1):

$$RQ = Q^*AQ$$

$$RQ = Q^{-1}AQ$$ 

RQ has the same eigenvalues as A.

Compute a QR factorization and reverse the order of multiplcation of Q and R.

$A_0 = A$

$$A_k = R_kQ_k = Q^{-1}_kA_kQ_k$$

$$A_{k-1}=Q_kR_k$$

We will finally converge to an upper triangular matrix form as the iteration progresses:

$$
 A_k = R_kQ_k = \left[ {\begin{array}{ccc}
\lambda_1 & X & \dots & X\\
0 & \lambda_2 & \dots & X\\
\vdots & \vdots & \ddots &\vdots\\
0 & 0 & \dots & \lambda_n\\
  \end{array} } \right]
$$
