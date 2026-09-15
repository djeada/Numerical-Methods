import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

rng=np.random.default_rng(4)
def f(P):
    x=P[:,0]; y=P[:,1]; return (x-1.1)**2+1.5*(y+0.7)**2+.25*np.sin(4*x)*np.sin(3*y)
lo=np.array([-3.,-3.]); hi=np.array([3.,3.]); P=rng.uniform(lo,hi,size=(60,2))
snaps={0:P.copy()}
for gen in range(35):
    fit=f(P); new=np.empty_like(P)
    for i in range(len(P)):
        a,b=rng.choice(len(P),2,replace=False); new[i]=P[a if fit[a]<fit[b] else b]
    for i in range(0,len(P)-1,2):
        if rng.random()<.75:
            a=rng.uniform(0,1,2); p,q=new[i].copy(),new[i+1].copy(); new[i]=a*p+(1-a)*q; new[i+1]=(1-a)*p+a*q
    mask=rng.random(P.shape)<.12; new+=mask*rng.normal(0,.3,P.shape); P=np.clip(new,lo,hi)
    if gen+1 in [8,34]: snaps[gen+1]=P.copy()
fig,axes=plt.subplots(1,3,figsize=(9,3.4));
xx=np.linspace(-3,3,80); yy=np.linspace(-3,3,80); X,Y=np.meshgrid(xx,yy); Z=(X-1.1)**2+1.5*(Y+.7)**2+.25*np.sin(4*X)*np.sin(3*Y)
for ax,(gen,Q) in zip(axes,sorted(snaps.items())):
    ax.scatter(Q[:,0],Q[:,1],s=10); ax.scatter([1.1],[-.7],marker='*',s=55);  ax.set_title(f'generation {gen}'); ax.set_xlim(-3,3); ax.set_ylim(-3,3); ax.set_aspect('equal')
finish(fig,'genetic_algorithm_population.svg')
