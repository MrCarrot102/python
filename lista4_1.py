from scipy import optimize  
# znajdywanie pierwiastkow funkcji 
# definiowanie danej funkcji 
# korzystanie z metody riddera 
def funkcja(x):
    return 2*x**4+24*x**3+61*x**2-16*x+1
# generowanie zakresu x do -10 do 1 
x = [x*0.001 for x in range(-10000, 1001)]
# metoda riddera 
# uzywanie zbioru aby pierwiastki sie nie powtarzaly 
roots = set()

for n in x:
    try:
        # szukanie pierwiastka
        root = optimize.ridder(funkcja, n, n+0.01)
        # dodawanie pierwiastka i zaokraglanie go do 11 miejsc po przecinku 
        roots.add(round(root, 11))
    except:
        pass
    
roots = list(roots)
print(roots)

