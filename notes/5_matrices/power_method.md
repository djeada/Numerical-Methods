## Power Method

The power method is a fundamental iterative algorithm for estimating the eigenvalue of largest magnitude and its associated eigenvector for a given matrix. This technique is particularly appealing when dealing with large and sparse matrices, where direct eigenvalue computations (e.g., via the characteristic polynomial) are computationally expensive or numerically unstable. The power method capitalizes on the property that repeated multiplication by a matrix $A$ will cause any initial vector to align with the direction of the eigenvector associated with the dominant eigenvalue, assuming this eigenvalue is well-separated from the others in magnitude.

![power_method](https://github.com/user-attachments/assets/e48ec2b5-fd18-4886-a4b9-497c73aae0de)

- The power method **iteratively** refines a vector to approximate the eigenvector associated with the dominant eigenvalue.
- It is particularly **efficient** for large and sparse matrices since it only requires matrix-vector multiplications.
- Convergence is ensured when the largest eigenvalue in magnitude is **unique** and well-separated from the next largest.
- The method starts with an initial **guess** vector, which is repeatedly multiplied by the matrix to approach the dominant eigenvector.
- **Normalization** of the vector at each step prevents numerical overflow or underflow during the iterations.
- The rate of **convergence** depends on the ratio between the dominant eigenvalue and the second-largest eigenvalue in magnitude.
- The power method can be **extended** to find multiple eigenvalues by deflating the matrix after each dominant eigenvalue is found.
- It is widely used in applications such as Google's PageRank algorithm to determine the importance of web pages.

### Mathematical Formulation

Given an $n \times n$ matrix $A$ and an initial guess $x^{(0)}$, the power method iterates as follows:

I. Compute:

$$y^{(k)} = A x^{(k)}$$

II. Normalize:

$$x^{(k+1)} = \frac{y^{(k)}}{\|y^{(k)}\|}$$

These steps are repeated until convergence. Convergence occurs when the vector $x^{(k)}$ no longer changes significantly between iterations or equivalently, when successive eigenvalue approximations stabilize.

### Inverse Power Method for the Smallest Eigenvalue

If we are interested in finding the smallest eigenvalue of $A$, we can use the inverse power method. The eigenvalues of $A^{-1}$ are the reciprocals of the eigenvalues of $A$. Thus, applying the power method to $A^{-1}$ instead of $A$ will yield the eigenvector associated with the smallest eigenvalue of $A$, and the inverse of the dominant eigenvalue of $A^{-1}$ will give us the smallest eigenvalue of $A$.

### Derivation

Suppose $A$ has distinct eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_n$ arranged so that:

$$|\lambda_1| > |\lambda_2| \geq \cdots \geq |\lambda_n|.$$

Let $v_1, v_2, \dots, v_n$ be the corresponding eigenvectors forming a basis. Any initial vector $x^{(0)}$ can be written as:

$$x^{(0)} = c_1 v_1 + c_2 v_2 + \cdots + c_n v_n, \quad \text{with } c_1 \neq 0.$$

Applying $A$ repeatedly:

$$A x^{(0)} = c_1 \lambda_1 v_1 + c_2 \lambda_2 v_2 + \cdots + c_n \lambda_n v_n.$$

After $k$ iterations:

$$A^k x^{(0)} = c_1 \lambda_1^k v_1 + c_2 \lambda_2^k v_2 + \cdots + c_n \lambda_n^k v_n.$$

As $k \to \infty$, because $|\lambda_1| > |\lambda_j|$ for $j > 1$, the terms involving $\lambda_j^k$ vanish in comparison to $\lambda_1^k$. Therefore:

$$\frac{A^k x^{(0)}}{\|A^k x^{(0)}\|} \to v_1$$

and the Rayleigh quotient $\frac{x^{(k)T} A x^{(k)}}{x^{(k)T} x^{(k)}}$ tends to $\lambda_1$. 

Thus, the power method converges to the dominant eigenvector $v_1$ and eigenvalue $\lambda_1$.

### Algorithm Steps

I. **Initialize**: Choose an initial vector $x^{(0)}$ (random or based on domain knowledge).

II. **Iterative Step**: For $k=0,1,2,\dots$:

- Compute $y^{(k)} = A x^{(k)}$.
- Normalize $x^{(k+1)} = \frac{y^{(k)}}{\|y^{(k)}\|}$.

III. **Convergence Check**: Stop when $\|x^{(k+1)} - x^{(k)}\|$ is sufficiently small, or when changes in the estimated eigenvalue become negligible.

IV. **Eigenvalue Approximation**: Once converged, estimate the dominant eigenvalue as:

$$\lambda_{\text{max}} \approx \frac{x^{(k)T} A x^{(k)}}{x^{(k)T} x^{(k)}}.$$

### Example

Consider:

$$A = \begin{bmatrix}2 & 1 \\ 1 & 3\end{bmatrix}, \quad x^{(0)} = \begin{bmatrix}1 \\ 1\end{bmatrix}.$$

**First iteration**:

$$y^{(0)} = A x^{(0)} = \begin{bmatrix}2 & 1 \\ 1 & 3\end{bmatrix}\begin{bmatrix}1 \\ 1\end{bmatrix} = \begin{bmatrix}3 \\ 4\end{bmatrix}.$$

Normalize:

$$x^{(1)} = \frac{1}{5}\begin{bmatrix}3 \\ 4\end{bmatrix} = \begin{bmatrix}0.6 \\ 0.8\end{bmatrix}.$$

**Second iteration**:

$$y^{(1)} = A x^{(1)} = \begin{bmatrix}2 & 1 \\ 1 & 3\end{bmatrix}\begin{bmatrix}0.6 \\ 0.8\end{bmatrix} = \begin{bmatrix}2.0 \\ 3.0\end{bmatrix}.$$

Normalize:

$$x^{(2)} = \frac{1}{\sqrt{2^2 + 3^2}}\begin{bmatrix}2 \\ 3\end{bmatrix} = \begin{bmatrix}0.5547 \\ 0.8321\end{bmatrix}.$$

Repeating these steps, $x^{(k)}$ converges to the eigenvector associated with the largest eigenvalue, which in this case is approximately 3.5616. The corresponding eigenvector stabilizes around:

$$\begin{bmatrix}0.55 \\ 0.83\end{bmatrix}$$

### Advantages

- The algorithm is **straightforward** to implement, making it accessible for various applications.
- It is **beneficial** for large and sparse matrices since it only requires matrix-vector multiplication.
- The method maintains a **low** memory footprint by only storing the current vector and its transformation.

### Limitations

- The power method can find only the **largest** eigenvalue in magnitude, not all eigenvalues.
- Convergence may be **slow** if the magnitudes of the first and second eigenvalues are close.
- The method **requires** a unique largest eigenvalue to ensure convergence to a single eigenvector.
