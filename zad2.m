clear

function fun = fun1(x)
  fun=3*x.^3-4*x.^2-1;
end

a = 0;
b = 2;
y = a:0.1:b;
w = [];

if fun1(a)*fun1(b) >= 0
  printf("Brak rozwiazania na przedziale\n");
  
else
   while b-a>0.001
      wartosc = (a+b)/2 
      w(end+1) = wartosc;  
     if fun1(wartosc)*fun1(a) > 0
       a=wartosc;
     else
       b=wartosc;
     end
    end   
  printf("wynik to %f ", wartosc);
  plot (y,fun1(y), w, fun1(w), "or")
end

