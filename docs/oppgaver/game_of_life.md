# Conway's Game of Life

## Oppgave

Conway er kjent som oppfinner av spillet Game of Life (eller kort Life), som var en videreutvikling og forenkling av ideer fra John von Neumann. Spillet ble først publisert i 1970 i Scientific American innenfor Martin Gardners rubrik Mathematical Games. Spillet har det teoretiske potentiale av en Turing maskin, det vil si alt som kan beregnes algoritmisk kan også beregnes innenfor Game of Life. På grunn av Lifes analogier med vekst, nedgang og forandring tilhører den den økende klassen av såkalte simulation games. Spillet har fått avgjørende betydning for utviklingen av såkalte cellulære automater. (Fra [SNL](https://snl.no/John_Horton_Conway))

![Game of life](./img/Gospers_glider_gun.gif)

Spillet går ut på at det er et eneste stort rutenett. Rutene kan være enten opplyste (levende) eller tomme (døde).

Spillet er bygget på følgende regler:

* Hvis en levende rute berører en eller ingen andre levende ruter, dør den
* Hvis en eller flere døde ruter blir omringet av levende ruter, blir de omringede rutene levende
* Hvis en rute er i kontakt med flere enn tre ruter, dør ruta.

**Oppgave:** Lag Game of Life.

## Ressurser

* Du trenger en kodeeditor og Python til denne oppgaven.


---

_Denne oppgaven er laget av [fuzzbin](https://github.com/fuzzbin) og [bitjungle](https://github.com/bitjungle). Oppgaven er lisensiert under en [Creative Commons Navngivelse-DelPåSammeVilkår 4.0 Internasjonal lisens.](http://creativecommons.org/licenses/by-sa/4.0/)_
