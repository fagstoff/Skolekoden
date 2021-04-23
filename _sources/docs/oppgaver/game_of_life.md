# Conway's Game of Life

## Oppgave

Conway er kjent som oppfinner av spillet Game of Life (eller kort Life), som var en videreutvikling og forenkling av ideer fra John von Neumann. Spillet ble først publisert i 1970 i Scientific American innenfor Martin Gardners rubrik Mathematical Games. Spillet har det teoretiske potentiale av en Turing maskin, det vil si alt som kan beregnes algoritmisk kan også beregnes innenfor Game of Life. På grunn av Lifes analogier med vekst, nedgang og forandring tilhører den den økende klassen av såkalte simulation games. Spillet har fått avgjørende betydning for utviklingen av såkalte cellulære automater. (Fra [SNL](https://snl.no/John_Horton_Conway))

![Game of life](./img/Gospers_glider_gun.gif)

Spillet går ut på at det er et eneste stort rutenett. Rutene kan være enten opplyste (levende) eller tomme (døde). Alle celler spillet har ni naboceller.

![Naboer](./img/naboer.png)

Spillet er bygget på følgende regler:

    1. En levende celle med færre en to levende naboer dør av ensomhet.
    2. En levende celle med to eller tre levende naboer overlever til neste generasjon.
    3. En levende celle med fler enn tre naboer dør på grunn av overbefolkning.
    4. En død celle med nøyaktig tre naboer blir levende som ved reproduksjon.


**Oppgave:** Lag Game of Life!

## Ressurser

* Du trenger en kodeeditor og Python til denne oppgaven.


---

_Denne oppgaven er laget av [fuzzbin](https://github.com/fuzzbin) og [bitjungle](https://github.com/bitjungle). Oppgaven er lisensiert under en [Creative Commons Navngivelse-DelPåSammeVilkår 4.0 Internasjonal lisens.](http://creativecommons.org/licenses/by-sa/4.0/)_
