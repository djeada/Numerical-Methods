import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

def ras(x): return 10+x*x-10*np.cos(2*np.pi*x)
x=np.linspace(-5.12,5.12,1200); y=ras(x)
fig,ax=plt.subplots(figsize=(7,4)); ax.plot(x,y); ax.scatter([0],[0],marker='*',s=100,label='global minimum')
for xv in [-3,-2,-1,1,2,3]: ax.scatter([xv],[ras(xv)],s=18)
ax.set_xlabel('x'); ax.set_ylabel('f(x)'); ax.set_title('Rastrigin: many local minima'); ax.legend(); ax.grid(alpha=.2)
finish(fig,'global_rastrigin.svg')

fig,ax=plt.subplots(figsize=(7,4)); ax.plot(x,y,alpha=.65)
local=np.array([3.6,3.25,3.08,3.01,2.99]); anneal=np.array([3.6,2.8,3.1,1.9,2.4,1.15,.8,.15,.02])
ax.plot(local,ras(local),marker='o',label='local refinement')
ax.plot(anneal,ras(anneal),marker='s',label='global/stochastic exploration')
ax.set_xlim(-.5,4); ax.set_xlabel('x'); ax.set_ylabel('f(x)'); ax.set_title('Local exploitation versus broader exploration'); ax.legend()
finish(fig,'global_search_comparison.svg')
