
$$ Linear Regression
We have to arrays of numbers $X$ and $Y$. Array $X$ contains independent data points. Array $Y$ contains dependent data points $y_i,i=1,…,m$.

We want to find $\hat{y}(x)$, that accurately represents given data.\\

$$ Assumptions

* Linear relationship
* Little or no multi-collinearity
* Little or no auto-correlation
* Homoscedasticity

## Least Squares Regression

Total squared error is defined as: 
$$E = \sum_{i=1}^m (\hat{y} - y_i)^2$$. 

The individual errors or residuals are defined as: 
$$e_i = (\hat{y} - y_i)$$.

We try to minimize total squared error and $E = \|{e}\|_{2}^{2}$.

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

## Least Squares Method

The least squares method is a statistical procedure to find the best fit for a set of data points by minimizing the sum of the squares of the offsets or residuals of points from the plotted curve.

## Key Concepts

- Used in regression analysis to approximate the solution of overdetermined systems.
- The method minimizes the sum of the square differences between the observed and predicted values.

## Mathematical Formulation

For a simple linear regression model `y = mx + b`, the least squares estimates of the parameters `m` and `b` are given by:

$$
m = (NΣxy - ΣxΣy) / (NΣx^2 - (Σx)^2)$$

$$b = (Σy - mΣx) / N$$

Where,
N is the number of observations.
Σxy is the sum of the product of x and y observations.
Σx and Σy are the sums of x and y observations respectively.
Σx^2 is the sum of the squares of x observations.
Algorithm Steps

    Establish the linear regression equation y = mx + b.
    Substitute the observed values into the equation and calculate the estimated values.
    Compute the residuals between the observed and estimated values.
    Minimize the sum of the square residuals using calculus to find the least squares estimates of m and b.

Example

Suppose we have a set of points {(1,1), (2,2), (3,2)}. We can use the least squares method to find the best fitting line for these points.
Advantages

    Provides a simple and interpretable mathematical formula for predictions.
    Finds the best fit line that minimizes the sum of the square differences, which is often a reasonable approach.

Limitations

    It assumes a linear relationship between variables.
    It can be sensitive to outliers.
    It can only handle a single dependent variable.
