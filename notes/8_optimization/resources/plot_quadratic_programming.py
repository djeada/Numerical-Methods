import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

fig,ax=plt.subplots(figsize=(6,5))
x=np.linspace(-.5,4.5,220); y=np.linspace(-.5,4.5,220); X,Y=np.meshgrid(x,y); Z=(X-3.5)**2+1.6*(Y-2.6)**2
ax.contour(X,Y,Z,levels=10)
poly=np.array([[0,0],[3,0],[2.4,1.6],[0,3]])
ax.fill(poly[:,0],poly[:,1],alpha=.18,label='feasible set'); ax.plot([0,3,2.4,0,0],[0,0,1.6,3,0])
start=np.array([1.2,1.0]); grad=np.array([2*(start[0]-3.5),3.2*(start[1]-2.6)]); trial=start-.55*grad
proj=np.array([2.9,1.1])
ax.scatter(*start,label='current'); ax.scatter(*trial,label='unconstrained trial'); ax.scatter(*proj,marker='*',s=90,label='projected point')
ax.arrow(start[0],start[1],*(trial-start),head_width=.08,length_includes_head=True,alpha=.8); ax.arrow(trial[0],trial[1],*(proj-trial),head_width=.08,length_includes_head=True,alpha=.8)
ax.set_xlim(-.4,4.5); ax.set_ylim(-.4,4.5); ax.set_aspect('equal'); ax.set_xlabel('x1'); ax.set_ylabel('x2'); ax.set_title('Projected-gradient idea for a convex QP'); ax.legend(fontsize=8)
finish(fig,'quadratic_programming_projection.svg')
