When we have data with noise (potential errors), or multiple different measurement values ($y$) at a given $x$, then we may not want to, or simply cannot fit a function/curve that goes through all points exactly, and rather have to perform [**curve-fitting**](https://en.wikipedia.org/wiki/Curve_fitting) - finding a function that approximates the data in some sense but does not necessarily go through all the points

This is the most typical case for real world data which contains variability and noise, and could additionally give rise to multiple different measurements (i.e. $y$ values) at the same $x$ location.

## How to fit the data exacty

To fit a polynomial that exactly goes through n points we need n unknowns, or free parameters, to choose in the polynomial. 
So we need a polynomial of degree n-1, since such polynomial has n free parameters (all the powers up to n-1, including 0).
