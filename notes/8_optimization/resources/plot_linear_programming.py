import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

fig,ax=plt.subplots(figsize=(6,5))
poly=np.array([[0,0],[4,0],[3,2],[0,3.5]])
ax.fill(poly[:,0],poly[:,1],alpha=.22,label='feasible polytope'); ax.plot([0,4,3,0,0],[0,0,2,3.5,0])
xx=np.linspace(0,4.5,100)
for val in [8,15,23]:
    yy=(val-5*xx)/4
    ax.plot(xx,yy,'--',alpha=.7)
    ax.text(.15,(val-.75)/4,f'5x1+4x2={val}',fontsize=8)
ax.scatter([3],[2],marker='*',s=120,label='optimal vertex (3,2)')
ax.set_xlim(-.2,4.5); ax.set_ylim(-.2,4); ax.set_aspect('equal'); ax.set_xlabel('x1'); ax.set_ylabel('x2'); ax.set_title('Linear programming geometry'); ax.legend()
finish(fig,'linear_programming_geometry.svg')
