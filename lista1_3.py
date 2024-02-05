# robienie dzialan na macierzach i wektorze 
import numpy as np 
import scipy as sci 
# macierz A 
A = np.array([[4, -2 , 1],
            [-2, 4, -2],
            [1, -2, 4]])
# macierz B 
B = np.array([[4, 2, 0],
             [2, 5, 2],
             [1, -2, 4]])
# wektor w 
w = np.array([[1],
              [-2],
              [4]])
# obliczanie AB 
AB = np.matmul(A, B)
# obliczanie Aw 
Aw = np.matmul(A, w)
# obliczanie B(Aw)
C = np.matmul(B, Aw) 
# obliczanie wyznacznikow i macierzy odwrotnych 
Adet = np.linalg.det(A)
Bdet = np.linalg.det(B)
# odwrotne
Ainv = np.linalg.inv(A)
Binv = np.linalg.inv(B)

# wyswietlanie wynikow pierwsze  
print(AB, '\n')
print(Aw, '\n')
print(C, '\n')
# wyswietlanie wynikow drugie 
print(Adet, '\n')
print(Bdet, '\n')
print(Ainv, '\n')
print(Binv, '\n')
