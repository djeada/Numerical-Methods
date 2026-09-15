import numpy as np
import matplotlib.pyplot as plt
from plot_style import finish

def f(x): return 10+x*x-10*np.cos(2*np.pi*x)
rng=np.random.default_rng(7); x=3.7; fx=f(x); T=8.; alpha=.992; sigma=.55
vals=[]; temps=[]; uphill=[]
for k in range(650):
    y=np.clip(x+sigma*rng.standard_normal(),-5.12,5.12); fy=f(y); d=fy-fx; accepted=d<=0 or rng.random()<np.exp(-d/max(T,1e-300))
    if accepted:
        if d>0: uphill.append(k)
        x,fx=y,fy
    vals.append(fx); temps.append(T); T*=alpha
fig,ax=plt.subplots(figsize=(7,4)); ax.plot(vals,label='current objective'); ax.plot(np.minimum.accumulate(vals),label='best so far')
for k in uphill[:25]: ax.axvline(k,alpha=.08)
ax2=ax.twinx(); ax2.plot(temps,linestyle=':',alpha=.7,label='temperature'); ax.set_xlabel('iteration'); ax.set_ylabel('objective'); ax2.set_ylabel('temperature'); ax.set_title('Simulated annealing trace'); ax.legend(loc='upper left'); ax2.legend(loc='upper right')
finish(fig,'simulated_annealing_trace.svg')
