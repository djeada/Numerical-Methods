from pathlib import Path
import numpy as np
from svg_plot_utils import line_chart
OUT=Path(__file__).with_name("plots")
rng=np.random.default_rng(7); x=np.linspace(0,6,14); y=1.2+.8*x+rng.normal(0,.55,x.size)
X=np.c_[np.ones_like(x),x]; beta,*_=np.linalg.lstsq(X,y,rcond=None); fit=X@beta
line_chart(OUT/"least_squares_residuals.svg","Least squares minimizes total squared residual","x","y",
    [{"x":x,"y":fit,"label":"least-squares line"}],[{"x":x,"y":y,"label":"observations"}])
b0=np.linspace(beta[0]-1.6,beta[0]+1.6,140)
series=[]
for slope in np.linspace(beta[1]-.45,beta[1]+.45,4):
    rss=np.array([np.sum((y-(a+slope*x))**2) for a in b0])
    series.append({"x":b0,"y":rss,"label":f"beta1={slope:.2f}"})
line_chart(OUT/"least_squares_objective_contours.svg","Slices through the convex least-squares objective","intercept beta0","RSS",series)
