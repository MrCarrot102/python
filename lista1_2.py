# obliczanie kolejnych 100 elementow ciagu x_n+1 = 3.5 * x_n ( 1 - x_n ) 
# n to liczby calkowite > 0 
import matplotlib.pyplot as plt 
import numpy as np 
# pierwszy wyraz ciagu 
xn = 0.1 
# tablica elementow ciagu 
ciag = [] 
# obliczanie 100 elementow ciagu i dodawanie ich do talbicy 
for i in range ( 0 , 100 ):
    xn = 3.5 * xn * ( 1 - xn ) 
    ciag.append(xn) 
# wektor x 
x = np.linspace ( 0 , 99 , 100 ) 
# przedstawianie wyniku na wykresie 
plt.scatter( x , ciag )
plt.show()