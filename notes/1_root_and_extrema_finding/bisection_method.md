# Bisection Method

We may use the bisection method to quickly find an approximation to the root if we know it is somewhere in the interval $[a, b]$.

It moves across the interval using a step $\Delta x$ and smartly adjusts this step with each iteration to come closer to the root value.



## Algorithm

- We start with inital $a$ and $b$ for which $f(a)f(b) < 0$

- We calculate the midpoint between $a$ and $b$: $c = \frac{a+b}{2}$


  - If $f(a)f(c) < 0$, then we replace the old value of $b$ with $c$.

  - else we replace the old value of $a$ with $c$.


- We repeat all the steps $n$ times, wehre $n$ is a number provided to the user.
