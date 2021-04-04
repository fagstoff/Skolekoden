# Variabler
__Creative Commons BY-SA : bitjungle (Rune Mathisen) og fuzzbin (Tom Jarle Christiansen)__

<hr/>

**I nesten alle programmer har vi behov for å behandle og manipulere tall og tekst. For å få til dette er vi helt avhengige av å kunne lagre denne informasjonen et sted. Dette gjøres ved hjelp av variabler.**

En variabel i programmering brukes på samme måte som i matematikk. Variablen representeres med et symbol eller navn som kan inneholde en verdi. Denne verdien kan være et tall, en tekst, en liste eller helt andre ting. En variabel kan som oftest endre sin verdi etter at den er laget.

Variabler kan ha mange ulike typer innhold. Dette kalles for datatyper. Noen av disse har også undertyper, for eksempel datatypen *tall* (number) som bl.a. har undertypene *heltall* (integer) og *desimaltall* (float).

Python har mange ulike [datatyper](https://docs.python.org/3/library/stdtypes.html), her er noen av de viktigste:

>+ `Numbers -> 3 eller 3.1415926`
>+ `String  -> "Hallo verden!"`
>+ `Boolean -> True eller False`
>+ `List    -> [123, "Rune"]`
>+ `Tuple   -> (123, "Tom Jarle")`
>+ `Dictionary -> {"fag": "Programmering", "type": "Realfag", "inntakspoeng": 45.6}`

La oss se på noen eksempler der vi lager og bruker noen disse variabeltypene. 

Vi tilordner en verdi til en variabel med et likhetstegn `=`. 

tall1 = 10
print(tall1, "er et heltall.")

tall2 = 10.0
print(tall2, "er et desimaltall.")

Du kan finne ut hvilken datatype en variabel er ved å bruke den innebygde funksjonen `type`.



print("Variablen tall1 har datatypen: ", type(tall1))
print("Variablen tall2 har datatypen: ", type(tall2))

Men variabler trenger ikke bare å inneholde tall, det går så klart an å fylle dem med tekst også. I Python kalles slike variabler for "strenger". La oss prøve å lage en sånn variabel.

tekst = "Dette er en tekst!"
print(tekst, "er en tekst.")

Boolske variabler er variabler som bare har to mulige verdier: `True` eller `False`.

sant_eller_usant = True
print(sant_eller_usant, "er en boolsk verdi.")

## Lister og tupler
Nå har du sett de grunnleggende datatypene i Python, men det går også an å gruppere og organisere disse på ulike måter. En liste er samling av dataelementer som kan være av ulike typer, for eksempel tall eller tekst. Når du skal lage en liste, bruker du `[]`.

Hver element i en liste kan refereres til med en indeks, men vær oppmerksom på at det første elementet i en liste har indeksen 0 (ikke 1 som en kanskje skulle tro). I eksemplet nedenfor endrer vi på den fjerde dataenheten i lista, og da bruker vi indeksen 3. 

liste = [1, 2, 3, "Heisann", 4]
print(liste, "er en liste.")
liste[3] = "Hohoho"
print("Nå ser den slik ut: ", liste)

En tuppel er en spesiell type liste hvor elementene ikke kan endres. Når du lager en ny liste, bruker du `()`.

tuppel = (5, 6, 7, "Hoppsann", 8)
print(tuppel, "er en tuppel.")
print("I motsetning til en liste, er det ikke mulig å endre verdiene i en tuppel.")
print("Den neste linja vil derfor gi en feilmelding")
tuppel[3] = "Heisann"


## Dictionary

En dictionary i Python er en nyttig datatype i Python for å lagre data på en strukturert måte. I denne datatypen gir du selv navn til indeksene, istedenfor at du får tildelt indekser som 0, 1, 2, ... slik som i lister og tupler. Her er et eksempel på hvordan du kan lage en dictionary.

dict = {"fabrikant": "BMW", "modell": "X3", "akselr": 4.8, "seter": 7}
print(dict, " er en dictionary.")
dict["seter"] = 5
print("Nå ser den slik ut: ", dict)

## Dokumentasjon
Her finner du utfyllende dokumentasjon på hvordan de ulike datatypene kan brukes:

* [Numeric Types — int, float, complex](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
* [Sequence Types — list, tuple, range](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
* [Text Sequence Type — str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)


## Bruk riktig datatype
Det er viktig å holde styr på hva slags datatype du bruker i programmene dine, og at du bruker riktig datatype til den oppgaven du skal løse. Nedenfor ser du noen eksempler på resultatet av å legge sammen tall med forskjellige datatyper. Det er ikke mulig å bruke + mellom to ulike datatyper (forsøk gjerne å gjøre det nedenfor).

a = "2"
b = "3"
c = 2
d = 3
e = 2.0
f = 3.0
mine_tall = {"g": 2, "h": 3}

print("a + b = ", a + b)
print("a + b = ", int(a) + int(b))
print("a + b = ", float(a) + float(b))
print("c + d = ", c + d)
print("e + f = ", e + f)
print("g + h = ", mine_tall["g"] + mine_tall["h"])

## Variabelnavn
I matematikk er det populært å bruke $x$ og $y$ og andre bokstaver som variabelnavn. I Python er det vanlig praksis å gi variablene navn som er beskrivende for innholdet. Dersom variabelnavnet inneholder flere ord, skiller du mellom ordene med et understrek-tegn ( _ ). Eksempler:

vekt_bil = 1788
vekt_sykkel = 9
vekt_differanse = vekt_bil - vekt_sykkel
print("Vektforskjellen mellom bil og sykkel er", vekt_differanse,  "kg.")

## Fysikkeksempel
La oss se på et enkelt eksempel fra fysikken der vi ser på hvordan vi regner ut tilbakelagt strekning når vi vet den konstante farten og tiden. I eksempelet brukes variabler av datatypen _Numbers_ (int)

$$s=v \cdot t$$

Hvis vi lar $v=20\textrm{ m/s}$ og $t=30\textrm{s}$ så kan vi regne ut tilbakelagt strekning på følgende måte.

$$ s = 20 \cdot 30 $$
$$ s= \underline{\underline{600\textrm{ m}}}$$

I Python ville samme eksempel bli løst som vist under:

fart = 20
tid = 30

strekning = fart * tid

print("Tilbakelagt strekning er", strekning, "meter.")

## Mer om variabler og matematikk

Det er _mye_ å lære om variabler, og i dette kurset vil vi såvidt se på noen av de viktigste egenskapene.
Tabellen under viser noen variableoperasjoner med tilhørende resultat:

| Kommando | Resultat      | Kommentar  |
|:--------|:-------------| :---------|
| 2 + 2           | 4  | Sum/diff av heltall ([int](https://no.wikipedia.org/wiki/Heltall)) gir heltall som svar|
| 2 + 3\*6        | 20 | Vanlig regnerekkefølge gjelder |
| (50 - 5\*6) / 4 | 5.0| Divisjon gir _alltid_ et desimaltall ([float](https://en.wikipedia.org/wiki/Floating-point_arithmetic))|
| 5 \*\* 2 | 25 | \*\* brukes for å opphøye et tall med et annet |
| 7 // 3 | 2 | Heltallsdivisjon. Tallet 3 går 2 ganger opp i 7, med en rest på 1|
| 7 % 3 | 1 | Rest etter divisjon med største teller som går opp i nevner: $ 7 - 2\cdot3 = 1 $|


## Oppgaver

1. Lag et program som der du oppretter variablene _tall1_ og _tall2_. Skriv så ut resultatet av minst fem ulike operasjoner på disse tallene.
2. Lag et program der du deklarerer, tilordner verdi til variabler med ulike datatyper.
3. Lag et program der du konverterer fra en datatype til en annen.
4. Lag et program som viser om et tall er delelig på 2.
5. Bruk fysikkprogrammet ovenfor som utgangspunkt, men gjør det som slik at det regner ut fart når du kjenner strekning og tid (og antar at farten er konstant).
6. Klarer du å få programmet du laget i punkt 5. til å kræsje? Forklar hvorfor!


