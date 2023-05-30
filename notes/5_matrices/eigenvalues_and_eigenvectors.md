## Eigenvalues and Eigenvectors

- Eigenvalues and eigenvectors are important concepts in linear algebra and have many applications in different fields such as physics, computer graphics, machine learning, and more.
- They are used to decompose or simplify complex matrix transformations.

## Definitions

- An **eigenvector** of a square matrix **A** is a non-zero vector **v** such that when **A** multiplies **v**, the output is a scaled version of **v**. The scaling factor is the eigenvalue associated with that eigenvector.

Mathematically,

$$
A \mathbf{v} = \lambda \mathbf{v}
$$

where:
- **A** is a square matrix,
- **v** is an eigenvector of **A**,
- $\lambda$ is the corresponding eigenvalue.

## Procedure for Finding Eigenvalues and Eigenvectors

1. **Eigenvalues**: Solve the characteristic equation, which is obtained by setting up and solving the equation $|A - \lambda I| = 0$, where **I** is the identity matrix of the same dimension as **A**, and $|\cdot|$ denotes the determinant. The roots of this equation give the eigenvalues.

2. **Eigenvectors**: For each eigenvalue, find the corresponding eigenvectors by substituting the eigenvalue into the equation $(A - \lambda I)\mathbf{v} = 0$ and finding the null space. 

## Example

Consider a 2x2 matrix A = [[4, 1], [2, 3]]

1. Solve the characteristic equation $|A - \lambda I| = 0$, which gives $\lambda^2 - 7\lambda + 10 = 0$. The roots of this equation are $\lambda_1 = 2$ and $\lambda_2 = 5$, the eigenvalues.

2. To find the eigenvectors:
    - For $\lambda_1 = 2$, solve $(A - 2I)\mathbf{v} = 0$ to get the eigenvector $\mathbf{v_1} = [1, -2]^T$.
    - For $\lambda_2 = 5$, solve $(A - 5I)\mathbf{v} = 0$ to get the eigenvector $\mathbf{v_2} = [1, 1]^T$.

## Applications

- Used in Principal Component Analysis (PCA) for dimensionality reduction.
- Used in solving systems of linear differential equations.
- Used in quantum mechanics where eigenvalues and eigenvectors of operators represent measurable quantities.

## Caveats

- Not all matrices have eigenvalues and eigenvectors. For example, non-square matrices do not have them.
- Computation of eigenvalues and eigenvectors can be computationally expensive for large matrices.


