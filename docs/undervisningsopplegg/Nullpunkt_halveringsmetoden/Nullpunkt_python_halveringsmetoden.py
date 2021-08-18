''' Dette er to forslag til løsning på punkt 6 i dette undervisningsopplegget:
https://github.com/fagstoff/Skolekoden/blob/master/Undervisningsopplegg/Nullpunkt_halveringsmetoden/Nullpunkt_halveringsmetoden.md
Copyright (C) 2020 BITJUNGLE Rune Mathisen
Koden er lisensiert under en GPLv3-lisens 
Se http://www.gnu.org/licenses/gpl-3.0.html 
'''

def f(x):
    '''Funksjonen som er gitt i oppgava.'''
    return (1/4)*x**3 - (3/4)*x**2 - x + 2

# --- Jobber først med en løsning som her fokus på antall iterasjoner
it = 7 # Antall iterasjoner som skal utføres
a = 1 # startpunkt på venstre side av nullpunktet
b = 2 # startpunkt på høyre side av nullpunktet
print('=== Starter beregning ===')
for i in range(it):   # kjør iterasjonen et gitt antall ganger
    x = (a + b)/2       # velg x midt mellom a og b
    print('Iterasjon', i)
    print('Nå er x =', x)
    if f(a)*f(x) > 0:   # hvis produktet er større enn null
        a = x                # sett a til x-verdien
    else:               # ellers
        b = x                # sett b til x-verdien
                        # gjenta 

# --- Så prøver vi en løsning som har fokus på presisjonen i svaret
a = 1 # startpunkt på venstre side av nullpunktet
b = 2 # startpunkt på høyre side av nullpunktet
TOL = 1E-9 # toleranse: hvor nærme svaret skal vi komme før vi er fornøyde?
print('=== Starter beregning ===')
while abs(a - b) > TOL: # så lenge avstanden mellom a og b stor
    x = (a + b)/2       # velg x midt mellom a og b
    print('Nå er x=', x)
    if f(a)*f(x) > 0:   # hvis produktet er større enn null
        a = x                # sett a til x-verdien
    else:               # ellers
        b = x                # sett b til x-verdien
                        # gjenta 

print("Løsningen er x=", x)
