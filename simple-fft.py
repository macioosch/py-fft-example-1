#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pylab import *
from numpy import *
from scipy import *

w = 100           # częstotliwość próbkowania [Hz]
T = 1            # rozważany okres [s]

n = T * w        # liczba próbek
t = linspace(0, T, n, endpoint=False) # punkty na osi OX [s]

amplituda = 2
czestotliwosc = 50
f = lambda t : amplituda *sin( t *2*pi *czestotliwosc)    # def. funkcji
signal = f(t)                 # funkcja spróbkowana

subplot(211)
plot(t, signal, '*')
xlabel("czas [s]")
ylabel("sygnał [j.u.]")

signal1 = fft(signal)      
signal1 = abs(signal1) /( amplituda *T*w/2)        # moduł 

subplot(212)
freqs = linspace(0, w, n, endpoint=False)
stem(freqs, signal1, '-*')
xlabel("częstotliwość [Hz]")
ylabel("Intensywność składowej [j.u.]")

show()
