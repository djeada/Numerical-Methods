%przyklad
clear

%liczba próbek
N = 1000;
%szybkosc probkowania
Ts = 0.01;
%przedzial czasu
t = -1:1*Ts:1;
%nasz sygnal u(t)
f1 = 4; 
a1 = 5;
f2 = 3; 
a2 = 8;
f3 = 2; 
a3 = 20;
u = a1*sin(2*pi*f1*t) + a2*sin(2*pi*f2*t) + a3 * sin(2*pi*f3*t);

%wykres sygnalu
figure(1);
plot(t,u);
title('Suma sinusów'); 
xlabel('Czas[s]');
ylabel('Amplituda');

%transformata U(omega)
U = fft(u,N);
U = U(1:N/2);

%przedzial czestotliwosci
f = (0:N/2-1)/(Ts*N);

%wykres transformaty
figure(2);
plot(f,abs(U));
title('Transforamta sumy sinusów'); 
xlabel('Czêstoœæ[Hz]'); 
ylabel('Amplituda');

