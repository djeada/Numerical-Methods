%przyklad
clear

%liczba próbek
N = 1000;
%szybkosc probkowania
Ts = 0.01;
%przedzial czasu
t = -1:1*Ts:1;
%nasz sygnal u(t)
sz = 0.5;
u = rectpuls(t,sz);

%wykres sygnalu
figure(1);
plot(t,u);
title('Funkcja Rect'); 
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
title('Transforamta Funkcji Rect'); 
xlabel('Czêstoœæ[Hz]'); 
ylabel('Amplituda');

