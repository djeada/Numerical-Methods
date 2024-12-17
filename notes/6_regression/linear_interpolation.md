## Introduction

Linear interpolation is one of the most basic and commonly used interpolation methods. The idea is to approximate the value of a function between two known data points by assuming that the function behaves linearly (like a straight line) between these points. Although this assumption may be simplistic, it often provides a reasonable approximation, especially when the data points are close together or the underlying function is relatively smooth.

**Conceptual Illustration (Not Removing the Plot)**:

Imagine you have two points on a graph:

![Example Illustration](https://user-images.githubusercontent.com/37275728/188960814-569c5a91-82b4-415c-9840-f5ebd4cc421d.png)

Linear interpolation draws a straight line between the two known data points $(x_i,y_i)$ and $(x_{i+1},y_{i+1})$, and then estimates the value at $x$ by following this line.

## Mathematical Formulation

Given two known data points $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$, and a target $x$-value with $x_i \leq x \leq x_{i+1}$, the line connecting these points has a slope $\alpha$ given by:

$$\alpha = \frac{y_{i+1} - y_i}{x_{i+1} - x_i}.$$

To find the interpolated value $y$ at $x$, start from $y_i$ and move along the line for the interval $(x - x_i)$:

$$y = y_i + \alpha (x - x_i).$$

Substituting $\alpha$:

$$y = y_i + (x - x_i) \frac{y_{i+1} - y_i}{x_{i+1} - x_i}.$$

This formula provides the interpolated $y$-value directly.

## Derivation

![Derivation Illustration](https://user-images.githubusercontent.com/37275728/188960726-ac99ac89-f1b8-4b82-9761-5093cb91d4db.png)

I. **Slope Calculation:**

The slope $\alpha$ of the line passing through $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$ is:

$$\alpha = \frac{y_{i+1} - y_i}{x_{i+1}-x_i}.$$

II. **Linear Equation:**

A line passing through $(x_i, y_i)$ with slope $\alpha$ is:

$$y - y_i = \alpha (x - x_i).$$

III. **Substitution:**

Replace $\alpha$ with its expression:

$$y - y_i = \frac{y_{i+1} - y_i}{x_{i+1}-x_i} (x - x_i).$$

IV. **Final Formula:**

Simplifying:

$$y = y_i + \frac{(y_{i+1} - y_i)}{x_{i+1}-x_i} (x - x_i).$$

## Algorithm Steps

I. Identify the interval $[x_i, x_{i+1}]$ that contains the target $x$.

II. Compute the slope:

$$\frac{y_{i+1} - y_i}{x_{i+1}-x_i}.$$

III. Substitute into the linear interpolation formula:

$$y = y_i + \frac{(y_{i+1} - y_i)}{x_{i+1}-x_i} (x - x_i).$$

The result is the interpolated value $y$ at the desired $x$.

## Example

**Given Points**: $A(-2,0)$ and $B(2,2)$. Suppose we want to find $y$ at $x=1$.

I. Compute the slope:

$$\alpha = \frac{2 - 0}{2 - (-2)} = \frac{2}{4} = 0.5.$$

II. Substitute $x=1$:

$$y = 0 + 0.5 (1 - (-2)) = 0.5 \times 3 = 1.5.$$

So, the line passing through $(-2,0)$ and $(2,2)$ gives $y=1.5$ when $x=1$.

## Advantages

- **Simplicity**: The calculation is straightforward and quick.
- **Minimal Data Requirements**: Only two data points are needed.
- **Local Approximation**: Good approximation if the function is nearly linear in the interval.

## Limitations

- **Linear Assumption**: If the true relationship is not nearly linear, the approximation can be poor.
- **No Derivative Information**: The method does not use any information about the slope or curvature of the underlying function.
- **Accuracy**: The accuracy diminishes as the interval $(x_{i+1}-x_i)$ grows large or the function becomes more non-linear.
