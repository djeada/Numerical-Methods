from pathlib import Path
import numpy as np
from svg_plot_utils import line_chart
OUT=Path(__file__).with_name("plots")
rng=np.random.default_rng(3); x=np.linspace(-2.5,2.5,26); truth=1+.5*x-.65*x**2+.18*x**3
y=truth+rng.normal(0,.8,x.size); q=np.linspace(-2.7,2.7,260)
series=[]
for d in [1,3,10]: series.append({"x":q,"y":np.polyval(np.polyfit(x,y,d),q),"label":f"degree {d}"})
line_chart(OUT/"regression_model_complexity.svg","Regression balances flexibility against noise","x","predicted response",series,[{"x":x,"y":y,"label":"observations"}])
p=rng.permutation(len(x)); tr=p[:18]; te=p[18:]; deg=np.arange(1,13); a=[]; b=[]
for d in deg:
    c=np.polyfit(x[tr],y[tr],d)
    a.append(np.sqrt(np.mean((y[tr]-np.polyval(c,x[tr]))**2)))
    b.append(np.sqrt(np.mean((y[te]-np.polyval(c,x[te]))**2)))
line_chart(OUT/"regression_train_validation_error.svg","Training error can fall while held-out error rises","polynomial degree","RMSE",
    [{"x":deg,"y":a,"label":"training RMSE"},{"x":deg,"y":b,"label":"held-out RMSE"}])
