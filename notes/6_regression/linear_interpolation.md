## Linear Interpolation

Linear interpolation is a simple yet effective technique used in curve fitting to approximate a value between two known data points. This method is based on the assumption that the function between the two points is linear, making it a quick and easy method of approximation.

### Key Concepts

- Linear interpolation is based on the assumption that the function is linear between two points.
- This method is both simple and quick, although its accuracy may be compromised for complex functions or larger intervals.

### Mathematical Formulation

Given two data points $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$, the linear interpolation of a value $y$ at a point $x$ can be estimated using the following formula:

$$
y = y_i + \frac{(y_{i+1} - y_i) (x - x_i)}{x_{i+1} - x_i}
$$

### Derivation
 
![Derivation Illustration](https://user-images.githubusercontent.com/37275728/188960726-ac99ac89-f1b8-4b82-9761-5093cb91d4db.png)

We can derive the formula for linear interpolation as follows:

1. Calculate the slope ($\alpha$) of the line between the two points: 

$$
\alpha = \frac{y_{i+1} - y_i}{x_{i+1} - x_i}
$$

2. Multiply the slope by the difference between the desired x value and the first x value to get $h$:

$$
h = \alpha \cdot (x - x_i)
$$

3. Add $h$ to the initial y value to get the interpolated y value:

$$
y = y_i + h
$$

This can be written as:

$$
y = y_i + (x - x_i) \cdot \frac{y_{i+1} - y_i}{x_{i+1} - x_i}
$$

This equation is the formula for linear interpolation.

### Algorithm Steps

Implementing linear interpolation involves the following steps:

1. Identify the two points $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$ between which you want to interpolate.
2. Apply the linear interpolation formula to estimate the value of the function at the desired point $x$.

### Example

Suppose we have the points A(-2, 0) and B (2, 2). Let's try to estimate the value of the function at $x=1$.

![Example Illustration](https://user-images.githubusercontent.com/37275728/188960814-569c5a91-82b4-415c-9840-f5ebd4cc421d.png)

1. Identify the points between which we want to interpolate, in this case $(-2, 0)$ and $(2, 2)$.
2. Apply the linear interpolation formula:

$$
\hat{y}(x) = y_i + \frac{(y_{i+1} - y_{i})(x - x_{i})}{(x_{i+1} - x_{i})} = 0 + \frac{(2 - 0)(1 - (-2))}{(2 - (-2))} = 1.5
$$

### Advantages

- The method is straightforward and quick to apply.
- It's practical when the data is nearly linear or when a quick approximation is required.

### Limitations

- The accuracy of the method diminishes as the function becomes more non-linear.
- It does not take into account any known derivatives at the data points,
