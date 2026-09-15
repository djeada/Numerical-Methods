import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

x=np.linspace(-2.5,2.5,400); f=x*x+0.25*x
x1,x2=-1.8,1.7; y1=x1*x1+.25*x1; y2=x2*x2+.25*x2
fig,ax=plt.subplots(figsize=(6.5,4)); ax.plot(x,f,label='convex f')
ax.plot([x1,x2],[y1,y2],'--',label='chord')
mid=.35*x1+.65*x2; fm=mid*mid+.25*mid; chord=.35*y1+.65*y2
ax.scatter([mid,mid],[fm,chord]); ax.vlines(mid,fm,chord,linestyle=':'); ax.annotate('f(weighted point)',(mid,fm),xytext=(10,-20),textcoords='offset points'); ax.annotate('weighted chord value',(mid,chord),xytext=(10,10),textcoords='offset points')
ax.set_xlabel('x'); ax.set_ylabel('value'); ax.set_title('Jensen inequality'); ax.legend(); ax.grid(alpha=.2)
finish(fig,'convex_jensen.svg')

u=np.linspace(-1,5,260); v=np.linspace(-1,5,260); X,Y=np.meshgrid(u,v); Z=(X-1.2)**2+1.7*(Y-1.4)**2
fig,ax=plt.subplots(figsize=(6,5)); ax.contour(X,Y,Z,levels=12)
poly=np.array([[0,0],[4,0],[0,4]])
ax.fill(poly[:,0],poly[:,1],alpha=.18,label='convex feasible set')
ax.plot([0,4,0,0],[0,0,4,0]); ax.scatter([1.2],[1.4],marker='*',s=100,label='unconstrained minimum')
ax.set_xlim(-.5,4.6); ax.set_ylim(-.5,4.6); ax.set_aspect('equal'); ax.set_xlabel('x1'); ax.set_ylabel('x2'); ax.set_title('Convex levels over a convex set'); ax.legend()
finish(fig,'convex_feasible_levels.svg')
