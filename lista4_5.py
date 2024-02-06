# zadanie w ktorym obliczamy c rakity saturn V 
# w locie pionowym tuz przy powierzchni ziemi 
# przyblizajac podanym wzorem
# v =  (u*l* M_0)/(M_0-mt) - gt
# musimy wyznaczyc czas po jakim rakieta osiagnie przedkosc dzwieku

import numpy as np
 
# definiowanie wzoru
def f(u, M, m, t):
    return u*np.log(M/(M-m*t))- 9.81*t
# podane dane 
u = 2510 # m/s 
M = 2.8e6 # kg 
m = 13.3e3 # kg/s
czas = np.arange(0, 100.01, 0.01)
# do przechowywania bliskich danych 
slownik = {}
# szukanie pary predkosci i czasu dla predkosci bliskiej dzwiekowi 
for t in czas:
    v=f(u,M,m,t)
    if round(v)==335:
        slownik[v]=t
# znajdowanie nablizszej wartosci dla predkosci 335 
najblizsza_predkosc = min(slownik.keys(), key=lambda x:abs(x-335))

print(slownik[najblizsza_predkosc])
