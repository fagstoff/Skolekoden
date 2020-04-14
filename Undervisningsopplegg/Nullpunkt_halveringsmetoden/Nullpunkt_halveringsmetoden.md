# Å finne nullpunkt med halveringsmetoden

Dette er et undervisningsopplegg hvor elevene skal bruke algoritmisk tenking i utforskning og problemløsning i matematikk.

Utgangspunktet er [læreplan for matematikk 1T](https://www.udir.no/lk20/mat09-01) som gjelder fra 1.8.2020. Relevante kompetansemål for undervisningsopplegget er:

* formulere og løyse problem ved hjelp av algoritmisk tenking, ulike problemløysingsstrategiar, digitale verktøy og programmering
* utforske strategiar for å løyse likningar, likningssystem og ulikskapar og argumentere for tenkjemåtane sine
* utforske og beskrive eigenskapane ved polynomfunksjonar, rasjonale funksjonar, eksponentialfunksjonar og potensfunksjonar

Undervisningsopplegget er knyttet til [kjerneelementene](https://www.udir.no/lk20/mat09-01/om-faget/kjerneelementer) "utforsking og problemløysing", "representasjon og kommunikasjon" og "resonnering og argumentasjon".

En nærmere beskrivelse av hvordan vi har jobbet under utarbeidelsen av dette undervisningsopplegget er gitt i dokumentet [Forslag til arbeidsmåte for å lage undervisningsopplegg i matematikk](../Forslag_til_arbeidsmåte_for_å_lage_undervisningsopplegg_i_matematikk.md).

I det følgende er det gitt en detaljert beskrivelse av hvordan vi har tenkt at dette undervisningsopplegget skal gjennomføres.

## Innhold og rekkefølge

Undervisningsopplegget gjennomføres i den rekkefølgen som er angitt nedenfor. Det skal ikke brukes noen hjelpemidler i punkt 1-5. Anbefalt tidsbruk er 3-4 timer.

1. Gjett tallet
2. Algoritmen med ord
3. Vi ser på grafen
4. Gruppearbeid: Elevene jobber med arbeidsarket.
5. Fellesarbeid - Lærer og klassen reflekterer over resultatene
6. Implementering i Python
7. Fellesarbeid - Lærer og klassen reflekterer over resultatene
8. Oppsummering
9. Vurdering

## 1. Gjett tallet

"Gjett tallet" er en lek som de aller fleste kjenner. Det fine med denne leken er at mange bruker halvveringsmetoden for å komme fram til riktig tall med færrest mulig forsøk.

Opplegget startes ved at lærer gjennomfører denne leken noen ganger sammen med klassen. Lærer kan for eksempel velge seg et tilfeldig tall mellom 1 og 20, og be elevene om å gjette tallet. Når elevene gjetter, skal læreren svare "for høyt", "for lavt" eller eventuelt "riktig!".

Etter at læreren har gjennomført en runde, kan elevene jobbe 2 og 2 med den samme leken. Understrek for elevene at det er viktig at de bruker færrest mulig forsøk når de førsøker å finne tallet.

## 2. Algoritmen med ord

Når "Gjett tallet" er gjort noen ganger, gjennomføres en plenumsdiskusjon om hvilke strategier de valgte når de gjettet seg fram til tallet.

På [Wikipedia](https://no.wikipedia.org/wiki/Algoritme) er en algoritme definert slik: 

> "_I matematikk og informatikk er en algoritme en presis beskrivelse av en endelig serie operasjoner som skal utføres for å løse et problem eller flere problemer. Hvis en prosess er algoritmisk, kan den skrives som en serie operasjoner som kan utføres gjennom beregninger._"

Som en oppsummering av denne delen skal elevene bli enige om den "beste" algoritmen for å kommer frem til riktig tall (den som gir færrest gjettinger). Finnes det alternative algoritmer som også finner det ukjente tallet?

## 3. Vi ser på en graf

Vi ser på grafen til $f(x)=\frac{1}{4}x^3-\frac{3}{4}x^2-x+2$.  
([bilde](Nullpunkt_halveringsmetoden.png)) på storskjerm. Snakk med elevene om hva som kan være en god strategi for å "gjette" seg inn mot nullpunktet. Sammenlign med leken i punkt 1. Vis hvordan første tilnærming i nullpunktsmetoden gjøres: velg to punkter som ligger på hver side av ett av nullpunktene, og velg så en x-verdi som ligger midt mellom disse to punktene. Hva gjør vi videre?

## 4. Gruppearbeid: Elevene jobber med arbeidsarket

Del ut [arbeidsarket](Nullpunkt_halveringsmetoden.docx) og be elevene om å jobbe i grupper. De må formulere [algoritmen](https://ordbok.uib.no/perl/ordbok.cgi?OPP=algoritme) med ord, og de skal vise grafisk og med utregning hvordan man beregner nytt midtpunkt for fem gjentagelser. Introduser gjerne begrepet [iterasjoner](https://ordbok.uib.no/perl/ordbok.cgi?OPP=iterasjon).

## 5. Fellesarbeid - Lærer og klassen reflekterer over resultatene

Nå er det tid for fellesrefleksjon der gruppene muntlig presenterer sine funn. Læreren legger til rette for dette, og skriver opp løsningsalgoritmen. Ord som *hvis* og *gjenta* og liknende bør utheves. Det bør også snakkes litt om begreper og at en algoritme er en trinnvis oppskrift. Utfordre elevene til å tenke over om andre ville forstått oppskriften (løsningsalgoritmen).

## 6. Implementering i Python

Elevene fortsetter nå med å jobbe i grupper. Nå skal algoritmen implementeres i Python! Bruk god tid. Lærer går rundt å veileder. [Et løsningsforslag er gitt her](Nullpunkt_halveringsmetoden.py).

## 7. Fellesarbeid - Lærer og klassen reflekterer over resultatene

Nå er det tid for fellesrefleksjon der gruppene muntlig presenterer sine funn. Læreren fasiliserer og skriver opp en løsning i Python. Dette er en fin anledning til å sammenlikne resultatene på arbeidsarket med programmet. Demonstrer ulikt antall iterasjoner. Vi eksempler på når algoritmen feiler.

## 8. Oppsummering

Oppsummering og test på andre funksjoner og oppgaver.

Mer tekst her

## 9. Vurdering

* Løse likninger (forslag kommer)

_Dette undervisningsopplegget er laget av [fuzzbin](https://github.com/fuzzbin) og [bitjungle](https://github.com/bitjungle). Oppgaven er lisensiert under en [Creative Commons Navngivelse-DelPåSammeVilkår 4.0 Internasjonal lisens.](http://creativecommons.org/licenses/by-sa/4.0/)_