# eliminacja Gaussa
import numpy as np 
# definiowanie funkcji do eliminacji Gaussa 
def eliminacja_gaussa(A, b):
    # sprawdzanie wymiarów macierzy 
    if A.shape[0] != A.shape[1] or A.shape[0] != b.shape[0]:
        raise ValueError("Niekompatybilne wymiary macierzy!")
    else:
        n=A.shape[0]
        gauss_matrix=np.column_stack((A, b)).astype(float)
        # eliminacja w przod
        for kolumna in range(n):
            for wiersz in range(n):
                if wiersz != kolumna:
                    if gauss_matrix[kolumna, kolumna] != 0:
                        wspolczynnik=gauss_matrix[wiersz, kolumna] / gauss_matrix[kolumna, kolumna]
                        gauss_matrix[wiersz, :] -= wspolczynnik *gauss_matrix[kolumna, :]
        # eliminacja wstecz 
        for kolumna in range(n-2, -1, -1):
            for wiersz in range(n):
                if wiersz != kolumna:
                    if gauss_matrix[kolumna, kolumna] != 0:
                        wspolczynnik=gauss_matrix[wiersz, kolumna] / gauss_matrix[kolumna, kolumna]
                        gauss_matrix[wiersz, :] -= wspolczynnik * gauss_matrix[kolumna, :]
        # normalizacja wierszy ale jest niepotrzebna bo juz jest znormalizowane 
        for wiersz in range(n):
            gauss_matrix[wiersz, :] /= gauss_matrix[wiersz, wiersz]
        
        return gauss_matrix[:, -1]
# macierz z zadania 1 
A1 = np.array([[-1, 1, -4],
               [2, 2, 0],
               [3, 3, 2]])
b1 = np.array([0, 1, 0.5])
x1 = eliminacja_gaussa(A1, b1)
print(f"Rozwiazanie zadania 1 za pomoca eliminacji gaussa:\n {x1}")
# zadanie 2
A2 = np.array([[1, 0, 0],
               [3/2, 1, 0],
               [1/2, 11/13, 1]])
B2 = np.array([[2, -3, -1],
               [0, 13/2, -7/2],
               [0, 0, 32/13]])
b2 = np.array([1, -1, 2])
x3 = eliminacja_gaussa(A2, b2)
x4 = eliminacja_gaussa(B2, b2)
print(f"Zadanie 2:\n {x3}\n {x4}")
# zadanie 3 
A3 = np.array([[0, 0, 2, 1, 2],
               [0, 1, 0, 2, -1],
               [1, 2, 0, -2, 0],
               [0, 0, 0, -1, 1],
               [0, 1, -1, 1, -1]])
b3 = np.array([1, 1, -4, -2, -1])
x3 = eliminacja_gaussa(A3, b3)
print(f'Zadanie 3:\n{x3}')