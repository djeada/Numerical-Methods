import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

x = np.linspace(0, 1, 400)
exact = 2*np.exp(x) - x - 1
y0 = np.ones_like(x)
y1 = 1 + x + 0.5*x**2
y2 = 1 + x + x**2 + x**3/6
y3 = 1 + x + x**2 + x**3/3 + x**4/24

fig, ax = plt.subplots(figsize=(7, 4.3))
ax.plot(x, exact, linewidth=2, label="exact")
for i, y in enumerate([y0, y1, y2, y3]):
    ax.plot(x, y, label=f"$y_{i}$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y(x)$")
ax.set_title("Successive Picard iterates approach the exact solution")
ax.grid(alpha=0.25)
ax.legend()
finish(fig, "picard_iterates.svg")

# Numerically generate more Picard iterates via cumulative trapezoid
x = np.linspace(0, 1, 1201)
dx = x[1]-x[0]
y = np.ones_like(x)
errors = []
for n in range(8):
    errors.append(np.max(np.abs(y - (2*np.exp(x)-x-1))))
    integrand = x + y
    integ = np.zeros_like(x)
    integ[1:] = np.cumsum(0.5*(integrand[:-1]+integrand[1:])*dx)
    y = 1 + integ

fig, ax = plt.subplots(figsize=(6.4, 4.2))
ax.semilogy(range(len(errors)), errors, "o-")
ax.set_xlabel("Picard iteration")
ax.set_ylabel("maximum error on $[0,1]$")
ax.set_title("Picard iteration converges rapidly on this short interval")
ax.grid(alpha=0.25, which="both")
finish(fig, "picard_convergence.svg")
