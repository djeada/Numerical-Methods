import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

fig,ax=plt.subplots(figsize=(6,5)); t=np.linspace(0,2*np.pi,300)
for r in [1.2,2.0,2.828,3.5]: ax.plot(r*np.cos(t),r*np.sin(t),alpha=.65)
xx=np.linspace(-1,5,200); ax.plot(xx,4-xx,label='constraint x+y=4')
p=np.array([2.,2.]); ax.scatter(*p,marker='*',s=120,label='constrained minimum')
v=p/np.linalg.norm(p); ax.arrow(*p,.8*v[0],.8*v[1],head_width=.1,length_includes_head=True); ax.text(*(p+1.0*v),'grad f')
ax.set_xlim(-1,5); ax.set_ylim(-1,5); ax.set_aspect('equal'); ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title('Lagrange multiplier tangency'); ax.legend()
finish(fig,'lagrange_tangency.svg')
