''' Dette er et forslag til alternativ løsning på punkt 6 i dette undervisningsopplegget:
https://github.com/fagstoff/Skolekoden/blob/master/Undervisningsopplegg/Nullpunkt_halveringsmetoden/Nullpunkt_halveringsmetoden.md
Copyright (C) 2020 BITJUNGLE Rune Mathisen og FUZZBIN Tom Jarle Christiansen
Koden er lisensiert under en GPLv3-lisens 
Se http://www.gnu.org/licenses/gpl-3.0.html 
'''

# Definerer funksjonen
def f(x):
    '''Funksjonen som er gitt i oppgava.'''
    return (1/4)*x**3 - (3/4)*x**2 - x + 2

# Den deriverte av funksjonen
def df(x):
    return (3/4)*x**2 - (6/4)*x -1

# Siste ledd i Newtons metode
def h(x):
    return f(x) / df(x)

x_0 = -3 # Startpunkt
n = 5 # Antall iterasjoner

x_liste = [x_0]

# Løkke som kjører n iterasjoner av Newtons metode
for i in range(n):
    x_liste.append(x_liste[-1] - h(x_liste[-1])) # Newtons metode
    print("Startverdi: {} - Iterasjon: {} - Beregnet verdi: {}".format(x_0, i, x_liste[-1]))