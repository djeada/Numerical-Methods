clear

#the Newton-Raphson Method for finding the roots of 
#an algebraic/transcendental equation.

#define the function, for the given equation
f=@(x) 3*x + sin(x) - e.^x;

#define the frist derivative of your function
df=@(x) 3 - cos(x) - e.^x;


#Change lower limit 'a' and upper limit 'b'
x = 0.05;
x1 = 1000;
w = [];

while (abs(x-x1)>= 0.001)
  x1 = x;
  fx = f(x);
  fx1 = df(x);
  x = x - (fx/fx1);
  w(end+1) = x;  
endwhile

printf("Root found %f \n\n", x)

y = -10:0.1:10;
fun = f(y);
figure;
plot(fun)
grid on
hold on 
plot (w, f(w), "or")
