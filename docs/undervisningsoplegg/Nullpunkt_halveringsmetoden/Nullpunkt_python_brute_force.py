''' Dette er et forslag til alternativ løsning på punkt 6 i dette undervisningsopplegget:
https://github.com/fagstoff/Skolekoden/blob/master/Undervisningsopplegg/Nullpunkt_halveringsmetoden/Nullpunkt_halveringsmetoden.md
Copyright (C) 2020 BITJUNGLE Rune Mathisen
Koden er lisensiert under en GPLv3-lisens 
Se http://www.gnu.org/licenses/gpl-3.0.html 
'''

def f(x):
    '''Funksjonen som er gitt i oppgava.'''
    return (1/4)*x**3 - (3/4)*x**2 - x + 2

x = 1.0   # Velger en startverdi som vi tror at ligger til venstre for nullpunkt
dx = 1E-4 # Legger til x for hver gang vi sjekker om vi har passert et nullpunkt

while f(x)*f(x+dx) > 0: # Så lenge produktet er positivt har svarene samme fortegn
    print('Nå er x=', x)
    x += dx # Lager ny x-verdi, og prøver på nytt

print("Løsningen er x=", x)