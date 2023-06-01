## Least Squares Regression

Least Squares Regression is a statistical procedure used to find the best fit for a set of data points by minimizing the sum of the squares of the offsets or residuals of points from the plotted curve.

It's used in both simple and multiple linear regression.

## Mathematical Formulation

Given a matrix of features $X$, a vector of target variables $Y$, we're trying to find the coefficient vector $β$ that minimizes the residual sum of squares (RSS), i.e., the squared difference between the observed $Y$ and the predicted $Y$ (denoted $Ŷ$ or $Y_hat$).

In mathematical form, the objective is to minimize:

$$
RSS = \| Y - Xβ \|_{2}^{2}
$$

Using calculus and linear algebra, it can be shown that the $β$ that minimizes the RSS is given by:

$$
β = (X^{T}X)^{-1}X^{T}Y
$$

This formula is known as the **Normal Equation** for least squares regression.

## Derivation

Given the observed data $x_i$ and the corresponding dependent variable $y_i$, we want to estimate $\hat{y}(x_i)$ that accurately represents the data. We assume a model of the form:

$$\hat{y}(x_i) = {\alpha}_1 f_1(x_i) + {\alpha}_2 f_2(x_i) + \cdots + {\alpha}_n f_n(x_i)$$

Here, $f_k(x)$ are a set of functions of the variable $x$ (which could be as simple as $x^k$ or even just $x$, depending on the model), and ${\alpha}_k$ are the coefficients that we need to determine. We can write this set of equations for all observations in matrix form as:

$$\hat{Y} = A{\beta}$$

Where:
- $\hat{Y}$ is the vector of estimated values $\hat{y}(x_i)$,
- ${\beta}$ is the vector of coefficients ${\alpha}_i$, 
- $A$ is the design matrix where each column $i$ is $f_i(x)$ evaluated at each data point.

We want to minimize the total squared error defined as:

$$E = \|{\hat{Y} - Y}\|_{2}^2$$

To find the $\hat{Y}$ that minimizes $E$, we need to find the point where the derivative of $E$ with respect to ${\alpha}_i$ is zero (since at a minimum point, the derivative is zero). 

Taking the derivative and setting it to zero, we find that for the minimum, the residual (the difference between the observed and estimated values) is orthogonal to the estimated values:

$$\hat{Y}^T (Y - \hat{Y}) = 0$$

Expanding $\hat{Y}$ using the equation $\hat{Y} = A{\beta}$ and simplifying gives us:

$$A^T Y - A^T A {\beta} = 0$$

Solving this equation for $\beta$ gives us the least squares regression formula:

$${\beta} = (A^T A)^{-1} A^T Y$$

This is the solution that minimizes the total squared error and gives us the best fit to our data.

## Algorithm Steps

The algorithm for performing a least squares regression is as follows:

1. **Step 1: Data Preparation**: Organize your data into a matrix of features $\mathbf{X}$ and a vector of target variables $\mathbf{Y}$. Each row in the matrix $\mathbf{X}$ corresponds to a single observation, and each column in $\mathbf{X}$ corresponds to a feature. $\mathbf{Y}$ contains the corresponding target values for each observation.

2. **Step 2: Calculate $\mathbf{X}^T \mathbf{X}$ and $\mathbf{X}^T \mathbf{Y}$**: Calculate the product of the transpose of $\mathbf{X}$ with itself, and the product of the transpose of $\mathbf{X}$ with $\mathbf{Y}$.

3. **Step 3: Invert $\mathbf{X}^T \mathbf{X}$**: Invert the matrix $\mathbf{X}^T \mathbf{X}$. This step requires that $\mathbf{X}^T \mathbf{X}$ is invertible (nonsingular). If $\mathbf{X}^T \mathbf{X}$ is not invertible, it means there is multicollinearity in your data, and you may need to remove redundant features or use regularization techniques.

4. **Step 4: Calculate $\boldsymbol{\beta}$**: Calculate $\boldsymbol{\beta}$ by multiplying the inverted $\mathbf{X}^T \mathbf{X}$ with $\mathbf{X}^T \mathbf{Y}$.

5. **Step 5: Use $\boldsymbol{\beta}$ for Predictions**: Once you have $\boldsymbol{\beta}$, you can use it to make predictions for new data. To make a prediction for a new observation, simply multiply the features of the new observation by $\boldsymbol{\beta}$.

## Example

Suppose we have three data points $(1, 1)$, $(2, 2)$, and $(3, 2)$. We wish to fit a linear regression model to this data.

1. First, we arrange our data into $\mathbf{X}$ and $\mathbf{Y}$. In this case, $\mathbf{X}$ is a column vector of the x-coordinates, and $\mathbf{Y}$ is a column vector of the y-coordinates. We add a column of ones to $\mathbf{X}$ to account for the intercept term in $\boldsymbol{\beta}$.

$$\mathbf{X} = \begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix}, \quad \mathbf{Y} = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}$$

2. We calculate $\mathbf{X}^T \mathbf{X}$ and $\mathbf{X}^T \mathbf{Y}$:

$$\mathbf{X}^T \mathbf{X} = \begin{bmatrix} 3 & 6 \\ 6 & 14 \end{bmatrix}, \quad \mathbf{X}^T \mathbf{Y} = \begin{bmatrix} 5 \\ 12 \end{bmatrix}$$

3. We then calculate the inverse of $\mathbf{X}^T \mathbf{X}$:

$$(\mathbf{X}^T \mathbf{X})^{-1} = \begin{bmatrix} 2 & -1 \\ -1 & 0.5 \end{bmatrix}$$

4. We then calculate $\boldsymbol{\beta}$:

$$\boldsymbol{\beta} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{Y} = \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix}$$

So, our linear regression model is $Y = 0.5 + 0.5X$.

## Advantages

- Provides a simple and interpretable mathematical formula for predictions.
- Finds the best fit line that minimizes the sum of the square differences, which is often a reasonable approach.

## Limitations

- It assumes a linear relationship between variables.
- It can be sensitive to outliers.
- While it can handle multiple dependent variables (multiple regression), the interpretation becomes more complex.
