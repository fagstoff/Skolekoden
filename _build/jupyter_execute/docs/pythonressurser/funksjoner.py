# Funksjoner
__Creative Commons BY-SA : bitjungle (Rune Mathisen) og fuzzbin (Tom Jarle Christiansen)__

<hr/>

**Funksjoner er helt sentrale i programmering. Vi kan tenke på en funksjon som en kodeblokk som utfører en bestemt oppgave. Den kan kjøres når, og så mange ganger vi selv ønsker det. Når vi bruker funksjoner i programmer reduserer vi utviklingskostnadene, fordi vi bare trenger å programmere en sammensatt operasjon en gang. I tillegg blir det enklere å feilsøke og vedlikeholde programmet.**

Før vi bruker en funksjon, må vi definere den. Deretter bruker vi funksjonen hjelp av et såkalt funksjonskall. Definisjon og kall til en funksjon kan se slik ut i Python:

```python
def funksjonsnavn(<innparameter>):
    <kode som skal kjøres>
    return <det som skal returneres>

for i in range(10):
    funksjonsnavn(<innparameter>)
```

I eksemplet under kalles funksjonen `hilsen()` tre ganger i en løkke.

def hilsen():
    print("Hallo verden!")
    return

for i in range(3):
    hilsen()

Mer avanserte funksjoner har [inn-/utparametre](https://en.wikipedia.org/wiki/Parameter_(computer_programming$29), som fungerer litt på samme måte som i matematikk. Dette er den aller vanligste bruksmåten for funksjoner.

Koden under viser en funksjon som summerer verdien de tre tallene a, b og c og returner resultatet:

def legg_sammen_tre_tall(a, b, c):
    return a + b + c

summen = legg_sammen_tre_tall(2, 4, 6)
print("Summen er", summen)

La oss se på et eksempel der vi lar en tekststreng være innparameter. Vi kjører så funksjonen to ganger, med ulike innparameter.

def personligHilsen(navn):
    print("Heisann", navn, "! Så hyggelig å se deg.")

personligHilsen('Fuzzbin')
personligHilsen('Bitjungle')

## Oppgaver

1. Lag en funksjon som tar imot tallene 1 til 7 som innparameter, og som returnerer ukedag som tekststreng (1 gir "mandag", 2 gir "tirsdag" og så videre). Hint: Legg ukedagene i en liste.
2. Lag en funksjon som regner om fra grader Celsius (innparameter) til Fahrenheit (returverdi). Formelen for omregning fra Celsius til Fahrenheit er: $F = \frac{9}{5}C + 32$. Skriv ut verdier fra 0 til 100 grader Celsius med tilhørende grader Fahrenheit.
3. Lag en funksjon som regner om fra grader Fahrenheit til Celsius.
4. Lag en funksjon som tar en liste med tall som innparameter og returnerer gjennomsnittet av tallen i lista.
5. Lag en funksjon som tar en liste med heltall som innparameter, og returnerer en liste med kun partallene fra lista som ble sendt inn.
6. Lag en funksjon som skriver ut n [fibonaccitall](https://en.wikipedia.org/wiki/Fibonacci_number), der n er et heltall som sendes som innparameter.


