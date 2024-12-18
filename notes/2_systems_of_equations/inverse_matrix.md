## Matrix Inverse

The inverse of a matrix A is denoted as A^-1. It is a unique matrix such that when it is multiplied by the original matrix A, the result is the identity matrix I. Mathematically, this is expressed as:

$$
AA^{-1} = A^{-1}A = I
$$

Not all matrices have an inverse. Only square matrices (those with the same number of rows and columns) are eligible to have an inverse, and even then, some do not. A matrix has an inverse if and only if it is non-singular, i.e., its determinant is not zero.

### Mathematical Formulation

Given a square matrix A of order n, the inverse A^-1 is calculated as:

$$
A^{-1} = \frac{1}{det(A)} adj(A)
$$

where det(A) is the determinant of A and adj(A) is the adjugate of A.

The adjugate of A is the transpose of the cofactor matrix C of A. Each element c_ij of C is calculated as (-1)^(i+j) det(M_ij), where M_ij is the (i, j)th minor of A.

### Using inverse matrix to solve matrix equations

We can solve a following matrix equation, using a matrix invers:

$$ A\boldsymbol{x}=\boldsymbol{b} $$

Let's mutiply both sides by the inverse of the matrix $A$:

$$ \implies A^{-1}A\boldsymbol{x} = A^{-1}\boldsymbol{b} $$

$$ \implies I\boldsymbol{x} = A^{-1}\boldsymbol{b} $$

$$ \implies \boldsymbol{x} = A^{-1}\boldsymbol{b} $$

### Algorithm Steps

Finding the inverse of a matrix is a multi-step process:

1. Check if the matrix is invertible. A matrix is invertible if it is square (has the same number of rows and columns) and its determinant is not zero. If the matrix is not invertible, stop here, the matrix does not have an inverse.
2. Calculate the matrix of minors. The minor of each element in the matrix is the determinant of the matrix formed by removing the row and column of that element from the original matrix.
3. Form the matrix of cofactors. Multiply each minor by (-1)^(i+j), where i and j are the row and column numbers of each element.
4. Calculate the adjugate of the matrix. The adjugate is simply the transpose of the cofactor matrix.
5. Finally, the inverse of the original matrix is the adjugate divided by the determinant of the original matrix.

### Example

Let's take a 2x2 matrix A as an example:

$$
A = \begin{bmatrix} 4 & 7 \\ 
2 & 6\\ \end{bmatrix}
$$

1. First, check if the matrix is invertible. The determinant of A is (4*6 - 7*2) = 10, which is not zero, so the matrix is invertible.
2. The minor of 4 is the determinant of the matrix that results from removing the row and column of 4 from A, which is just 6. Similarly, the minor of 7 is 2, the minor of 2 is 7, and the minor of 6 is 4.
3. The cofactor matrix is obtained by multiplying each minor by (-1)^(i+j). For a 2x2 matrix, this results in the same matrix, as (-1)^(i+j) is 1 for all elements.
4. The adjugate of A is the transpose of the cofactor matrix, which is the same in this case because A is a 2x2 matrix.
5. The inverse of A is the adjugate divided by the determinant, resulting in:

$$
A^{-1} = \frac{1}{10} \begin{bmatrix} 6 & -7 \\ 
-2 & 4\\ \end{bmatrix} = \begin{bmatrix} 0.6 & -0.7 \\ 
-0.2 & 0.4\\ \end{bmatrix}
$$

### Advantages

- The inverse of a matrix is a powerful concept in linear algebra, offering a way to analytically solve systems of linear equations, among other things.

### Limitations

- Not all matrices have an inverse. Only non-singular square matrices can be inverted.
- Computing the inverse of a matrix involves calculating determinants and is therefore computationally expensive. For large matrices, numerical methods are often more efficient.

