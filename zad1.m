clear all

%zad 1

for i = 1:5
       wynik = 1/exp(-(15-i)/2)
end

%zad 2

Matrix1=ones(10,20);
Matrix1(6:10,1:20)=3;
Matrix1(4:6,1:20)=25
Matrix1(6:10,12:14)=Matrix1(6:10,12:14).^2;

Matrix1()

[rows,cols]= size(Matrix1);
rows
cols

Matrix1(12,15)=100;

Matrix1()

[rows2,cols2]= size(Matrix1);
rows2
cols2