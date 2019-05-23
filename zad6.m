clear all;
function f = F_xy(y, x)
  f = y - x*x;
end

function k = k1(y, x, step)
  k = (y + step*F_xy(y,x)) - (x + step)*(x + step);
end

function k = k2(y, x, h)
  k = (y + 1/2*h*F_xy(y,x)) - (x + 1/2*h)*(x + 1/2*h);
end

function k = k3(y, x, step)
  k = (y + 1/2*step*k2(y,x,step)) - (x + 1/2*step)*(x + 1/2*step);
end

function k = k4(y, x, step)
  k = (y + step*k3(y,x,step)) - (x + step)*(x + step);
end

function y = Kutty2(step)
  j = 1;
  y(j) = 1;
  for i = 0:step:3
    y(j+1) = y(j) + 1/2*(F_xy(y(j), i) + k1(y(j), i, step))*step;
    j +=1;
  end
end

function y = Kutty4(step)
  j = 1;
  y(j) = 1;
  for i = 0:step:3
    y(j+1) = y(j) + 1/6*(F_xy(y(j), i) + 2*k2(y(j), i, step)+ 2*k3(y(j), i, step) + k4(y(j), i, step))*step;
    j +=1;
  end
end

function y = Euler(step)
  j = 1;
  y(j) = 1;
  for i = 0:step:3
    y(j+1) = y(j) + step * (y(j)-i*i);
    j +=1;
  end
end

step = 1;
x = 0:step:3+step;

hold on;
%Euler method
y1 = Euler(step);
scatter(x,y1, "r")

%Second order Kutty
y2 = Kutty2(step);
scatter(x,y2, "g")

%Forth order Kutty
y3 = Kutty4(step);
scatter(x,y3, "b")

%analytical solution
sol =@(x) 2 + 2*x + x.^2 - exp(x);
plot(x,sol(x))

legend("Euler", "RK II", "RK IV", "Analityczna")