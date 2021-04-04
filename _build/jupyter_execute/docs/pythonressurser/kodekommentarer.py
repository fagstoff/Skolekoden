# Kodekommentarer og dokumentasjon
__Creative Commons BY-SA : bitjungle (Rune Mathisen) og fuzzbin (Tom Jarle Christiansen)__

<hr/>

**Når du skriver programkode bør du tenke på at du selv skal forstå hva du har gjort når du finner fram koden igjen om et år. Kanskje må også andre enn deg kunne lese og forstå koden din. Da er det viktig å skrive gode kodekommentarer, og å dokumentere hva alle funksjoner og moduler gjør.**

Programmeringsspråket Python har en egen standard for hvordan god Python-kode skal se ut. Denne standarden heter [PEP-8](https://www.python.org/dev/peps/pep-0008/), og du bør gjøre deg kjent med hva som står i standarden. I dette dokumentet skal vi se nærmere på hva PEP-8 sier om [kodekommentarer og dokumentasjon](https://www.python.org/dev/peps/pep-0008/#comments).

## Kodekommentarer
Kommentarer i koden din bør være fullstendige setninger, og de bør beskrive hva koden faktisk gjør. Husk at du må oppdatere kommentarer når du endrer koden, sånn at du ikke ender opp med kommentarer som ikke stemmer overens med koden.

Du bør siden skrive alle kommentarene dine på engelsk. Det er veldig få mennesker her i verden som forstår norsk, og om du dokumenterer på norsk er det veldig få mennesker som vil ha mulighet til å sette seg inn i koden din. I dette kurset kan du skrive kommentarer på norsk.

En kommentarlinje starter med en enkelt `#`. Her er et eksempel:

# Loading the math library.
import math

# Print help for the ceil function.
help(math.ceil)

Du kan også skrive en kommentar på samme linje som en kodesnutt, men ikke bruk denne teknikken for mye, og ikke skriv noe som er opplagt. Kommentaren din bør utfylle koden. Her er et eksempel på en unyttig kommentar, og et eksempel på en kommentar som gir ekstra informasjon.

t = 0.001 # Give variable x the value 0.001

a = math.log10(1/t) # Converting from transmittance to absorbance (spectroscopy)

print('t = {} => a = {}'.format(t, a))

## Dokumentasjonsstrenger
I python er det vanlig å skrive det som kalles [docstrings](https://en.wikipedia.org/wiki/Docstring#Python) for å dokumentere funksjoner og programmer. Når en bruker skriver kommandoen ```help()```, så er det docstringen som vises. I større prosjekter er det vanlig å lage docstrings i begynnelsen av programmet, men også til hver funksjon. 

Eksempelet under viser hvordan man kan skrive en docstring i en funksjon.

def sum_av_to_tall(a, b):
    '''
    Denne funksjonen returnerer summen av to tall.
    Tallene sendes inn som to innparameter. a og b.
    '''
    return a + b

Vi kan nå bruke kommandoen ```help(sum_av_to_tall)``` for å skrive ut docstringen.

help(sum_av_to_tall)

La oss nå kjøre funksjonen:

sum_av_to_tall(3, 9)

Utfordring: Kan du forklare neste kodelinje i detalj til en medelev?

tall1 = 3
tall2 = 9
print('Summen av {} og {} er {}'.format(tall1, tall2, sum_av_to_tall(tall1, tall2)))