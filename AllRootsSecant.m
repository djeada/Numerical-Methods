clear

#Find all roots using the Secant Method

#define the function, for the given equation
function fun = fun1(x)
  fun=3*x + sin(x) - e.^x;
end

#define bisection funcion
function x3 = bisekcja(x1, x2)
while (abs(x2-x1)>= 0.0001)
  x3 = x2-fun1(x2)*(x1-x2)/(fun1(x1)-fun1(x2));
  x1 = x2;
  x2 = x3;
endwhile
endfunction

krok = 1;
a = 0;
b = a + krok;
bmax = 100;
root = [];

while(b < bmax)
 if fun1(a)*fun1(b) < 0  
   root(end+1) = bisekcja(a, b); 
 endif 
   a = b;       
   b = a + krok; 
endwhile

printf("Following roots has been found: \n");

for i = 1:size(root)+1
  printf("%f \n", root(i));
end

