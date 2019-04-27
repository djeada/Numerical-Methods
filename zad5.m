clear
function m = fit(x,y,n)
  for j = 0:2*n
    xsum(j+1) = sum(x.^j);
  end
  for j = 0:n
    for i = 0:n
      A(j+1,i+1) = xsum(j+i+1);
      b(j+1) = sum (y.*x.^j);
    end
  end
  m = A\b';
  m = fliplr(m');
end
x = [1 2 3 4 5]; 
y = [52 5 -5 -40 10];
m=4;
a = fit(x,y,m);
x2 = 1:0.01:6;
y2 = polyval(a,x2);
plot(x,y,'o',x2,y2)