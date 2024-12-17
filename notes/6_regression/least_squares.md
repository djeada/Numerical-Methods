## Introduction

Least Squares Regression is a fundamental technique in statistical modeling and data analysis used for fitting a model to observed data. The primary goal is to find a set of parameters that minimize the discrepancies (residuals) between the model’s predictions and the actual observed data. The "least squares" criterion is chosen because it leads to convenient mathematical properties and closed-form solutions, particularly for linear models.

In its simplest form, least squares regression is applied to **linear regression**, where we assume a linear relationship between a set of input variables (features) \(X\) and an output variable \(Y\). More generally, it can be extended to polynomial regression and multiple linear regression with multiple input variables. Because of its simplicity, transparency, and relative mathematical convenience, least squares remains one of the most widely used techniques in data analysis.


## Mathematical Formulation

Given a matrix of features \( X \in \mathbb{R}^{m \times n} \) (with \( m \) observations and \( n \) features), and a vector of target variables \( Y \in \mathbb{R}^m \), we seek a coefficient vector \(\beta \in \mathbb{R}^n\) that best fits the data in the sense of minimizing the sum of squared residuals. If we include a column of ones in \( X \) to represent the intercept term, \(\beta\) naturally includes the intercept as well.

We model:
\[
\hat{Y} = X \beta.
\]

**Objective**: Minimize the Residual Sum of Squares (RSS):
\[
RSS(\beta) = \| Y - X\beta \|_2^2 = (Y - X\beta)^\top (Y - X\beta).
\]

The goal is to find \(\beta\) that solves:
\[
\min_\beta \| Y - X\beta \|_2^2.
\]

By setting the gradient of this objective with respect to \(\beta\) to zero, we obtain the **Normal Equation**:
\[
X^\top X \beta = X^\top Y.
\]

Provided \( X^\top X \) is invertible, we have a closed-form solution:
\[
\beta = (X^\top X)^{-1} X^\top Y.
\]

This \(\beta\) is the least squares estimate of the coefficient vector, ensuring that the fitted line (or hyperplane, in the multi-dimensional case) is the best fit in the least squares sense.


## Derivation

1. **Set up the Problem**:

   Suppose we have observations \(\{ (x_i, y_i) \}_{i=1}^m\), where \( x_i \in \mathbb{R}^n \) is a vector of features for the \(i\)-th observation and \( y_i \) is the response. We assume a linear model:
   \[
   \hat{y}_i = \sum_{j=1}^n \beta_j x_{ij} = x_i^\top \beta,
   \]
   or in matrix form:
   \[
   \hat{Y} = X\beta,
   \]
   where \( X \) is the \( m \times n \) matrix with rows \( x_i^\top \), and \( Y \in \mathbb{R}^m \) is the vector of observed responses.

2. **Defining the Error to Minimize**:

   We define the residuals as:
   \[
   r = Y - X\beta.
   \]

   The objective is to minimize:
   \[
   RSS(\beta) = r^\top r = (Y - X\beta)^\top (Y - X\beta).
   \]

3. **Finding the Minimum**:

   To minimize with respect to \(\beta\), take the gradient and set it to zero:
   \[
   \frac{\partial RSS}{\partial \beta} = -2X^\top(Y - X\beta) = 0.
   \]

   This implies:
   \[
   X^\top Y - X^\top X \beta = 0 \implies X^\top X \beta = X^\top Y.
   \]

4. **Solving the Normal Equation**:

   If \( X^\top X \) is invertible:
   \[
   \beta = (X^\top X)^{-1} X^\top Y.
   \]

   This formula provides a closed-form solution for the ordinary least squares estimator \(\beta\).


## Algorithm Steps

1. **Data Preparation**:
   - Construct your design matrix \( X \) by stacking the observations row-wise.  
   - Each row corresponds to one observation and each column corresponds to one feature.  
   - Often, a column of ones is added to incorporate the intercept term.
   - Construct the response vector \( Y \) from the observed target values.

2. **Compute Matrices**:
   - Compute \( X^\top X \) and \( X^\top Y \).

3. **Check Invertibility**:
   - Ensure \( X^\top X \) is invertible (or use a pseudo-inverse if not).
   - If \( X^\top X \) is not invertible, it may be due to multicollinearity. Consider removing or combining features, or use regularization methods (like Ridge or Lasso).

4. **Solve for \(\beta\)**:
   \[
   \beta = (X^\top X)^{-1} X^\top Y.
   \]

5. **Use the Model for Prediction**:
   - For a new input \( x_{\text{new}} \), predict:
     \[
     \hat{y}_{\text{new}} = x_{\text{new}}^\top \beta.
     \]


## Example

**Given Data Points**: \((x,y)\) = \((1,1), (2,2), (3,2)\).

**Step-by-step**:

1. Add an intercept term:
   \[
   X = \begin{bmatrix}
   1 & 1 \\
   1 & 2 \\
   1 & 3 \\
   \end{bmatrix}, \quad Y=\begin{bmatrix}1 \\ 2 \\ 2\end{bmatrix}.
   \]

2. Compute:
   \[
   X^\top X = \begin{bmatrix} 3 & 6 \\ 6 &14 \end{bmatrix}, \quad
   X^\top Y = \begin{bmatrix} 5 \\ 12 \end{bmatrix}.
   \]

3. Invert \( X^\top X \):
   \[
   (X^\top X)^{-1} = \begin{bmatrix} 2 & -1 \\ -1 & 0.5 \end{bmatrix}.
   \]

4. Compute \(\beta\):
   \[
   \beta = (X^\top X)^{-1}X^\top Y = \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix}.
   \]

Thus, the fitted line is:
\[
\hat{y} = 0.5 + 0.5x.
\]


## Advantages

- **Closed-Form Solution**: Provides an explicit formula for the optimal parameters, enabling direct interpretation.
- **Efficient for Small Problems**: Works well with relatively small datasets and few features.
- **Foundational Method**: Forms the basis for many advanced regression techniques and regularized models.

## Limitations

- **Assumes Linearity**: The method presupposes a linear relationship between features and output.
- **Sensitive to Outliers**: Squared errors emphasize large errors more heavily, making the model sensitive to outliers.
- **Invertibility Issues**: If \( X^\top X \) is not invertible, the standard formula fails. Issues like multicollinearity require either dropping features, transformations, or using regularized regression variants.

Despite these limitations, least squares regression is a cornerstone technique in data analysis, widely used due to its conceptual simplicity, interpretability, and strong theoretical foundations. It serves as the primary stepping stone to more sophisticated modeling approaches in statistics and machine learning.
