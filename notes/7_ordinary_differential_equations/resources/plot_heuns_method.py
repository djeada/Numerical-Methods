import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

def euler(h, tf=1.0):
    n = int(round(tf / h))
    u = 1.0
    for _ in range(n):
        u += h*u
    return u

def heun(h, tf=1.0):
    n = int(round(tf / h))
    u = 1.0
    for k in range(n):
        t = k*h
        k1 = u
        pred = u + h*k1
        k2 = pred
        u += h*(k1+k2)/2
    return u

# Predictor-corrector geometry for y'=y
h = 0.6
t0, u0 = 0.0, 1.0
pred = u0 + h*u0
corr = u0 + h*(u0 + pred)/2
tt = np.linspace(0, h, 300)

fig, ax = plt.subplots(figsize=(7, 4.3))
ax.plot(tt, np.exp(tt), label="exact solution")
ax.plot([0, h], [u0, pred], "o--", label="Euler predictor")
ax.plot([0, h], [u0, corr], "o-", label="Heun corrected step")
ax.plot([h, h], [pred, corr], ":", linewidth=1.5)
ax.set_xlabel("$t$")
ax.set_ylabel("$u$")
ax.set_title("Heun averages the starting and predicted ending slopes")
ax.grid(alpha=0.25)
ax.legend()
finish(fig, "heun_predictor_corrector.svg")

# Error comparison
hs = 2.0**(-np.arange(2, 10))
err_e = [abs(euler(float(h)) - np.e) for h in hs]
err_h = [abs(heun(float(h)) - np.e) for h in hs]

fig, ax = plt.subplots(figsize=(6.4, 4.2))
ax.loglog(hs, err_e, "o-", label="Euler")
ax.loglog(hs, err_h, "o-", label="Heun")
ref = err_h[-1] * (hs / hs[-1])**2
ax.loglog(hs, ref, "--", label="$O(h^2)$ reference")
ax.set_xlabel("step size $h$")
ax.set_ylabel("absolute error at $t=1$")
ax.set_title("Heun shows second-order convergence")
ax.grid(alpha=0.25, which="both")
ax.legend()
finish(fig, "heun_error_vs_step.svg")
