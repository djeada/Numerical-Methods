When we have data with noise (potential errors), or multiple different measurement values ($y$) at a given $x$, then we may not want to, or simply cannot fit a function/curve that goes through all points exactly, and rather have to perform [**curve-fitting**](https://en.wikipedia.org/wiki/Curve_fitting) - finding a function that approximates the data in some sense but does not necessarily go through all the points

This is the most typical case for real world data which contains variability and noise, and could additionally give rise to multiple different measurements (i.e. $y$ values) at the same $x$ location.

## How to fit the data exacty

To fit a polynomial that exactly goes through n points we need n unknowns, or free parameters, to choose in the polynomial. 
So we need a polynomial of degree n-1, since such polynomial has n free parameters (all the powers up to n-1, including 0).

## Squared error calculation</span>

Least squares fitting minimises the sum of the squares of the differences between the data provided and the polynomial approximation, i.e. it minimises the expression

$$E = \sum_{i=0}^{N} (P(x_i) - y_i)^2,$$

where $P(x)$ is the polynomial that we are evaulating and $x_i , y_i$ are the data points.


<img src="https://upload.wikimedia.org/wikipedia/commons/b/b0/Linear_least_squares_example2.svg" >

Why is the square distance and not just the distance used?


## Regression Analysis

Regression analysis is a statistical method that is used for predictive analysis. Regression establishes a relationship between a dependent variable (also known as the 'outcome variable', 'target', or 'response') and one or more independent variables (also known as 'predictors', 'covariates', or 'features').

## Key Concepts

- **Linear Regression**: It assumes a linear relationship between the dependent and independent variable(s). The goal is to find the line (or hyperplane in multiple dimensions) that best fits the data.

- **Non-linear Regression**: When the relationship between variables cannot be approximated by a linear model, non-linear regression is used. The data is fitted to a non-linear model.

- **Multiple Regression**: When there are two or more independent variables, the method used is multiple regression.

- **Polynomial Regression**: This is a type of multiple regression where the relationship between the independent and dependent variable is modeled as an nth degree polynomial.

- **Logistic Regression**: It is used when the dependent variable is categorical. It models the probability that the dependent variable equals a certain value.

## Mathematical Formulation

The mathematical representation of a linear regression model is:

`y = β0 + β1*x1 + β2*x2 + ... + βn*xn + ε`

Where:
- `y` is the dependent variable.
- `x1, x2, ..., xn` are the independent variables.
- `β0, β1, ..., βn` are the parameters of the model.
- `ε` is the error term.

## Example

A simple linear regression could be used to predict the price of a house (dependent variable) based on its size in square feet (independent variable).

## Advantages

- Regression analysis is straightforward to understand and explain, making it great for business applications.
- It works on a wide range of data, making it a versatile tool.

## Limitations

- It assumes a linear relationship between the dependent and independent variables. This is not always the case.
- It is sensitive to outliers in the data.
- It requires that the data meet certain assumptions (e.g., homoscedasticity, normality of errors).
