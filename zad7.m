n = 30;
tsteps = 2500;
u = zeros(n, tsteps);

L = 1;
T = 1;
D = 2;

dx = L/(n-1);
dt = T/tsteps;

r = D*dt/(dx*dx);

for i = 2:(n-1)
   x = (i-1)*dx;
   u(i, 1) = sin(pi*x);
end
  
for t = 1:tsteps-1
  for i = 2:(n-1)
    u(i, t+1) = r*u(i-1, t)+(1-2*r)*u(i, t) + r*u(i+1, t);
  end
end

mesh(u)

