# Derivasjon
__Creative Commons BY-SA : fuzzbin (Tom Jarle Christiansen) og bitjungle (Rune Mathisen)__

<hr/>

__[Derivasjon](https://snl.no/derivasjon_-_matematikk) er en operasjon på en funksjon som forteller om hvordan funksjonen endrer seg, altså hvordan funksjonsverdien stiger eller synker. Det å utføre en derivasjon kalles å derivere funksjonen.__

For en funksjon f(x) er den deriverte funksjonen [ekvivalent](https://no.wiktionary.org/wiki/ekvivalent) med følgende begreper:

1. Den momentane vekstraten til funksjonen f(x)
2. Stigningstallet til tangenten til funksjonen f(x) i punktet x

## Definisjon av den deriverte - Newtons kvotient

Vi vet at vi kan finne gjennomsnitlig vekstfart ved å se på endringen i funksjonsverdi i et gitt intervall.

$$\bar{a}=\frac{y_2-y_1}{x_2-x_1}$$

Hvis vil velger å se på mindre og mindre intervaller (grenseverdien $h=x_2-x_1$ går mot $0$), har vi:

$$f'(x)=\lim_{h \to 0}\frac{f(x + h)-f(x)}{h}$$

### Eksempel

Vi begynner med å definere den deriverte med programkode:

def derivert(f, x, h):
    return (f(x+h) - f(x)) / h

Så definerer vi funksjonen $f(x) = x^2 + 2x -3$

def f(x):
    return x**2 + 2 * x - 3

Vi vet fra klassisk matematikk at $f'(x) = 2x+2$ når $f(x)=x^2+2x-3$.

Setter vi inn en verdi for x i den deriverte, for eksempel 5, har vi $f'(5) = 2\cdot5+2=12$ som da er den deriverte av $f(x)$ i punktet $x=12$

Ved å bruk de definerte funksjonene i python har vi:

print(derivert(f, 5, 0.1))

## En forbedret utgave - Newtons symmetriske kvotient
La oss se om vi kan forbedre definisjonen ved å se på et symmetrisk område rundt x. Vi modifiserer uttrykket for den deriverte slik:

$$f'(x)=\lim_{h \to 0}\frac{f(x + h)-f(x - h)}{2h}$$

Vi lar nå grenseverdien nærme seg symmetrisk fra begge sider.

def derivert_2h(f, x, h):
    return (f(x+h) - f(x-h)) / (2*h)

print(derivert_2h(f, 5, 0.1))

## Oppgaver

1. Studer koden i eksemplene over. 
    * Hva er $h$ i eksemplene over?
    * Hva skjer når du endrer på $h$?
    * Deriver funksjonen $f(x)=x^2+2x-3$ i GeoGebra og sammenlign med resultatene i eksemplene. Hva ser du?
2. Bruk numerisk derivasjon for å lage en graf for $f'(x)$ når x$\epsilon[0,10]$ for $f(x)=x^3-2x^2-x+5$
3. Bygg videre på oppgave 2, og lag et program som vurderer hvor godt estimatet treffer for $f'(5)$ når du bruker verdier for $h$ fra $1\cdot 10^{-1}$ til $1\cdot 10^{-20}$.
4. Bruk numerisk derivasjon for å lage en graf for $f(x)$ og $f^\prime(x)$ for $f(x) = sin(x)$ når x$\epsilon[0,2\pi]$
5. Fra fysikken vet vi at: $a(t)=v'(t)=s''(t)$. Bruk numerisk derivasjon for å lage en graf for strekning, fart og akselerasjon når du vet at $s(t)=-0.01t^3+0.3t^2+8t$ når $t\in[0,10]$
6. Når vi skal derivere produktet av to funksjoner, kan vi bruke regelen:

$$(u(x) \cdot v(x))' = u'(x) \cdot v(x) + u(x) \cdot v'(x)$$

Gitt de to funksjonene:

$$u(x) = sin(\frac{1}{x^2}) \quad v(x) = \sqrt{ln(x)} \quad x\in \langle 1,5]$$

Lag et Python-program som regner ut høyre og venstre side i produktregelen for derivasjon, og sammenlikn svarene. 