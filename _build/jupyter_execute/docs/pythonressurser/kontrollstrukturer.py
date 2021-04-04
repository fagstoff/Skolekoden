# Kontrollstrukturer
__Creative Commons BY-SA : bitjungle (Rune Mathisen) og fuzzbin (Tom Jarle Christiansen)__

<hr/>

**En kontrollstruktur i et dataprogram er kodeblokk som velger en vei gjennom programmet basert på analyse av en eller flere variabler. Kontrollstrukterer i dataprogrammer er helt grunnleggende kode for å få et dataprogram til å reagere på en bestemt måte når en spesiell tilstand inntreffer.**

Tenk deg at du står ved et lyskryss. Du ser på lyset, og ta en avgjørelse. Er det grønt, kan du gå over krysset. Er det rødt, må du vente. 

Trafikklyset er en variabel, og du må prosessere denne variablen for å velge korrekt utfall. I dataprogrammer gjør vi på samme måte. Vi må hele tiden vurdere verdien til en eller flere variabler, og så ta beslutninger ut ifra hvilken verdi variablene har.

Det finnes to hovedtyper av kontrollstrukturer, og vi skal se nærmere på disse nedenfor. I det praktiske eksemplet med lyskrysset, kan vi tenke oss to ulike løsninger:

1. Dersom trafikklyset er rødt så VENT, ellers GÅ.
2. Så lenge trafikklyset er grønt, så fortsett å gå.

Den første løsningen er en såkalt **betinget struktur**, og den andre løsningen er en **løkke**. For at den andre løsningen skal fungere i dette eksemplet, må vi ha en rutine for å stoppe når betingelsen (_"...så lenge det er grønt..."_) opphører å være sann.

Det er kanskje ikke sånn helt umiddelbart klart for deg hva som er forskjellen på de to løsningene, men det blir helt sikkert enklere å forstå når vi har laget noen praktiske programmeringseksempler.

## Betingede strukturer  (tester)

I nesten alle programmer vil man før eller siden få behov for å teste eller sammenligne verdier slik at programmet kan gjøre ulike ting avhengig av resultatet på testen.

### if-test

La oss starte med trafikklys-eksemplet. Siden det bare kan ha to mulige verdier (rødt eller grønt), kan vi bruke en boolsk variabel for å representere trafikklyset. Enten er det grønt, ellers er det ikke grønt. Dette kan programmeres slik (forsøk å endre variablen `grønt` fra `True` til `False`):


grønt = True

if grønt:
    print("Du kan gå.")
else:
    print("Du må vente.")

If-kommandoen bruker operatorer til å sammenlikne to verdier, og resultatet av en if-test er enten sann eller falsk. I eksempelet under skrives teksten ut _bare_ hvis variabelen a er lik 1. Prøv å endre på verdien til a, og se hva som skjer.

a = 3

if a == 3:
    print("Variablen a er akkurat helt lik 3")
else:
    print("Verdien til variablen a er ", a)


Ofte ønsker man å gjøre litt mer avanserte ting enn kun å sjekke om to størrelser er like. Dette kan løses ved å bruke ulike operatorer. På denne måten kan man sjekke om to størrelser er større enn, mindre enn eller ulike hverandre. Man kan også kombinere flere tester med logiske operatorer som og og eller. Vi kan også lage større og mer sammensatte tester ved å kombinere kommandoene if, elif og else.

I tester brukes dobbelt likhetstegn hvis man skal sjekke om to verdier er like. I en test bruker man [logiske sammenligningsoperatorer](https://docs.python.org/3/reference/expressions.html#value-comparisons).

La oss se på flere eksempel der vi bruker ulike operatorer.

tall1 = 9
tall2 = 7

if tall1 == tall2:
    print("tall1 er lik tall2")

if tall1 > tall2:
    print("tall1 er større enn tall2")

if tall1 >= tall2:
    print("tall1 er større eller lik tall2")
    
if tall1 != tall2:
    print("tall1 er ulik tall2")

### elif og logiske kombinasjoner i tester

Noen ganger kan det være nødvendig å kombinere flere typer uttrykk og operatorer for å få testet det man ønsker. Hvis man ønsker å kombinere flere tester etter hverandre, brukes kommandoene _elif_ og _else_. Hvis man ønsker å teste flere ting i samme test, brukes kommandoene [_and_](https://en.wikipedia.org/wiki/Logical_conjunction) og [_or_](https://en.wikipedia.org/wiki/Logical_disjunction)


tall1 = 12
tall2 = 11

if tall1 >= tall2 and tall2 % 2 == 0:
    print("tall1 er større eller lik tall2 OG tall2 er et partall")

elif tall1 != tall2 or tall1 + tall2 > 10:
    print("tall1 er ulik tall2 ELLER tall1 pluss tall2 er større enn 10")

else:
    print("Ingen av de foregående if-testene slo til når dette vises")

## Løkker


**I programmering har vi ofte behov for å gjenta kode mange ganger. For å få til dette bruker man løkker. Løkker har mye til felles med tester, men med den forskjellen at i en løkke gjentas kode intill en betingelse er sann eller usann.**

Det finnes to hovedtyper løkker - for-løkker og while-løkker:

+ **for** - Gjentar kode et gitt antall ganger
+ **while** - Gjentar kode sålenge en betingelse er sann

### For-løkker

I en for-løkke bestemmer vi hvor mange ganger en kode skal gjentas. Alt dette gjøres i deklarasjonen av løkka. Legg spesielt merke til kommandoen [_range()_](https://docs.python.org/3/library/stdtypes.html#range).

for tall in range(10):
    print("Tellevariabelen tall har nå verdien", tall)

## While-løkker


En [while-løkke](https://en.wikipedia.org/wiki/While_loop#Python) har veldig lik funksjonalitet som for-løkker. Forskjellen er at i en while-løkke så må tellevariabelen deklarereres på forhånd, og den må økes eller minkes manuelt inne i koden. Alt dette gjøres i deklarasjonen på en for-løkke.


teller = 0
while teller < 9:
   print("Telleren har nå verdien:", teller)
   teller = teller + 1
print("while-løkken er nå avsluttet")

La oss avslutte denne leksjonen med lyskryss-eksemplet vårt, men for å unngå at vi får en løkke som går evig lager vi en teller som endrer fra grønt til rødt etter et gitt antall gjentagelser. I eksempelet under tenker vi oss et system som trekker ut hver 8. passasjerer til utvidet sikkerhetskontroll på en flyplass. Vi starter med person 7, og teller ned til 0.

grønt = True
person = 7

while grønt:
    print("Gå på grønn sone")
    person = person - 1
    if (person <= 0):
        grønt = False
        print("Gå til rød sone!")

## Oppgaver

1. Lag en for-løkke som teller fra 0 til 20.
2. Lag en for-løkke som teller fra 10 til 1.
3. Lag en for-løkke som teller annenhvert tall fra 10 til 50.
4. Lag et program der brukeren kan taste inn et tall. Programmet skriver så ut tallene fra 0 til det brukeren har tastet inn.
5. Lag et program der brukeren kan taste inn et tall. Programmet skriver så ut _"tallet er større enn 5"_, _"tallet er lik 5"_ eller _"tallet er mindre enn 5"_ avhengig av hva slags tall brukeren tastet inn.

