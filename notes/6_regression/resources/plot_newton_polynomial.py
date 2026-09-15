from pathlib import Path
import numpy as np
from svg_plot_utils import line_chart
OUT=Path(__file__).with_name("plots")
xn=np.array([0.,1.,2.,3.]); yn=np.array([1.,2.,.5,3.])
def dd(x,y):
    c=np.array(y,float).copy()
    for j in range(1,len(c)): c[j:]=(c[j:]-c[j-1:-1])/(x[j:]-x[:-j])
    return c
def ev(xn,c,x):
    p=np.full_like(x,c[-1],dtype=float)
    for k in range(len(c)-2,-1,-1): p=c[k]+(x-xn[k])*p
    return p
c=dd(xn,yn); x=np.linspace(-.2,3.2,240)
series=[]
for k in range(1,len(xn)+1): series.append({"x":x,"y":ev(xn[:k],c[:k],x),"label":f"first {k} node(s)"})
line_chart(OUT/"newton_incremental_construction.svg","Newton interpolation can be extended one node at a time","x","y",series,[{"x":xn,"y":yn,"label":"data"}])
prod=np.ones_like(x); running=np.full_like(x,c[0]); series=[{"x":x,"y":running.copy(),"label":"P0"}]
for k in range(1,len(c)):
    prod*=x-xn[k-1]; running=running+c[k]*prod
    series.append({"x":x,"y":running.copy(),"label":f"P{k}"})
line_chart(OUT/"newton_partial_sums.svg","Each Newton correction preserves earlier nodes","x","partial interpolant",series,[{"x":xn,"y":yn,"label":"nodes"}])
