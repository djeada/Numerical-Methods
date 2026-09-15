from pathlib import Path
import numpy as np
from svg_plot_utils import line_chart
OUT=Path(__file__).with_name("plots")
def lagrange(xn,yn,x):
    p=np.zeros_like(x,dtype=float)
    for j in range(len(xn)):
        L=np.ones_like(x,dtype=float)
        for m in range(len(xn)):
            if m!=j: L*= (x-xn[m])/(xn[j]-xn[m])
        p+=yn[j]*L
    return p
xn=np.array([0.,1.,2.,3.,4.]); yn=np.array([1.,1.8,1.2,2.6,2.])
x=np.linspace(0,4,240); poly=lagrange(xn,yn,x); trend=np.polyval(np.polyfit(xn,yn,1),x)
line_chart(OUT/"interpolation_exact_vs_regression.svg","Interpolation passes through every data point","x","y",
    [{"x":x,"y":poly,"label":"interpolating polynomial"},{"x":x,"y":trend,"label":"least-squares line","dash":"8 5"}],
    [{"x":xn,"y":yn,"label":"data"}])
line_chart(OUT/"interpolation_local_vs_global.svg","Local and global interpolation use the same nodes differently","x","interpolated value",
    [{"x":x,"y":np.interp(x,xn,yn),"label":"piecewise linear"},{"x":x,"y":poly,"label":"global polynomial","dash":"8 5"}],
    [{"x":xn,"y":yn,"label":"nodes"}])
