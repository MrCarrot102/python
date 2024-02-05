# obliczanie ukladu rownan dla Ax=b
# dla dwoch macierzy 
import numpy as np 
from scipy import linalg 
# definiowanie macierzy 
A = np.array([[0, 0, 2, 1, 2],
              [0, 1, 0, 2, -1],
              [1, 2, 0, -2, 0],
              [0, 0, 0, -1, 1],
              [0, 1, -1, 1, -1]])
# macierz b
b = np.array([1, 1, -4, -2, -1])
# definiowanie rozwiazania 
x = linalg.solve(A, b)
# pokazywanie rozwiazania 
print(f'Rozwiazanie Ax=b: {x}')