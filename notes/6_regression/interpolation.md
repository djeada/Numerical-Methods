## Introduction
Interpolation is a method of estimating values between two known values in a sequence or function. It involves constructing new data points within the range of a discrete set of known data points.

We have to arrays of numbers $X$ and $Y$. Array $X$ contains independent data points. Array $Y$ contains dependent data points $y_i,i=1,…,m$.

We want to find a function $\hat{y}(x)$, which gets the exact same value with given points.

In this case the function $f$ is known as the *interpolating function*, or simply the *interpolant*.

Interpolation assumes:

* given data points are *exact* (e.g. no measurement errors) 
* given data points are *distinct* $x$ locations, i.e. there is no ambiguity in a mapping from $x$ to $y$ (which there would be if we had multiple $y$ values for the same $x$). 
* 
$$x_0 < x_1 < \ldots < x_N,$$ 

We can then use this function to find (or estimate) $y$ values at $x$ locations other than those provided by the data. 

When these new $x$ locations are within the range of known data points (i.e. for $x\in[\min\{x_i\},\max\{x_i\}]$) this process is called *interpolation*. 

In the case where we seek new $y$ values at $x$ locations that are outside the data range this is called [*extrapolation*](https://en.wikipedia.org/wiki/Extrapolation) 


## Key Concepts

- **Linear Interpolation**: The simplest form of interpolation where a straight line is drawn between two points, and the point of interest is estimated from this line.

- **Polynomial Interpolation**: Involves fitting a polynomial of degree n to a set of data points. This allows more complex curves to be fitted to the data.

- **Spline Interpolation**: A form of interpolation where small polynomials are fit to small sections of the data, making it particularly well-suited to large datasets.

- **Radial Basis Function Interpolation**: A method used when the function is known at a scattered set of points in some high-dimensional space and one wishes to interpolate this function onto a grid.

## Mathematical Formulation

The mathematical representation of a linear interpolation model is:

$$f(x) = f(a) + ((x - a) / (b - a)) * (f(b) - f(a))$$

Where:

    a and b are the known x-values.
    f(a) and f(b) are the known y-values.
    x is the point of interest.

Example

A simple example of linear interpolation would be estimating the population of a city for the year 2020 if you know the population for 2010 and 2030.
Advantages

    Interpolation can be a very powerful tool when the data set is large and the underlying function is complex.
    It is straightforward to understand and can be implemented quite easily.

Limitations

    Interpolation assumes the data is smooth between the known data points, which may not be the case.
    It doesn't perform well with extrapolation, i.e., estimating values outside the known range.
    It is sensitive to the choice of the interpolation method, as different methods can produce different results.
