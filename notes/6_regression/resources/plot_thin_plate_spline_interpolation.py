from pathlib import Path
import numpy as np
from svg_plot_utils import heatmap, wireframe
OUT=Path(__file__).with_name("plots")
p=np.array([[-1.,-1.],[-.8,.4],[-.2,1.],[.4,.8],[1.,.2],[.7,-.8],[0.,-.5],[-.3,.2],[.5,.1],[1.,1.],[-1.,1.],[.2,-1.]])
v=np.sin(1.7*p[:,0])+.7*np.cos(1.4*p[:,1])
def phi(r):
    r=np.asarray(r,float); out=np.zeros_like(r); m=r>0; out[m]=r[m]**2*np.log(r[m]); return out
n=len(p); K=phi(np.linalg.norm(p[:,None,:]-p[None,:,:],axis=2)); P=np.c_[np.ones(n),p]
sol=np.linalg.solve(np.block([[K,P],[P.T,np.zeros((3,3))]]),np.r_[v,np.zeros(3)]); w=sol[:n]; a=sol[n:]
g=np.linspace(-1.15,1.15,18); X,Y=np.meshgrid(g,g); q=np.c_[X.ravel(),Y.ravel()]
Z=(phi(np.linalg.norm(q[:,None,:]-p[None,:,:],axis=2))@w+a[0]+a[1]*q[:,0]+a[2]*q[:,1]).reshape(X.shape)
pts=np.c_[p,v]
wireframe(OUT/"thin_plate_spline_surface.svg","Thin-plate spline bends a smooth surface through scattered data",X,Y,Z,pts)
heatmap(OUT/"thin_plate_spline_contours.svg","Thin-plate spline interpolation over scattered sites",X,Y,Z,p)
