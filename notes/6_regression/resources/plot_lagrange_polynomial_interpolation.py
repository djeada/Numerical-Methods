from pathlib import Path
import numpy as np
from svg_plot_utils import line_chart
OUT=Path(__file__).with_name("plots")
xn=np.array([-1.,0.,1.,2.]); yn=np.array([1.5,.5,1.,3.]); x=np.linspace(-1.25,2.25,240)
def basis(j):
    L=np.ones_like(x)
    for m in range(len(xn)):
        if m!=j: L*= (x-xn[m])/(xn[j]-xn[m])
    return L
bases=[basis(j) for j in range(len(xn))]
line_chart(OUT/"lagrange_basis_functions.svg","Lagrange basis: one at its node, zero at the others","x","basis value",
    [{"x":x,"y":bases[j],"label":f"L{j}(x)"} for j in range(len(xn))],
    [{"x":xn,"y":np.zeros_like(xn),"label":"node positions"}])
terms=[yn[j]*bases[j] for j in range(len(xn))]
series=[{"x":x,"y":terms[j],"label":f"y{j} L{j}(x)","dash":"5 4"} for j in range(len(xn))]
series.append({"x":x,"y":np.sum(terms,axis=0),"label":"interpolating polynomial"})
line_chart(OUT/"lagrange_weighted_sum.svg","Weighted Lagrange terms add to the interpolant","x","y",series,[{"x":xn,"y":yn,"label":"data"}])
