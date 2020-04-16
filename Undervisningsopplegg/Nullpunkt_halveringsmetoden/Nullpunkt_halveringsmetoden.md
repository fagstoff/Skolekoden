# Å finne nullpunkt med halveringsmetoden

Dette er et undervisningsopplegg hvor elevene skal bruke algoritmisk tenking i utforskning og problemløsning i matematikk.

## Innhold og rekkefølge

Undervisningsopplegget gjennomføres i den rekkefølgen som er angitt nedenfor. Det skal ikke brukes noen hjelpemidler i punkt 1-5. Anbefalt tidsbruk er 3-4 timer.

1. Vi leker "Gjett tallet"
2. Algoritmen med ord
3. Vi ser på grafen
4. Gruppearbeid: Elevene jobber med arbeidsarket.
5. Fellesarbeid - Lærer og klassen reflekterer over resultatene
6. Implementering i Python
7. Fellesarbeid - Lærer og klassen reflekterer over resultatene
8. Oppsummering
9. Vurdering av kompetanse

## 1. Vi leker "Gjett tallet"

"Gjett tallet" er en lek som de aller fleste kjenner. Det fine med denne leken er at mange bruker halvveringsmetoden for å komme fram til riktig tall med færrest mulig forsøk.

Opplegget startes ved at lærer gjennomfører denne leken noen ganger sammen med klassen. Lærer kan for eksempel velge seg et tilfeldig tall mellom 1 og 20, og be elevene om å gjette tallet. Når elevene gjetter, skal læreren svare "for høyt", "for lavt" eller eventuelt "riktig!".

Etter at læreren har gjennomført en runde, kan elevene jobbe 2 og 2 med den samme leken. Understrek for elevene at det er viktig at de bruker færrest mulig forsøk når de førsøker å finne tallet.

## 2. Algoritmen med ord

