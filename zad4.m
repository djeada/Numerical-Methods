clear

A = [6 5 -5; 2 6 -2; 2 5 -1]; 


x0 = rand(3, 1);
x0 = x0/norm(x0);

x = [];
y = [];


for i = 1:100
    x(end+1) = i;  
    y(end+1) = norm(x0);  

    x0 = x0/norm(x0);

    x0 = A*x0;
end

scatter (x, y)


%norma wektora to warotsc wlasna
printf("wynik to %f \n", norm(x0));

x0/norm(x0)

printf("\n wektor wlasny znaleziony funkcja eig() : \n ");
[v l] = eig(A);
v(:,1)
diag(l)(1)


