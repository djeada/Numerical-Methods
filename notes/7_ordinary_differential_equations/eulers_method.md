Let's start with the Taylor series:

$$ u(t+\Delta t)=u(t)+\Delta t u'(t) + O(\Delta t^2) $$

We may alternatively rewrite the above equation as follows:

$$ u(t+\Delta t)=u(t)+ \Delta t f(u(t),t)+ O(\Delta t^2).$$

Which is roughly equivalent to:

$$ u(t+\Delta t)=u(t)+ \Delta t f(u(t),t)$$

## Example

$$ u'(t)=u(t),$$

$$ u(0)=1$$

$$u(0.1)=?$$

Let's choose the step value: $\Delta t = 0.05$

We start at $t=0$:

$$  u(0.05) \approx u(0)+0.05u'(0) $$

$$  u(0.05) \approx1+0.05u(0) $$

$$  u(0.05) \approx1+0.05 \cdot 1 $$

$$  u(0.05) \approx 1.05 $$

Now that we know $u(0.05)$, we can calculate the second step:

$$  u(0.1) \approx u(0.05)+0.05u'(0.05) $$

$$  u(0.1) \approx1.05+0.05u(0.05) $$

$$  u(0.1) \approx1.05+0.05 \cdot 1.05 $$

$$  u(0.1) \approx 1.1025 $$
