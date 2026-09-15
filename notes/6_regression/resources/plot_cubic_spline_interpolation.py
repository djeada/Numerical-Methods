from pathlib import Path
import numpy as np
from svg_plot_utils import line_chart
OUT=Path(__file__).with_name("plots")
def coeff(x,y):
    n=len(x)-1; h=np.diff(x); M=np.zeros(n+1)
    if n>1:
        A=np.zeros((n-1,n-1)); r=np.zeros(n-1)
        for i in range(1,n):
            q=i-1; A[q,q]=2*(h[i-1]+h[i])
            if q>0:A[q,q-1]=h[i-1]
            if q<n-2:A[q,q+1]=h[i]
            r[q]=6*((y[i+1]-y[i])/h[i]-(y[i]-y[i-1])/h[i-1])
        M[1:n]=np.linalg.solve(A,r)
    a=y[:-1]; b=np.diff(y)/h-h*(2*M[:-1]+M[1:])/6; c=M[:-1]/2; d=np.diff(M)/(6*h)
    return a,b,c,d,M
x=np.array([0.,1.,2.2,3.,4.5,5.]); y=np.array([0.,1.2,.4,1.8,1.,1.4]); a,b,c,d,M=coeff(x,y)
q=np.linspace(x[0],x[-1],300); i=np.clip(np.searchsorted(x,q,side="right")-1,0,len(x)-2); dx=q-x[i]
s=a[i]+b[i]*dx+c[i]*dx**2+d[i]*dx**3
line_chart(OUT/"cubic_spline_piecewise_curve.svg","Natural cubic spline through irregular knots","x","S(x)",[{"x":q,"y":s,"label":"natural cubic spline"}],[{"x":x,"y":y,"label":"knots"}])
sp=b[i]+2*c[i]*dx+3*d[i]*dx**2; spp=2*c[i]+6*d[i]*dx
line_chart(OUT/"cubic_spline_derivatives.svg","First and second derivatives stay continuous at knots","x","derivative",
    [{"x":q,"y":sp,"label":"S'(x)"},{"x":q,"y":spp,"label":"S''(x)"}],[{"x":x,"y":M,"label":"M_i = S''(x_i)"}])
