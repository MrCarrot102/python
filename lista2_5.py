# obliczanie calki oznaczonej 
import scipy 
import math
# obliczamy dla n od 2 do 20 korzystajac
# z rekurencyjnego zwiazku
def I(x):
    if (x == 1):
        return 1
    else:
        return math.e - (x) * I(x-1)
for i in range (2,21):
    print(f'dla {i}, claka = {I(i)}')    