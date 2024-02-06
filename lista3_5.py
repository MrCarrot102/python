# obliczanie normy i wskaznika dla macierzy hilberta 5, 10, 20 
import numpy as np 
from scipy.linalg import toeplitz, norm
# wymiary 
n = [5, 10, 20]
for i in n:
    # tworzenie macierzy toeplitza o rozmiarze n x n 
    c = np.arange(i, 0, -1) # kolumna dla macierzy 
    r = np.ones(i) # pierwszy wiersz 
    T = toeplitz(c, r)
    # obliczanie normly macierzy 
    matrix_norm = norm(T)
    # obliczanie wskaznika uwarunkowania 
    cond_number = np.linalg.cond(T)
    # wyswitlanie wynikow 
    print(f"n = {i}")
    print(f"Norma: {matrix_norm}")
    print(f"Wskaznik uwarunkowania: {cond_number}")
    print()