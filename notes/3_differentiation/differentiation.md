## The calssical definition

The classical definition of the derivative of a function $f(x)$ at a point $x_0$:

 $$f'(x_0)=\lim_{h\rightarrow 0} \frac{f(x_0+h)-f(x_0)}{h}. $$

Where $h$ is an infinitesimally small increment to the $x$ coordinate.

## Finite differences 

Finite differences are numerical methods for calculating the derivatives.

Weighted sums of function evaluations at a number of locations can be used to obtain approximations to a function's derivatives.

### Forward difference

$$ f'(x_0)\approx \frac{f(x_0+\Delta x)-f(x_0)}{\Delta x},\;\;\;\; \Delta x>0. $$

The limit $h$ from the classical definition has been replaced by $\Delta x$  which is extremely small but still finite.

$$\frac{df}{dx} = \lim_{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}$$

Backward difference:
$$\frac{df}{dx} = \lim_{h \rightarrow 0} \frac{f(x)-f(x-h)}{h}$$

Taylor expansion of f(x+h) about x

$$f(x+h) = f(x) + (x+h-x)f'(x) + \frac{1}{2}(x+h-x)^2f''(x) + ...$$
$$f(x+h) = f(x) + hf'(x) + \frac{1}{2}h^2f''(x) + ...$$

$$f'(x) = [\frac{f(x+h)-f(x)}{h}] + \frac{h}{2}f''(x)$$

what is the ideal h?
small, but can't be 0

-rounding error is bad if h is too small


## Central difference

$$\frac{df}{dx} = \lim_{h \rightarrow 0} \frac{f(x+h/2)-f(x-h/2)}{h}$$
