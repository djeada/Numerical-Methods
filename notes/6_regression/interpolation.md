## Interpolation

Interpolation is a method of constructing new data points within the range of a discrete set of known data points. It plays a crucial role in data analysis by helping to predict unknown values for any point within the given range.

Consider two arrays of numbers $X$ and $Y$. The array $X$ contains independent data points and $Y$ includes dependent data points $y_i, i=1,…,m$. The goal is to find a function $\hat{y}(x)$ that passes exactly through the given points. This function is known as the interpolating function or simply the interpolant.

Interpolation makes the following assumptions:

- The given data points are exact, meaning there are no measurement errors.
- The given data points are distinct $x$ locations, i.e., there is a unique mapping from $x$ to $y$.
- The independent variable values are ordered, i.e., $x_0 < x_1 < \ldots < x_N.$

With the interpolant, we can estimate $y$ values at $x$ locations not given in the data. When these $x$ locations are within the range of known data points (i.e., for $x\in[\min\{x_i\},\max\{x_i\}]$), this process is termed interpolation. Conversely, when we seek new $y$ values at $x$ locations outside the data range, this is known as extrapolation.

## Key Concepts

- **Linear Interpolation**: The simplest form of interpolation where a straight line is drawn between two points, and the point of interest is estimated from this line.

- **Polynomial Interpolation**: A method that fits a polynomial of degree $n$ to a set of data points, allowing more complex curves to be fitted to the data.

- **Spline Interpolation**: An interpolation where small polynomials are fit to small sections of the data, making it particularly well-suited for large datasets.

- **Radial Basis Function Interpolation**: A method used when the function is known at a scattered set of points in some high-dimensional space, and one wishes to interpolate this function onto a grid.

## Mathematical Formulation

The specific mathematical formulation of interpolation depends on the method used, but the general aim is to find an interpolating function $f(x)$ that passes through the given data points. For instance, in linear interpolation, the interpolating function is a straight line, while in polynomial interpolation, it's a polynomial of degree $n$.

## Example

Consider a situation where you have the following data about the temperature of a place at different times:

| Time (hours) | Temperature (°C) |
|--------------|------------------|
| 9            | 20               |
| 10           | 22               |
| 11           | 26               |
| 12           | 28               |
| 13           | 30               |
| 14           | 31               |
| 15           | 31               |

Suppose you are interested in estimating the temperature at 10:30 AM, but you don't have that data available. You can estimate the temperature by performing different types of interpolation.

1. **Linear Interpolation**: This method will use the data points at 10 AM (22°C) and 11 AM (26°C) to estimate the temperature at 10:30 AM. The formula for linear interpolation is:
 
$$f(x) = f(a) + ((x - a) / (b - a)) * (f(b) - f(a))$$

Plugging the values in, we get:

$$f(10.5) = 22 + ((10.5 - 10) / (11 - 10)) * (26 - 22) = 24 °C$$

So, according to linear interpolation, the temperature at 10:30 AM would be 24°C.

2. **Spline Interpolation**: This method will consider all the data points and fit a smooth curve to estimate the temperature at 10:30 AM. The curve is designed to minimize the overall curvature of the line, which can provide a more accurate estimate when the underlying data follows a non-linear trend. Performing spline interpolation typically involves complex mathematical computations and is often done using a statistical software or programming language. Let's assume the software returned an estimate of 24.8°C.

Given that the temperature pattern is non-linear (with a peak at noon), the spline interpolation would likely give a more accurate estimate of the temperature at 10:30 AM. This is because it takes into account the overall trend in the data, rather than just the immediate values at 10 AM and 11 AM. Thus, in this case, spline interpolation would be a more appropriate method.

## Advantages

- Interpolation can be a very powerful tool when the data set is large and the underlying function is complex.
- It is straightforward to understand and can be implemented quite easily.

## Limitations

- Interpolation assumes the data is smooth between the known data points, which may not be the case.
- It doesn't perform well with extrapolation, i.e., estimating values outside the known range.
- It is sensitive to the choice of the interpolation method, as different methods can produce different results.
