import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

def f(p):
    x,y=p; return (1-x)**2+100*(y-x*x)**2

def g(p):
    x,y=p; return np.array([-2*(1-x)-400*x*(y-x*x),200*(y-x*x)])

def H(p):
    x,y=p; return np.array([[2-400*y+1200*x*x,-400*x],[-400*x,200.]])

# paths
xx=np.linspace(-1.6,1.4,80); yy=np.linspace(-.4,2.0,80)
X,Y=np.meshgrid(xx,yy); Z=(1-X)**2+100*(Y-X**2)**2
fig,ax=plt.subplots(figsize=(7,4.6)); ax.contour(X,Y,np.log10(Z+1),levels=7)
# gd
p=np.array([-1.2,1.0]); gd=[p.copy()]
for _ in range(900):
    p=p-0.001*g(p)
    if _%45==0: gd.append(p.copy())
gd.append(p.copy()); gd=np.array(gd); ax.plot(gd[:,0],gd[:,1],label='gradient descent',marker='o',ms=2)
# damped newton
p=np.array([-1.2,1.0]); nt=[p.copy()]
for _ in range(12):
    grad=g(p)
    try: d=np.linalg.solve(H(p),-grad)
    except np.linalg.LinAlgError: break
    a=1.0; fp=f(p)
    while f(p+a*d)>fp+1e-4*a*grad@d and a>1e-5: a*=.5
    p=p+a*d; nt.append(p.copy())
nt=np.array(nt); ax.plot(nt[:,0],nt[:,1],label='damped Newton',marker='s',ms=3)
ax.scatter([1],[1],marker='*',s=100,label='minimum'); ax.legend(); ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title('Rosenbrock optimization paths')
finish(fig,'local_rosenbrock_paths.svg')

# idealized rates
k=np.arange(0,9)
linear=.6**k
superlinear=np.array([1,.55,.24,.075,.014,.0015,8e-5,2e-6,2e-8])
quadratic=np.array([1,.45,.18,.032,.001,1e-6,1e-12,1e-16,1e-16])
fig,ax=plt.subplots(figsize=(6.5,4)); ax.semilogy(k,linear,marker='o',label='linear'); ax.semilogy(k,superlinear,marker='s',label='superlinear'); ax.semilogy(k,quadratic,marker='^',label='quadratic')
ax.set_xlabel('iteration'); ax.set_ylabel('idealized error'); ax.set_title('Convergence-rate comparison'); ax.grid(alpha=.25); ax.legend()
finish(fig,'local_convergence_rates.svg')
