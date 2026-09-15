import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

x=np.linspace(0,5,250); y=np.linspace(0,5,250); X,Y=np.meshgrid(x,y); Z=(X-4.0)**2+(Y-3.2)**2
fig,ax=plt.subplots(figsize=(6,5)); ax.contour(X,Y,Z,levels=12)
poly=np.array([[0,0],[4,0],[3,2],[0,3.5]])
ax.fill(poly[:,0],poly[:,1],alpha=.2,label='feasible region'); ax.plot(*poly.T); ax.plot([poly[-1,0],poly[0,0]],[poly[-1,1],poly[0,1]])
pts=[]
for xv in np.linspace(0,4,400):
    ymax=min(8-2*xv,(7-xv)/2)
    if ymax>=0: pts.append((xv,ymax))
pts=np.array(pts); vals=(pts[:,0]-4)**2+(pts[:,1]-3.2)**2; p=pts[np.argmin(vals)]
ax.scatter([p[0]],[p[1]],marker='*',s=100,label='constrained optimum'); ax.set_xlabel('x1'); ax.set_ylabel('x2'); ax.set_title('Objective contours and feasibility'); ax.legend(); ax.set_aspect('equal')
finish(fig,'constrained_feasible_region.svg')

fig,ax=plt.subplots(figsize=(6,5)); t=np.linspace(0,2*np.pi,300)
center=np.array([0.6,0.7])
for rr in [.55,1.0,1.45,1.9]: ax.plot(center[0]+rr*np.cos(t),center[1]+rr*np.sin(t),alpha=.7)
xx=np.linspace(-.3,3.3,100); ax.plot(xx,3-xx,label='active constraint')
p=np.array([1.45,1.55]); ax.scatter(*p,marker='*',s=100)
obj_grad=2*(p-center); con_grad=np.array([1.,1.])
for vec,label in [(obj_grad/np.linalg.norm(obj_grad),'grad f'),(-con_grad/np.linalg.norm(con_grad),'constraint force')]:
    ax.arrow(p[0],p[1],.65*vec[0],.65*vec[1],head_width=.07,length_includes_head=True); ax.text(p[0]+.72*vec[0],p[1]+.72*vec[1],label)
ax.set_xlim(-.4,3.4); ax.set_ylim(-.4,3.4); ax.set_aspect('equal'); ax.set_title('KKT balance at an active boundary'); ax.legend()
finish(fig,'constrained_kkt_geometry.svg')
