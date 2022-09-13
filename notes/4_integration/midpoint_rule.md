## Midpoint Rule

The region between the integral boundaries is divided into $n$ subintervals. 
At the midpoint of each subinterval, we evaluate the function $f(x)$. 
So, if our subinterval is defined by $x_{i}$ and $x_{i+1}$, our rectangle will have the following coordinates:

$A = (x_{i}, f(\frac{x_{i} + x_{i+1}}{2}))$

$B = (x_{i+1}, f(\frac{x_{i} + x_{i+1}}{2}))$

$C = (x_{i+1}, 0)$

$D = (x_{i}, 0)$

The areas of each of those rectangles are then calculated, and the integral approximation is just the sum of all those areas.

$$I = \sum_{i=0}^{n-1} f(\frac{x_{i} + x_{i+1}}{2}) h$$

![Screenshot from 2022-09-13 23-18-11](https://user-images.githubusercontent.com/37275728/190011101-dcc77f54-d47d-4f62-b699-9d1eec9ef109.png)
