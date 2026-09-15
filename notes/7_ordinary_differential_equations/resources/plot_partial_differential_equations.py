import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

x = np.linspace(0, 1, 500)

# Heat equation: Gaussian-like Fourier-compatible profile using sine modes
def heat_profile(t):
    return (
        np.exp(-np.pi**2*t)*np.sin(np.pi*x)
        + 0.45*np.exp(-9*np.pi**2*t)*np.sin(3*np.pi*x)
        + 0.22*np.exp(-25*np.pi**2*t)*np.sin(5*np.pi*x)
    )

fig, ax = plt.subplots(figsize=(7, 4.3))
for t in [0.0, 0.01, 0.04, 0.12]:
    ax.plot(x, heat_profile(t), label=f"$t={t:g}$")
ax.set_xlabel("$x$")
ax.set_ylabel("$u(x,t)$")
ax.set_title("Heat equation: high-frequency structure decays fastest")
ax.grid(alpha=0.25)
ax.legend()
finish(fig, "pde_heat_diffusion.svg")

# Wave equation: fixed-end modal superposition
def wave_profile(t):
    return (
        np.cos(np.pi*t)*np.sin(np.pi*x)
        + 0.35*np.cos(3*np.pi*t)*np.sin(3*np.pi*x)
    )

fig, ax = plt.subplots(figsize=(7, 4.3))
for t in [0.0, 0.15, 0.30, 0.45]:
    ax.plot(x, wave_profile(t), label=f"$t={t:g}$")
ax.set_xlabel("$x$")
ax.set_ylabel("$u(x,t)$")
ax.set_title("Wave equation: modes oscillate instead of diffusing away")
ax.grid(alpha=0.25)
ax.legend()
finish(fig, "pde_wave_propagation.svg")
