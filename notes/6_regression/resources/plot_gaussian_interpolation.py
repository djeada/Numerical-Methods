from pathlib import Path
import numpy as np
from svg_plot_utils import line_chart
OUT=Path(__file__).with_name("plots")
xn=np.array([0.,1.,2.,3.]); yn=np.array([0.,1.,.2,1.2]); x=np.linspace(-.5,3.5,260)
def A(e): return np.exp(-(e*(xn[:,None]-xn[None,:]))**2)
def interp(e):
    w=np.linalg.solve(A(e),yn); return np.exp(-(e*(x[:,None]-xn[None,:]))**2)@w
e=1.2
line_chart(OUT/"gaussian_rbf_basis_functions.svg","Gaussian RBFs centered at the data sites","x","basis value",
    [{"x":x,"y":np.exp(-(e*(x-c))**2),"label":f"center {c:g}"} for c in xn])
series=[]
for e in [.5,1.,2.]:
    series.append({"x":x,"y":interp(e),"label":f"epsilon={e:g}, cond={np.linalg.cond(A(e)):.1e}"})
line_chart(OUT/"gaussian_rbf_shape_parameter.svg","Shape parameter changes curve and conditioning","x","s(x)",series,[{"x":xn,"y":yn,"label":"data"}])
