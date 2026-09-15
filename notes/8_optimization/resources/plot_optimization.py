import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

# Local/global landscape
x=np.linspace(-4,4,800)
y=0.11*x**4-0.8*x**2+0.35*x+2.1
fig,ax=plt.subplots(figsize=(7,4))
ax.plot(x,y,label="objective")
# sampled extrema-ish markers
for xv,label in [(-2.1,"local minimum"),(1.7,"global minimum"),(0.2,"local maximum")]:
    yv=0.11*xv**4-0.8*xv**2+0.35*xv+2.1
    ax.scatter([xv],[yv],zorder=3)
    ax.annotate(label,(xv,yv),xytext=(8,10),textcoords='offset points')
ax.set_xlabel("x"); ax.set_ylabel("f(x)"); ax.set_title("Local and global structure")
ax.grid(alpha=.25)
finish(fig,"optimization_landscape.svg")

# conditioning and GD paths on quadratics
fig,axes=plt.subplots(1,2,figsize=(8,3.8))
for ax,A,title,alpha in [
    (axes[0],np.diag([2.,1.]),"well conditioned",0.35),
    (axes[1],np.diag([20.,1.]),"poorly conditioned",0.085),
]:
    gx=np.linspace(-3,3,60); gy=np.linspace(-3,3,60)
    X,Y=np.meshgrid(gx,gy); Z=.5*(A[0,0]*X**2+A[1,1]*Y**2)
    ax.contour(X,Y,Z,levels=4)
    p=np.array([2.7,2.4]); pts=[p.copy()]
    for _ in range(22):
        p=p-alpha*(A@p); pts.append(p.copy())
    pts=np.array(pts); ax.plot(pts[:,0],pts[:,1],marker='o',ms=2.4,lw=1)
    ax.scatter([0],[0],marker='*',s=80)
    ax.set_title(title); ax.set_aspect('equal'); ax.set_xlabel('x1'); ax.set_ylabel('x2')
finish(fig,"optimization_conditioning.svg")
