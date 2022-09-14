## The calssical definition

The classical definition of the derivative of a function $f(x)$ at a point $x_0$:

 $$f'(x_0)=\lim_{h\rightarrow 0} \frac{f(x_0+h)-f(x_0)}{h}. $$

Where $h$ is an infinitesimally small increment to the $x$ coordinate.

## Finite differences 

Finite differences are numerical methods for calculating the derivatives.

Weighted sums of function evaluations at a number of locations can be used to obtain approximations to a function's derivatives.

### Forward difference

This method is called "forward difference method", beacuse it uses values of $x$ greater than $x_0$ ( $h>0$ ).

$$ f'(x_0)\approx \frac{f(x_0+h)-f(x_0)}{h}, \quad h>0. $$

The limit $h$ from the classical definition has been replaced by $h$  which is extremely small but still finite.

### Backward difference

Analogous to the forward difference:

$$ f'(x_0)\approx \frac{f(x_0) - f(x_0 - h)}{h}, \quad h>0. $$

## Taylor expansion

Taylor series expansion about the point $x_0$:

$$ f(x_0+h) = f(x_0) + hf'(x_0) + \frac{h^2}{2!}f''(x_0) + \frac{h^3}{3!}f'''(x_0) + \ldots $$

Let's try to move $f'(x_0)$ on the left side of the equation:

$$ -hf'(x_0) + f(x_0+h) = f(x_0) + \frac{h^2}{2!}f''(x_0) + \frac{h^3}{3!}f'''(x_0) + \ldots $$

$$ -hf'(x_0) = -f(x_0+h) + f(x_0) +O(h^2)$$

$$ hf'(x_0)=f(x_0+h)-f(x_0) +O(h^2) $$
  
 $$ f'(x_0)=\frac{f(x_0+h)-f(x_0)}{h}+O(h) $$

## Central difference

Let's use our taylor expansion knowledge to get a better approximation of the derivatives:

$$ f(x_0+ h) = f(x_0)+h f'(x_0)+\frac{h^2}{2}f''(x_0) + \mathcal{O}(h^3) $$

$$ f(x_0- h) = f(x_0)- h f'(x_0)+\frac{(-h)^2}{2}f''(x_0) + \mathcal{O}((-h)^3) $$

Now let's make use of one small tirck $(-h)^2=h^2$ and see what happens:

$$ f(x_0+h) = f(x_0)+hf'(x_0)+\frac{h^2}{2}f''(x_0) + \mathcal{O}(h^3) $$

$$ f(x_0-h) = f(x_0)-hf'(x_0)+\frac{h^2}{2}f''(x_0) + \mathcal{O}(h^3) $$

We subtract the second equation from the first:

$$ f(x_0+h)-f(x_0-h)=2hf'(x_0) + \mathcal{O}(h^3)$$

Let' rearrange for $f'(x_0)$:

$$ f'(x_0)=\frac{f(x_0+h)-f(x_0-h)}{2h} + O(h^2)$$
