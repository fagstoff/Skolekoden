''' Dette er et forslag til løsning på punkt 6 i dette undervisningsopplegget:
https://github.com/fagstoff/Skolekoden/blob/master/Undervisningsopplegg/Nullpunkt_halveringsmetoden/Nullpunkt_halveringsmetoden.md
Copyright (C) 2020 BITJUNGLE Rune Mathisen
Koden er lisensiert under en GPLv3-lisens 
Se http://www.gnu.org/licenses/gpl-3.0.html 
'''

def f(x, k):
    '''Funksjonen som er gitt i oppgava.'''
    return k*x**3 + (3/4)*k*x**2 + k*x + 1

a = -5 # startpunkt på venstre side av nullpunktet
b = 5  # startpunkt på høyre side av nullpunktet
TOL = 1E-9 # toleranse: hvor nærme svaret skal vi komme før vi er fornøyde?

while abs(a - b) > TOL: # så lenge avstanden mellom a og b stor
    k = (a + b)/2       # velg x midt mellom a og b
    print('Nå er k=', k)
    if f(-1.5, a)*f(-1.5, k) > 0:   # hvis produktet er større enn null
        a = k             # sett a til n-verdien
    else:               # ellers
        b = k             # sett b til n-verdien
                        # gjenta 

print("Løsningen er k=", k)
