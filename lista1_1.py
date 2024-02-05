# f(x) = cos x - 3 sin ( tg x - 1 ) 

import numpy as np 
import matplotlib.pyplot as plt 

# definicja funkcji  
def funkcja( x ):
    return np.cos(x) - 3 * np.sin( np.tan(x) - 1 ) 

# zakres 
x = np.linspace ( 0 , 1.5 , 100 ) 
# wartosci y 
y = funkcja ( x ) 

plt.plot ( x , y ) 
plt.axhline ( 0 , color = 'red' , linestyle = '--')
plt.show()

# wartosci odczytane z wykresu 
# funkcja ma 5 miejsc zerowych 