clear
A = [9, 8, -2, 2, -2; 7, -3, -2, 7, 2; 2, -2, 2, -7, 6; 4, 8, -3, 3, -1; 2, 2, -1, 1, 4];
[m n]=size(A);
if m~=n 
    disp('Macierz musi byc kwadratowa')
    beep
    break 
end
L=zeros(size(A));
U=zeros(size(A));
U(1,:)=A(1,:);
L(:,1)=A(:,1)/U(1,1);
L(1,1)=1;
for k=2:m
for i=2:m
    for j=i:m
        U(i,j)=A(i,j)-dot(L(i,1:i-1),U(1:i-1,j));
    end
    L(i,k)=(A(i,k)-dot(L(i,1:k-1),U(1:k-1,k)))/U(k,k);
end
end

[L1, U1] = lu (A);

printf("Moje U: \n");
U

printf("Octave U: \n");
U1

printf("Moje L: \n");
L

printf("Octave L: \n");
L1


