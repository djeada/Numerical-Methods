import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

a=np.linspace(0,2.3,500)
phi=(a-1.15)**2+0.15*np.sin(4*a)+1.0
phi0=phi[0]; slope0=-2.3+0.6
c1=.18
arm=phi0+c1*a*slope0
fig,ax=plt.subplots(figsize=(6.5,4)); ax.plot(a,phi,label='phi(alpha)'); ax.plot(a,arm,'--',label='Armijo bound')
mask=phi<=arm
if np.any(mask):
    aa=a[mask]; ax.fill_between(aa,phi[mask],arm[mask],alpha=.18,label='acceptable')
ax.scatter([0],[phi0]); ax.set_xlabel('alpha'); ax.set_ylabel('line-search value'); ax.set_title('Armijo sufficient decrease'); ax.legend(); ax.grid(alpha=.2)
finish(fig,'line_search_armijo.svg')
