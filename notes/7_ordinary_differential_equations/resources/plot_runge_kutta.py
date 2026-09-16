import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

# RK4 stage geometry on y'=y
h = 0.8
u0 = 1.0
k1 = u0
k2 = u0 + 0.5*h*k1
k3 = u0 + 0.5*h*k2
k4 = u0 + h*k3
stages_t = [0, h/2, h/2, h]
stages_u = [u0, k2, k3, k4]

tt = np.linspace(0, h, 300)
fig, ax = plt.subplots(figsize=(7, 4.3))
ax.plot(tt, np.exp(tt), linewidth=2, label="exact solution")
ax.scatter(stages_t, stages_u, s=55, zorder=3, label="RK4 stage states")
for i, (ts, us) in enumerate(zip(stages_t, stages_u), start=1):
    ax.annotate(f"$k_{i}$", (ts, us), xytext=(6, 7), textcoords="offset points")
ax.set_xlabel("$t$")
ax.set_ylabel("$u$")
ax.set_title("RK4 samples the vector field four times within a step")
ax.grid(alpha=0.25)
ax.legend()
finish(fig, "rk4_stages.svg")

def rk4(h, tf=1.0):
    n = int(round(tf/h))
    u = 1.0
    for _ in range(n):
        k1 = u
        k2 = u + 0.5*h*k1
        k3 = u + 0.5*h*k2
        k4 = u + h*k3
        u += h*(k1+2*k2+2*k3+k4)/6
    return u

hs = 2.0**(-np.arange(1, 8))
errs = [abs(rk4(float(h))-np.e) for h in hs]
fig, ax = plt.subplots(figsize=(6.4, 4.2))
ax.loglog(hs, errs, "o-", label="RK4 error")
ref = errs[-1]*(hs/hs[-1])**4
ax.loglog(hs, ref, "--", label="$O(h^4)$ reference")
ax.set_xlabel("step size $h$")
ax.set_ylabel("absolute error at $t=1$")
ax.set_title("Classical RK4 has fourth-order global accuracy")
ax.grid(alpha=0.25, which="both")
ax.legend()
finish(fig, "rk4_error_vs_step.svg")
