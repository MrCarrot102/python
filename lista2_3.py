# program do obliczania dwoch matematycznie rownowaznych wyrazem 
# sqrt ( x^2 + 1 ) - 1 oraz (x^2)/(sqrt(x^2+1)+1)
# ktore daje wiarygodne wyniki dal x = 2^-n i n od 2 do 24 

# definiowanie rownan 
def rownanie1(x):
    return (x**2+1)**(1/2) - 1 
def rownanie2(x):
    return (x**2)/((x**2+1)**(1/2)+1)

# petla do sprawdzaniaw wynikow 
for i in range ( 2, 35, 2):
    x = 2^(-i)
    print(i, ' ',  rownanie1(x), '\t', rownanie2(x), '\n')
    