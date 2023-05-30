## The power method

Let us have a square matrix A. It's size is $n \thinspace x \thinspace	n$.

It has a number of independet real eigenvalues: $\lambda_1, \lambda_2, \dots, \lambda_n$.

Eigenvectors corresponding to the eigenvalues are: $v_1, v_2, \dots, v_n$.

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
The reciprocals of the eigenvalues of A are the eigenvalues of it's inverse matrix  $A^{-1}$.

This will help us to find the smallest eigenvalue of A.

Instead of multiplying A as in power method, we multiply it's inverse to find it's largest value.

## Power Method

The power method is an algorithm for finding the largest eigenvalue in magnitude and the corresponding eigenvector of a matrix. It is a simple and efficient method used when a matrix is large and sparse.

## Key Concepts

- The power method uses iterative multiplication to progressively shift a vector towards the dominant eigenvector direction.
- It converges to the eigenvector corresponding to the largest eigenvalue in magnitude, given the largest eigenvalue is unique.

## Mathematical Formulation

Given a square matrix A and a vector x^(0), we perform repeated multiplication x^(k+1) = Ax^(k) / ||Ax^(k)||, where ||.|| denotes the norm. This is iterated until convergence, which occurs when the direction of x^(k) changes very little between iterations.

## Algorithm Steps

1. Initialize a vector x^(0) (often chosen randomly). 
2. Compute a new vector y^(k) = Ax^(k). 
3. Scale the vector to form x^(k+1) = y^(k) / ||y^(k)||. 
4. Repeat steps 2-3 until convergence, which is usually defined by ||x^(k+1) - x^(k)|| < ε for a very small ε.

## Example

Consider a matrix A = [[2, 1], [1, 3]]. Starting with an initial vector x^(0) = [1, 1], after several iterations of the power method, it will converge to the eigenvector corresponding to the largest eigenvalue of the matrix.

## Advantages

- Simple and efficient, especially for large, sparse matrices.
- Only requires matrix-vector multiplication, a relatively cheap operation for sparse matrices.

## Limitations

- Only finds the largest eigenvalue (in magnitude) and the corresponding eigenvector.
- Convergence can be slow if the ratio of the largest to the second-largest eigenvalue is close to 1.
- Does not work if the largest eigenvalue is not unique.

