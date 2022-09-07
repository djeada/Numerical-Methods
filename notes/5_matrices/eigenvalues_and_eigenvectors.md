## The power method

Let us have a square matrix A. It's size is $nxn$. \\
It has a number of independet real eigenvalues: $\lambda_1, \lambda_2, \dots, \lambda_n$. \\
Eigenvectors corresponding to the eigenvalues are: $v_1, v_2, \dots, v_n$. \\
One condition: $|\lambda_1| > |\lambda_2|$.

The eigenvectors are independent, which means that they are as well basis vectors. This implies that any vector in the same space can be written as a linear combination of the eigenvectors.

$$x_0 = c_1v_1+c_2v_2+\dots+c_nv_n$$

where $c_1\ne0$

After multypling both sides by matrix A:

$$Ax_0 = c_1Av_1+c_2Av_2+\dots+c_nAv_n$$

From the defintion $Av_i = \lambda{v_i}$, so:

$$Ax_0 = c_1\lambda_1v_1+c_2\lambda_2v_2+\dots+c_n\lambda_nv_n$$

$$Ax_0 = c_1\lambda_1[v_1+\frac{c_2}{c_1}\frac{\lambda_2}{\lambda_1}v_2+\dots+\frac{c_n}{c_1}\frac{\lambda_n}{\lambda_1}v_n]= c_1\lambda_1x_1$$

This was the first iteration. To begin the second iteration, we multiply $A$ by $x_1$:

$$Ax_1 = \lambda_1{v_1}+\frac{c_2}{c_1}\frac{\lambda_2^2}{\lambda_1}v_2+\dots+\frac{c_n}{c_1}\frac{\lambda_n^2}{\lambda_1}v_n$$

$$Ax_1 = \lambda_1[v_1+\frac{c_2}{c_1}\frac{\lambda_2^2}{\lambda_1^2}v_2+\dots+\frac{c_n}{c_1}\frac{\lambda_n^2}{\lambda_1^2}v_n] = \lambda_1x_2$$

After k iterations we have:

$$Ax_{k-1} = \lambda_1[v_1+\frac{c_2}{c_1}\frac{\lambda_2^k}{\lambda_1^k}v_2+\dots+\frac{c_n}{c_1}\frac{\lambda_n^k}{\lambda_1^k}v_n] = \lambda_1x_k$$


For large k, $(\frac{\lambda_n}{\lambda_1})^{k} = 0$

We have now the largest eigenvalue and its corresponding eigenvector:

$$Ax_{k-1} = {\lambda_1}v_1$$

## The inverse power method
The reciprocals of the eigenvalues of A are the eigenvalues of it's inverse matrix  $A^{-1}$. \\
This will help us to find the smallest eigenvalue of A. \\
Instead of multiplying A as in power method, we multiply it's inverse to find it's largest value.

## QR method

The QR method is used to find all eigenvalues of a matrix, without finding the eigenvectors at the same time.\\

1. The eigenvalues and corresponding eigenvectors of similar matrices are the same.

Two square matrices A and B are similar if:

$$A = C^{-1}BC$$

where C is an invertible matrix.\\

2. You can present any matrix as a product of two other matrices. 

\begin{align}
A &= QR
\end{align}

Here we want to get an orthogonal matrix Q and an upper triangular matrix R.\\

A matrix M is an orthogonal matrix if: $M^{-1} = M^T$. Thus $M^*M = I$. \\

Let us rewrite equation (1):

$$RQ = Q^*AQ$$

$$RQ = Q^{-1}AQ$$ 

RQ has the same eigenvalues as A.\\

Compute a QR factorization and reverse the order of multiplcation of Q and R.

$A_0 = A$

$$A_k = R_kQ_k = Q^{-1}_kA_kQ_k$$

$$A_{k-1}=Q_kR_k$$

```math
U = \left[ {\begin{array}{cc}
    1 & 0 & 0 \\
    1 & 1 & 0 \\
    0 & 1 & 1 \\
    0 & 0 & 1
  \end{array} } \right]
```

We will finally converge to an upper triangular matrix form as the iteration progresses:


```math
 A_k = R_kQ_k = \left[ {\begin{array}{ccc}
\lambda_1 & X & \dots & X\\
0 & \lambda_2 & \dots & X\\
& &\dots &\\
0 & 0 & \dots & \lambda_n\\
  \end{array} } \right]
```
