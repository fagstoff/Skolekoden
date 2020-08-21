# Introduksjon til tall og tallfølger med Python
# Et undervisningsopplegg for matematikk 1T
#
# Ingen forkunnskaper i Python er nødvendig
# Tidsbruk er 1-2 timer
# Anbefalt programvare er https://codewith.mu/
# eller https://trinket.io/python
#
# Vis bare ett steg til elevene av gangen, slik det er angitt i 
# koden nedenfor, og gjennomfør gode diskusjoner i hvert enkelt steg
#
# Copyright © BITJUNGLE Rune Mathisen
# Denne koden er lisensiert med en GPLv3-lisens
# Se http://www.gnu.org/licenses/gpl-3.0.html

# Steg 1 - Lære print-kommandoen
print("Hallo verden")

# Steg 2 - Bruke en variabel
navn = "Rune"
print("Hallo", navn)

# Steg 3 - Prøve matematikk-operatorer
print(2+3)
print(4-7)
print(8*7)
print(7/2)
print(2**4)

# I steg 4 og 5 bruker jeg ulike variabelnavn for å demonstrere
# at navnet i seg selv ikke har noen betydning.

# Steg 4 - Lære å telle i en løkke
for tall in range(1, 10): # Legg merke til at 10 er endepunkt for range() her
    print(tall)           

# Steg 5 - Diskutere naturlige tall, og formattere output
for x in range(1, 11): # Legg merke til at 11 er endepunkt for range() her
    print(x, end=" ")
print("...er naturlige tall (N)")

# Resten av økta baserer seg på at elevene kopierer de tre kodelinjene 
# ovenfor, og modifiserer denne i de neste stega. Da går kodinga
# raskere, og det reduserer sjansene for feil. Derfor er det ekstra 
# viktig at steg 5 fungerer hos alle elevene. Lær også elevene hvordan
# de kopierer og limer inn med tastaturet.

# Steg 6 - Sammenlikne definisjonen av naturlige tall og hele tall
for x in range(-5, 6):
    print(x, end=" ")
print("...er hele tall (Z)")

# Steg 7 - Bruke en matematisk operator i en løkke
for x in range(0, 11):
    print(2*x, end=" ")
print("...er partall")

# Steg 8 - Sammenlikne uttrykk for partall og oddetall
for x in range(0, 11):
    print(2*x + 1, end=" ")
print("...er oddetall")

# Steg 9 - Diskutere rasjonale tall
for x in range(-5, 6):
    print(x/5, end=" ")
print("...er rasjonale tall (Q)")

# Steg 10 - Studere kvadrattall
for x in range(0, 11):
    print(x**2, end=" ")
print("...er kvadrattall")

# Steg 11
# Elevene lager sine egne favoritt-tallfølger

# Steg 12 
# Elevene utfordrer medelever til å finne ut hvordan de laget tallfølgen