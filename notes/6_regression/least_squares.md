## Linear Regression

Linear regression is a statistical method that models the relationship between a dependent variable (denoted as $y$) and one or more independent variables (denoted as $X$). 

Assuming the relationship between $X$ and $Y$ is linear, we aim to find an estimator $\hat{y}(x)$ that accurately represents the given data.

## Mathematical Formulation

In simple linear regression, we assume a relationship between the dependent variable $y$ and the independent variable $x$ that takes the form $y = mx + b$, where $m$ is the slope of the line and $b$ is the y-intercept.

The slope $m$ and y-intercept $b$ are determined by minimizing the sum of the squares of the vertical deviations from each data point to the line. Mathematically, this is expressed as follows:

- Slope ($m$): $m = \frac{N \Sigma xy - \Sigma x \Sigma y}{N \Sigma x^2 - (\Sigma x)^2}$

- Intercept ($b$): $b = \frac{\Sigma y - m \Sigma x}{N}$

Here, 
- $N$ is the number of observations.
- $\Sigma xy$ is the sum of the product of $x$ and $y$ observations.
- $\Sigma x$ and $\Sigma y$ are the sums of $x$ and $y$ observations respectively.
- $\Sigma x^2$ is the sum of the squares of $x$ observations.

These formulas directly follow from the least squares criterion and the normal equation.

In multiple linear regression, the mathematical formulation is generalized to more than one predictor. In this case, the predictors and the output are represented as vectors, and the relationship between them is expressed in matrix form:

$Y = AX + \epsilon$

Here, 
- $Y$ is the vector of outputs.
- $A$ is a matrix where each row represents an observation and each column represents a different feature or predictor. 
- $X$ is a vector of parameters or coefficients. 
- $\epsilon$ is a vector of errors or residuals.

The least squares estimate of $X$ is given by:

$X = (A^T A)^{-1} A^T Y$

## Assumptions

The following assumptions are often made in linear regression:

- There exists a linear relationship between the dependent and independent variables.
- There is little or no multicollinearity between the independent variables.
- There is little or no autocorrelation in the data.
- The variance of the residuals, or homoscedasticity, is constant.

## Derivation

Estimation $\hat{y}(x_i)$ for each point $x_i$:

$$\hat{y}(x_1) = {\alpha}_1 f_1(x_1) + {\alpha}_2 f_2(x_1) + \cdots + {\alpha}_n f_n(x_1),$$
$$\hat{y}(x_2) = {\alpha}_1 f_1(x_2) + {\alpha}_2 f_2(x_2) + \cdots + {\alpha}_n f_n(x_2),$$
\begin{center}$ \cdots $ \end{center}
$$\hat{y}(x_m) = {\alpha}_1 f_1(x_m) + {\alpha}_2 f_2(x_m) + \cdots + {\alpha}_n f_n(x_m)$$

We can write this system of equations in terms of column vectors $\hat{Y}$ and $\beta$:\\

$\hat{Y}_i = \hat{y}(x_i)$\\
$\beta_i = {\alpha}_i$\\

and $m x n$ matrix $A$ such that it's i-th column equals $F_i(x)$.\\

The system of equations becomes then: $\hat{Y} = A{\beta}$\\

The total squared error is given by E:

$$E = \|{\hat{Y} - Y}\|_{2}^2$$

$\hat{Y}$, that is closest to $Y$ is the one that can point perpendicularly to $Y$ .

$${\text{dot}}(\hat{Y}, Y - \hat{Y}) = 0$$

$$\hat{Y}^T (Y - \hat{Y}) = 0$$

$$(A{\beta})^T(Y - A{\beta}) = 0$$

$${\beta}^T A^T Y - {\beta}^T A^T A {\beta} = {\beta}^T(A^T Y - A^T A {\beta}) = 0$$

$$A^T Y - A^T A {\beta} = 0$$\\

We arrive at the least squares regression formula:

$${\beta} = (A^T A)^{-1} A^T Y$$

## Algorithm Steps

1. **Collect and prepare the data:** Make sure the data is in the correct format. You will need two arrays of numbers: an independent variable `x` and a dependent variable `y`. Each pair `(x_i, y_i)` represents one data point.

2. **Compute the sums:** Calculate the sums of `x`, `y`, `x*y`, and `x^2`. You will need these sums to compute the parameters of the regression line.

3. **Calculate the parameters:** Use the following formulas to calculate the slope `m` and intercept `b` of the line:

    - Slope (`m`): `(N * Σxy - Σx * Σy) / (N * Σx^2 - (Σx)^2)`
    - Intercept (`b`): `(Σy - m * Σx) / N`

4. **Compute the residuals:** For each data point `(x_i, y_i)`, compute the residual `e_i = y_i - (m * x_i + b)`. This residual represents the difference between the observed and predicted `y` value for each `x`.

5. **Check the quality of the fit:** Calculate the total squared error `E = Σ(e_i)^2`. This quantity measures the overall difference between the data and the regression line. A smaller total squared error indicates a better fit.

## Example

Suppose we have a set of points {(1,1), (2,2), (3,2)}. We can use the least squares method to find the best fitting line for these points.

1. **Prepare the data:** In this case, the independent variable `x` is {1, 2, 3} and the dependent variable `y` is {1, 2, 2}.

2. **Compute the sums:** We have `Σx = 6`, `Σy = 5`, `Σxy = 9`, `Σx^2 = 14`.

3. **Calculate the parameters:** Using the formulas, we get `m = (3 * 9 - 6 * 5) / (3 * 14 - 6^2) = 0.5` and `b = (5 - 0.5 * 6) / 3 = 0.5`.

4. **Compute the residuals:** For each data point, we have `e_1 = 1 - (0.5 * 1 + 0.5) = 0`, `e_2 = 2 - (0.5 * 2 + 0.5) = 0.5`, `e_3 = 2 - (0.5 * 3 + 0.5) = -0.5`.

5. **Check the quality of the fit:** The total squared error is `E = 0^2 + 0.5^2 + (-0.5)^2 = 0.5`. So, the line `y = 0.5x + 0.5` is the best fitting line according to the least squares method for this data set.

## Advantages

- Provides a simple and interpretable mathematical formula for predictions.
- Finds the best fit line that minimizes the sum of the square differences, which is often a reasonable approach.

## Limitations

- Assumes a linear relationship between variables.
- Can be sensitive to outliers.
- Can only handle a single dependent variable.
