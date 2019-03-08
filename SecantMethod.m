clear

#the Secant Method for finding the roots of 
#an algebraic/transcendental equation.

#define the function, for the given equation
f=@(x) 3*x + sin(x) - e.^x;

#Change lower limit 'x2' and upper limit 'x1'
x1 = 10;
x2 = 5;
w = [];

while (abs(x2-x1)>= 0.0001)
  x3 = x2-f(x2)*(x1-x2)/(f(x1)-f(x2));
  x1 = x2;
  x2 = x3;
  w(end+1) = x3;  
endwhile

printf("Root found %f \n\n", x3)

y = -10:0.1:10;
fun = f(y);
figure;
plot(fun)
grid on
hold on 
plot (w, f(w), "or")