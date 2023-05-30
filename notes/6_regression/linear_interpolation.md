## Linear Interpolation

Linear interpolation is achieved by connecting two data points with a straight line.

For $x_i < x < x_{i+1}$:

$$\hat{y}(x) = y_i + \frac{(y_{i+1} - y_{i})(x - x_{i})}{(x_{i+1} - x_{i})}.$$


### Derivation
 
![Screenshot from 2022-09-07 21-23-10](https://user-images.githubusercontent.com/37275728/188960726-ac99ac89-f1b8-4b82-9761-5093cb91d4db.png)


$$\alpha = \frac{y_2 - y_1}{x_2 - x_1}$$

$$h = \alpha \cdot (x - x_1)$$

$$y = y_1 + h$$

$$y = y_1 + (x - x_1) \cdot \frac{y_2 - y_1}{x_2 - x_1}$$

### Example

We are given two points A(-2, 0) and B (2, 2).


![Screenshot from 2022-09-07 21-23-32](https://user-images.githubusercontent.com/37275728/188960814-569c5a91-82b4-415c-9840-f5ebd4cc421d.png)

Let's try to evaluate the value of the function at $x=1$

$$\hat{y}(x) = y_i + \frac{(y_{i+1} - y_{i})(x - x_{i})}{(x_{i+1} - x_{i})} = 0 + \frac{(2 - 0)(1 - (-2))}{(2 - (-2))} = 1.5$$


## Linear Interpolation

Linear interpolation is a method of curve fitting used to find the value between two known data points. 

## Key Concepts

- The method assumes the function is linear between two points.
- It's simple, quick, but not highly accurate for complex functions or large intervals.

## Mathematical Formulation

If we have two data points (x_0, y_0) and (x_1, y_1), the linear interpolation of a value y at point x can be obtained by:

$$y = y_0 + ((y_1 - y_0) / (x_1 - x_0)) * (x - x_0)$$

## Algorithm Steps

1. Identify the two points (x_0, y_0) and (x_1, y_1) between which you want to interpolate.
2. Apply the linear interpolation formula to estimate the function's value at the required point.

## Example

Suppose we have points (1, 2) and (3, 6). If we want to find the value of the function at x = 2:

1. Identify the points between which we interpolate, here (1, 2) and (3, 6).
2. Apply the linear interpolation formula, `y = 2 + ((6 - 2) / (3 - 1)) * (2 - 1) = 4`.

## Advantages

- The method is simple and quick to use.
- It's useful when the data is nearly linear or when we need a quick approximation.

## Limitations

- The accuracy of the method decreases as the function becomes more non-linear.
- It doesn't account for any known derivatives at the data points.
