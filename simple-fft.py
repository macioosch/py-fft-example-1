#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from pylab import *
#from numpy import *
#from scipy import *
import matplotlib.pyplot as plt
import numpy as np

w = 100           # częstotliwość próbkowania [Hz]
T = 1            # rozważany okres [s]

n = T * w        # liczba próbek
t = np.linspace(0, T, n, endpoint=False) # punkty na osi OX [s]

amplituda = 2
czestotliwosc = 10
f = lambda t : amplituda *np.sin( t *2*np.pi *czestotliwosc)    # def. funkcji
signal = f(t)                 # funkcja spróbkowana

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(t, signal, '*')
plt.xlabel("czas [s]")
plt.ylabel("sygnał [j.u.]")

signal1 = np.fft.fft(signal)      
signal1 = abs(signal1)        # moduł 

ax2 = fig.add_subplot(212)
#freqs = np.linspace(0, w, n, endpoint=False)
freqs = np.fft.fftfreq( signal.size, 1/w)
ax2.stem(freqs, signal1, '-*')
plt.xlabel("częstotliwość [Hz]")
plt.ylabel("Intensywność składowej [j.u.]")

plt.show()
