from pathlib import Path
import numpy as np
from svg_plot_utils import line_chart
OUT=Path(__file__).with_name("plots")
x0,y0,x1,y1,xq=1.,2.,4.,5.,2.2
t=(xq-x0)/(x1-x0); yq=(1-t)*y0+t*y1
line_chart(OUT/"linear_interpolation_geometry.svg","Linear interpolation is a weighted average","x","y",
    [{"x":[x0,x1],"y":[y0,y1],"label":"linear interpolant"}],
    [{"x":[x0,x1],"y":[y0,y1],"label":"endpoints"},{"x":[xq],"y":[yq],"label":f"query t={t:.2f}"}])
x=np.linspace(0,np.pi,240)
series=[{"x":x,"y":np.sin(x),"label":"sin(x)"}]
for n,dash in [(4,"8 5"),(8,"10 4 2 4"),(16,"2 4")]:
    nodes=np.linspace(0,np.pi,n+1)
    series.append({"x":x,"y":np.interp(x,nodes,np.sin(nodes)),"label":f"{n} intervals","dash":dash})
line_chart(OUT/"linear_interpolation_refinement.svg","Grid refinement reduces linear interpolation error","x","value",series)