Når "Gjett tallet" er gjort noen ganger, gjennomføres en plenumsdiskusjon om hvilke strategier de valgte når de gjettet seg fram til tallet. Elevene skal formulere en [algoritme](https://snl.no/algoritme) med ord. Introduser begrepet algoritme for elevene. SNL definerer det slik: 

> "_...en fullstendig og nøyaktig beskrivelse av fremgangsmåten for løsning av en beregningsoppgave eller annen oppgave._"

Som en oppsummering av denne delen skal elevene bli enige om den "beste" algoritmen for å kommer frem til riktig tall (den som gir færrest gjettinger). Det finnes det [flere mulige algoritmer for å komme fram til nullpunktet](Nullpunkt_halveringsmetoden_algoritmer.md).

## 3. Vi ser på en graf

Vi ser på grafen til <code>f(x)&nbsp;=&nbsp;&frac14;x<sup>3</sup>&nbsp;-&nbsp;&frac34;x<sup>2</sup>&nbsp;-&nbsp;x&nbsp;+&nbsp;2</code>.
([bilde](Nullpunkt_halveringsmetoden.png)) på storskjerm. Snakk med elevene om hva som kan være en god strategi for å "gjette" seg inn mot nullpunktet. Sammenlign med leken i punkt 1. Vis hvordan første tilnærming i nullpunktsmetoden gjøres: velg to punkter som ligger på hver side av ett av nullpunktene, og velg så en x-verdi som ligger midt mellom disse to punktene. Hva gjør vi videre?

## 4. Gruppearbeid: Elevene jobber med arbeidsarket

Del ut [arbeidsarket](Nullpunkt_halveringsmetoden_arbeidsark.pdf) ([docx](Nullpunkt_halveringsmetoden_arbeidsark.docx)) og be elevene om å jobbe i grupper. De må formulere [algoritmen](https://snl.no/algoritme) med ord, og de skal vise grafisk og med utregning hvordan man beregner nytt midtpunkt for fem gjentagelser. Introduser gjerne begrepet [iterasjon](https://snl.no/iterasjon).

Du kan også laste ned et [løsningsforslag til arbeidsarket](Nullpunkt_halveringsmetoden_løsningsforslag.pdf) ([docx](Nullpunkt_halveringsmetoden_løsningsforslag.docx)).

## 5. Fellesarbeid - Lærer og klassen reflekterer over resultatene

Nå er det tid for fellesrefleksjon der gruppene muntlig presenterer sine funn. Læreren legger til rette for dette, og skriver opp løsningsalgoritmen. Ord som *hvis* og *gjenta* og liknende bør utheves. Det bør også snakkes litt om begreper og at en algoritme er en trinnvis oppskrift. Utfordre elevene til å tenke over om andre ville forstått oppskriften (løsningsalgoritmen).

## 6. Implementering i Python

Elevene fortsetter nå med å jobbe i grupper. Nå skal algoritmen implementeres i Python! Bruk god tid. Lærer går rundt og veileder. [Et løsningsforslag er gitt her](Nullpunkt_halveringsmetoden.py).

Det er ikke nødvendig for elevene å ha Python installert på egne datamaskiner. Her er noen online-ressurser som kan brukes til denne oppgava:

* [repl.it](https://repl.it/languages/python3)
* [trinket.io](https://trinket.io/python3)
* [Azure Notebooks](https://notebooks.azure.com/)

## 7. Fellesarbeid - Lærer og klassen reflekterer over resultatene

Nå er det tid for fellesrefleksjon der gruppene muntlig presenterer sine funn. Læreren legger til rette for presentasjonene, og skriver ned en mulig løsning i Python. Dette er en fin anledning til å sammenlikne resultatene på arbeidsarket med programmet. Demonstrer ulikt antall iterasjoner/toleranse. Vi eksempler på når algoritmen feiler, for eksempel uheldige valg av startverdier for a og b.

## 8. Oppsummering

Oppsummering og test på andre funksjoner og oppgaver.

* <code>_g(x)&nbsp;=&nbsp;-3x&nbsp;-&nbsp;8_</code>
* <code>_h(x)&nbsp;=&nbsp;-x<sup>2</sup>&nbsp;+&nbsp;4x&nbsp;-&nbsp;5_</code> (har ingen reelle nullpunkter)
* <code>_k(x)&nbsp;=&nbsp;2x&nbsp;-&nbsp;2<sup>x</sup>&nbsp;+&nbsp;2_</code>

## 9. Vurdering av kompetanse

Med den kunnskapen og de ferdighetene elevene har hatt mulighet til å tilegne seg gjennom aktivitetene i dette undervisningsopplegget, bør de kunne finne nullpunkter til alle reelle funksjoner. De kan nå for eksempel vise kompetansen sin i nye og ukjente sammenhenger gjennom å bruke nullpunktsmetoden for å løse likninger eller finne skjæringspunktet til grafene for to funksjoner. Her er noen forslag:

* Finn skjæringspunktet til grafene for funksjonene <code>_g(x)&nbsp;=&nbsp;-3x&nbsp;-&nbsp;8_</code> og <code>_h(x)&nbsp;=&nbsp;&nbsp;-x<sup>2</sup>&nbsp;+&nbsp;4x&nbsp;-&nbsp;5_</code>.
* Løs likningen <code>_-3x&nbsp;-&nbsp;8&nbsp;=&nbsp;-x<sup>2</sup>&nbsp;+&nbsp;4x&nbsp;-&nbsp;5_</code>.
* Løs likningen <code>_cos(x)&nbsp;=&nbsp;x_</code>.

---

_Dette undervisningsopplegget er laget av [fuzzbin](https://github.com/fuzzbin) og [bitjungle](https://github.com/bitjungle). Oppgaven er lisensiert under en [Creative Commons Navngivelse-DelPåSammeVilkår 4.0 Internasjonal lisens.](http://creativecommons.org/licenses/by-sa/4.0/)_