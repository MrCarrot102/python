# macierz Hilberta n x n 
# rownanie opisujace h_ik = ( 1 ) / ( i + k + 1 ) , i,k = 0,1...,n-1
# wypisywanie elementow dla n = 4 i 8 
# oraz sprawdzanie jak sie zmienia dla n od 5 do 20 
import scipy.linalg as sp 
import numpy as np
# petla do tworzenia macierzy 
for i in range (4, 9, 4):
    hilbert = sp.hilbert(i)
    h = np.linalg.inv(hilbert)
    print('\n\n\n', hilbert, '\n\n\n', h)
# sprawdzanie jak sie zmienia det od 5 do 20 
for i in range (5,21):
    hilbert = sp.hilbert(i)
    h = np.linalg.det(hilbert)
    print('dla n = ', i, ' det = ', h)
    