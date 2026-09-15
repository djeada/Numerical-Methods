import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

x=np.linspace(-2.3,2.3,400)
f=.18*x**4+.25*x**3+1.1*x**2-.7*x+1
x0=1.35
g=.72*x0**3+.75*x0**2+2.2*x0-.7
h=2.16*x0**2+1.5*x0+2.2
f0=.18*x0**4+.25*x0**3+1.1*x0**2-.7*x0+1
newton=f0+g*(x-x0)+.5*h*(x-x0)**2
hq=.65*h
quasi=f0+g*(x-x0)+.5*hq*(x-x0)**2
fig,ax=plt.subplots(figsize=(7,4)); ax.plot(x,f,label='objective'); ax.plot(x,newton,'--',label='Newton quadratic model'); ax.plot(x,quasi,':',label='quasi-Newton model')
ax.scatter([x0],[f0]); ax.set_ylim(0,8); ax.set_xlabel('x'); ax.set_ylabel('value'); ax.set_title('Exact versus approximate curvature'); ax.legend(); ax.grid(alpha=.2)
finish(fig,'newton_quasi_newton.svg')
