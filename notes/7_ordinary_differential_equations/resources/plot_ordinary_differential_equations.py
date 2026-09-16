import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

# Logistic phase-line / trajectories
r, K = 1.2, 1.0
t = np.linspace(0, 6, 500)

def logistic(t, y0):
    return K / (1 + ((K-y0)/y0)*np.exp(-r*t))

fig, ax = plt.subplots(figsize=(7, 4.3))
for y0 in [0.08, 0.25, 0.6, 1.4]:
    ax.plot(t, logistic(t, y0), label=f"$y_0={y0}$")
ax.axhline(K, linestyle="--", linewidth=1.2, label="stable equilibrium $K$")
ax.set_xlabel("$t$")
ax.set_ylabel("$y(t)$")
ax.set_title("Autonomous ODE trajectories approach a stable equilibrium")
ax.grid(alpha=0.25)
ax.legend(ncol=2)
finish(fig, "ode_phase_line.svg")

# Method accuracy on y'=y over [0,2]
def solve(method, h, tf=2.0):
    n = int(round(tf/h))
    t = np.linspace(0, tf, n+1)
    u = np.empty(n+1)
    u[0] = 1.0
    for k in range(n):
        if method == "Euler":
            u[k+1] = u[k] + h*u[k]
        elif method == "Heun":
            pred = u[k] + h*u[k]
            u[k+1] = u[k] + 0.5*h*(u[k]+pred)
        else:
            y = u[k]
            k1 = y
            k2 = y + 0.5*h*k1
            k3 = y + 0.5*h*k2
            k4 = y + h*k3
            u[k+1] = y + h*(k1+2*k2+2*k3+k4)/6
    return t, u

fig, ax = plt.subplots(figsize=(7, 4.3))
tt = np.linspace(0, 2, 400)
ax.plot(tt, np.exp(tt), linewidth=2, label="exact")
for method in ["Euler", "Heun", "RK4"]:
    ts, us = solve(method, 0.4)
    ax.plot(ts, us, "o-", label=method)
ax.set_xlabel("$t$")
ax.set_ylabel("$u$")
ax.set_title("Different time-stepping orders at the same step size")
ax.grid(alpha=0.25)
ax.legend()
finish(fig, "ode_method_accuracy.svg")
