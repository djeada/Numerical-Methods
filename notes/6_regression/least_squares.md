## Least Squares Regression

Least Squares Regression is a fundamental technique in statistical modeling and data analysis used for fitting a model to observed data. The primary goal is to find a set of parameters that minimize the discrepancies (residuals) between the model’s predictions and the actual observed data. The "least squares" criterion is chosen because it leads to convenient mathematical properties and closed-form solutions, particularly for linear models.

In its simplest form, least squares regression is applied to **linear regression**, where we assume a linear relationship between a set of input variables (features) $X$ and an output variable $Y$. More generally, it can be extended to polynomial regression and multiple linear regression with multiple input variables. Because of its simplicity, transparency, and relative mathematical convenience, least squares remains one of the most widely used techniques in data analysis.

![output(31)](https://github.com/user-attachments/assets/3777f998-f72c-43a1-a8a9-8ecad0e82b1f)

### Mathematical Formulation

Given a matrix of features $X \in \mathbb{R}^{m \times n}$ (with $m$ observations and $n$ features), and a vector of target variables $Y \in \mathbb{R}^m$, we seek a coefficient vector $\beta \in \mathbb{R}^n$ that best fits the data in the sense of minimizing the sum of squared residuals. If we include a column of ones in $X$ to represent the intercept term, $\beta$ naturally includes the intercept as well.

We model:

$$\hat{Y} = X \beta$$

**Objective**: Minimize the Residual Sum of Squares (RSS):

$$RSS(\beta) = \| Y - X\beta \|_2^2 = (Y - X\beta)^\top (Y - X\beta)$$

The goal is to find $\beta$ that solves:

$$\min_\beta \| Y - X\beta \|_2^2$$

By setting the gradient of this objective with respect to $\beta$ to zero, we obtain the **Normal Equation**:

$$X^\top X \beta = X^\top Y$$

Provided $X^\top X$ is invertible, we have a closed-form solution:

$$\beta = (X^\top X)^{-1} X^\top Y$$

This $\beta$ is the least squares estimate of the coefficient vector, ensuring that the fitted line (or hyperplane, in the multi-dimensional case) is the best fit in the least squares sense.

### Derivation

I. **Set up the Problem**:

Suppose we have observations $\{ (x_i, y_i) \}_{i=1}^m$, where $x_i \in \mathbb{R}^n$ is a vector of features for the $i$-th observation and $y_i$ is the response. We assume a linear model:

$$\hat{y}_i = \sum_{j=1}^n \beta_j x_{ij} = x_i^\top \beta,$$
or in matrix form:

$$\hat{Y} = X\beta,$$
where $X$ is the $m \times n$ matrix with rows $x_i^\top$, and $Y \in \mathbb{R}^m$ is the vector of observed responses.

II. **Defining the Error to Minimize**:

We define the residuals as:

$$r = Y - X\beta$$

The objective is to minimize:

$$RSS(\beta) = r^\top r = (Y - X\beta)^\top (Y - X\beta)$$

III. **Finding the Minimum**:

To minimize with respect to $\beta$, take the gradient and set it to zero:

$$\frac{\partial RSS}{\partial \beta} = -2X^\top(Y - X\beta) = 0$$

This implies:

$$X^\top Y - X^\top X \beta = 0 \implies X^\top X \beta = X^\top Y$$

IV. **Solving the Normal Equation**:

If $X^\top X$ is invertible:

$$\beta = (X^\top X)^{-1} X^\top Y$$

This formula provides a closed-form solution for the ordinary least squares estimator $\beta$.

V. **Confirming the Minimum (Second-Derivative Check)**:

The Hessian (second derivative) of $RSS$ with respect to $\beta$ is:

$$\frac{\partial^2 RSS}{\partial \beta^2} = 2X^\top X$$

Since $X^\top X$ is positive semi-definite (and positive definite when $X$ has full column rank), the critical point found in step III is indeed a global minimum.

### Algorithm Steps

I. **Data Preparation**:

- Construct your design matrix $X$ by stacking the observations row-wise.  
- Each row corresponds to one observation and each column corresponds to one feature.  
- Often, a column of ones is added to incorporate the intercept term.
- Construct the response vector $Y$ from the observed target values.

II. **Compute Matrices**:

Compute $X^\top X$ and $X^\top Y$.

III. **Check Invertibility**:

- Ensure $X^\top X$ is invertible (or use a pseudo-inverse if not).
- If $X^\top X$ is not invertible, it may be due to multicollinearity. Consider removing or combining features, or use regularization methods (like Ridge or Lasso).

IV. **Solve for $\beta$**:

$$\beta = (X^\top X)^{-1} X^\top Y$$

V. **Use the Model for Prediction**:

For a new input $x_{\text{new}}$, predict:

$$\hat{y}_{\text{new}} = x_{\text{new}}^\top \beta$$

### Example

**Given Data Points**: $(x,y)$ = $(1,1), (2,2), (3,2)$.

**Step-by-step**:

I. Add an intercept term (column of ones):

$$X = \begin{bmatrix}
1 & 1 \\
1 & 2 \\
1 & 3 \\
\end{bmatrix}, \quad
Y=\begin{bmatrix}1 \\ 2 \\ 2\end{bmatrix}$$

II. Compute $X^\top X$ and $X^\top Y$:

$$X^\top X = \begin{bmatrix} 1+1+1 & 1+2+3 \\ 1+2+3 & 1+4+9 \end{bmatrix} = \begin{bmatrix} 3 & 6 \\ 6 & 14 \end{bmatrix}$$

$$X^\top Y = \begin{bmatrix} 1 \cdot 1 + 1 \cdot 2 + 1 \cdot 2 \\ 1 \cdot 1 + 2 \cdot 2 + 3 \cdot 2 \end{bmatrix} = \begin{bmatrix} 5 \\ 11 \end{bmatrix}$$

III. Invert $X^\top X$:

Compute the determinant:

$$\det(X^\top X) = 3 \cdot 14 - 6 \cdot 6 = 42 - 36 = 6$$

Compute the adjugate (swap diagonal entries and negate off-diagonal entries):

$$\text{adj}(X^\top X) = \begin{bmatrix} 14 & -6 \\ -6 & 3 \end{bmatrix}$$

Apply the inverse formula $A^{-1} = \frac{1}{\det(A)}\text{adj}(A)$:

$$(X^\top X)^{-1} = \frac{1}{6}\begin{bmatrix} 14 & -6 \\ -6 & 3 \end{bmatrix} = \begin{bmatrix} \frac{7}{3} & -1 \\ -1 & \frac{1}{2} \end{bmatrix}$$

IV. Compute $\beta$:

$$\beta = (X^\top X)^{-1}X^\top Y = \frac{1}{6}\begin{bmatrix} 14 & -6 \\ -6 & 3 \end{bmatrix}\begin{bmatrix} 5 \\ 11 \end{bmatrix} = \frac{1}{6}\begin{bmatrix} 70 - 66 \\ -30 + 33 \end{bmatrix} = \frac{1}{6}\begin{bmatrix} 4 \\ 3 \end{bmatrix} = \begin{bmatrix} \frac{2}{3} \\[4pt] \frac{1}{2} \end{bmatrix}$$

Thus, the fitted line is:

$$\hat{y} = \frac{2}{3} + \frac{1}{2}\,x$$

V. Verify at data points and compute residuals:

| $x$ | $y$ | $\hat{y}$ | Residual $(y - \hat{y})$ |
|-----|-----|-----------|--------------------------|
| 1 | 1 | $\frac{2}{3} + \frac{1}{2} = \frac{7}{6} \approx 1.167$ | $-\frac{1}{6} \approx -0.167$ |
| 2 | 2 | $\frac{2}{3} + 1 = \frac{5}{3} \approx 1.667$ | $\phantom{-}\frac{1}{3} \approx 0.333$ |
| 3 | 2 | $\frac{2}{3} + \frac{3}{2} = \frac{13}{6} \approx 2.167$ | $-\frac{1}{6} \approx -0.167$ |

VI. Compute the coefficient of determination ($R^2$):

Mean of observed values:

$$\bar{y} = \frac{1 + 2 + 2}{3} = \frac{5}{3}$$

Total Sum of Squares:

$$TSS = \sum_{i=1}^{3}(y_i - \bar{y})^2 = \left(1 - \frac{5}{3}\right)^2 + \left(2 - \frac{5}{3}\right)^2 + \left(2 - \frac{5}{3}\right)^2 = \frac{4}{9} + \frac{1}{9} + \frac{1}{9} = \frac{2}{3}$$

Residual Sum of Squares:

$$RSS = \sum_{i=1}^{3}(y_i - \hat{y}_i)^2 = \left(\frac{1}{6}\right)^2 + \left(\frac{1}{3}\right)^2 + \left(\frac{1}{6}\right)^2 = \frac{1}{36} + \frac{1}{9} + \frac{1}{36} = \frac{1}{6}$$

$$R^2 = 1 - \frac{RSS}{TSS} = 1 - \frac{1/6}{2/3} = 1 - \frac{1}{4} = \frac{3}{4} = 0.75$$

This means 75% of the variance in $Y$ is explained by the linear model.

VII. Prediction for a new input:

For $x_{\text{new}} = 4$:

$$\hat{y} = \frac{2}{3} + \frac{1}{2} \cdot 4 = \frac{2}{3} + 2 = \frac{8}{3} \approx 2.667$$

### Advantages

- **Closed-Form Solution**: Provides an explicit formula for the optimal parameters, enabling direct interpretation.
- **Efficient for Small Problems**: Works well with relatively small datasets and few features.
- **Foundational Method**: Forms the basis for many advanced regression techniques and regularized models.

### Limitations

- **Assumes Linearity**: The method presupposes a linear relationship between features and output.
- **Sensitive to Outliers**: Squared errors emphasize large errors more heavily, making the model sensitive to outliers.
- **Invertibility Issues**: If $X^\top X$ is not invertible, the standard formula fails. Issues like multicollinearity require either dropping features, transformations, or using regularized regression variants.
