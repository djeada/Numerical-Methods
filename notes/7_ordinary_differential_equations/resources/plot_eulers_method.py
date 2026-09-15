import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

def euler(h, tf=1.0):
    n = int(round(tf / h))
    t = np.linspace(0, tf, n + 1)
    u = np.empty_like(t)
    u[0] = 1.0
    for k in range(n):
        u[k+1] = u[k] + h*u[k]
    return t, u

# Geometry of Euler's method
t = np.linspace(0, 1, 400)
exact = np.exp(t)
te, ue = euler(0.25)

fig, ax = plt.subplots(figsize=(7, 4.3))
ax.plot(t, exact, label="exact $e^t$")
ax.plot(te, ue, "o-", label="Euler, $h=0.25$")
for tn, un in zip(te[:-1], ue[:-1]):
    xx = np.linspace(tn, tn + 0.25, 25)
    ax.plot(xx, un + un*(xx-tn), "--", linewidth=1)
ax.set_xlabel("$t$")
ax.set_ylabel("$u$")
ax.set_title("Euler follows the tangent at the current point")
ax.grid(alpha=0.25)
ax.legend()
finish(fig, "euler_tangent_steps.svg")

# Global error versus step size
hs = 2.0**(-np.arange(2, 10))
errs = []
for h in hs:
    _, u = euler(float(h))
    errs.append(abs(u[-1] - np.e))

fig, ax = plt.subplots(figsize=(6.4, 4.2))
ax.loglog(hs, errs, "o-", label="Euler error at $t=1$")
ref = errs[-1] * (hs / hs[-1])
ax.loglog(hs, ref, "--", label="$O(h)$ reference")
ax.set_xlabel("step size $h$")
ax.set_ylabel("absolute error")
ax.set_title("First-order global convergence")
ax.grid(alpha=0.25, which="both")
ax.legend()
finish(fig, "euler_error_vs_step.svg")
