clear

f=@(x) 3*x.^3-4*x.^2-1;

a = 0;
b = 2;
y = a:0.1:b;
w = [];

if f(a)*f(b) >= 0
  printf("Brak rozwiazania na przedziale\n");
  
else
   while b-a>0.001
      wartosc = (a+b)/2 
      w(end+1) = wartosc;  
     if f(a)*f(a) > 0
       a=wartosc;
     else
       b=wartosc;
     end
    end   
  printf("wynik to %f ", wartosc);
  plot (y,f(y), w, f(w), "or")
end

