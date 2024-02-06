# obliczanie pierwiastka 5 stopnia z dowolnej liczy dodatniej 
# metoda Newtona 

# definiowanie funkcji 
def pierwiastek_piaty(x, epsilon=1e-6, max_iter=1000):
    przyblizenie=x/2.0
    for _ in range(max_iter):
        # metoda Newtona
        nowe_przyblizenie=(4*przyblizenie+x/przyblizenie**4)/5
        # sprawdzanie wyniku przyblizenia 
        if abs(nowe_przyblizenie - przyblizenie)<epsilon:
            # wystarczajaco blisko, wtedy zwracamy wynik
            return round(nowe_przyblizenie, 4)
        # aktualne przyblizenie 
        przyblizenie = nowe_przyblizenie
    
# pokazanie dzialania programu 
x = 5 
print(f"pierwiastek piatego stopnia z liczy {x} to {pierwiastek_piaty(x)}")