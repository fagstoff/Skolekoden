# Moduler, pakker og biblioteker
__Creative Commons BY-SA : bitjungle (Rune Mathisen) og fuzzbin (Tom Jarle Christiansen)__

<hr>

**En av fordelene med å bruke Python i programvareprosjekter, er det store økosystemet av moduler som enkelt kan importeres og tas i bruk. Her skal vi se litt på hvordan du tar i bruk moduler, og du får noen tips til moduler som kan være nyttige for faget Programmering og modellering.**

I Python er en **modul** en samling av funksjoner og klasser som kan gjenbrukes i mange ulike programmer. Et eksempel på en slikt modul er [math](https://docs.python.org/3/library/math.html), som er en samling av matematiske funksjoner. Her finner du for eksempel trigonometriske funksjoner (sin, cos, tan, og så videre) og konstanter (for eksempel $\pi$) som du kan bruke i programmene dine. Når du skal lage et program vil det spare deg for mye tid om du finner og bruker moduler som andre har laget allerede.

En **pakke** i Python er en samling av moduler. Mange pakker kan igjen samles i **biblioteker**. Det biblioteket du bør gjøre deg kjent med aller først, er det såkalte [Python Standard Library](https://docs.python.org/3/library/index.html). Standardbiblioteket er tilgjengelig for deg uten at du trenger å installere ekstra utover en "vanlig" Python-installasjon.

Om du ikke finner det du trenger i [standardbiblioteket](https://docs.python.org/3/library/index.html) til Python, bør du lete gjennom [The Python Package Index (PyPI)](https://pypi.python.org/pypi). Sjansene er store for at noen har laget akkurat det du trenger allerede, sånn at du ikke må lage alt helt fra bunn av.

Nå skal vi gjennomgå noen få (men sentrale) funksjoner og moduler fra [standardbiblioteket](https://docs.python.org/3/library/index.html), men det er viktig at du selv sørger for å gjøre deg kjent med hva du finner der. Vi skal også se på noen biblioteker fra [PyPI](https://pypi.python.org/pypi) som er nyttige i faget Programmering og modellering.


## Funksjoner og moduler i standardbiblioteket

Python har en del [innebygde funksjoner](https://docs.python.org/3/library/functions.html), og du trenger en eller flere av disse i alle programmer. her er noen eksempler. Forsøk gjerne å gjøre endringer i eksemplene, og se hva som skjer.


Vi skal først se på funksjonen [format()](https://www.python.org/dev/peps/pep-3101/#format-strings), som er den foretrukne måten å sette data inn i tekststrenger på. Her er noen eksempler.

heltall = 7
desimaltall = 9.81
navn = "fuzzbin"
print('Hei {}, her er heltallet {} og desimaltallet {}'.format(navn, heltall, desimaltall))

Vi bruker range() for å generere en sekvens av tall som vi kan loope gjennom.


for num in range(5):
    print('Nå er jeg på tallet {}'.format(num))

For å runde av et desimaltall kan vi bruke round().

a = 2.3
b = -2.6
print('a ≈ {} og b ≈ {}'.format(round(a), round(b)))

I tillegg til de innebygde funksjonene, vil du helt garantert få bruk for modulen [math](https://docs.python.org/3/library/math.html), som er en del av [standardbiblioteket](https://docs.python.org/3/library/index.html) i Python. Her er noen få eksempler på funksjonene i math:

import math

x = -4.67

x_abs = math.fabs(x)
print('Absoluttverdien av {} er {}'.format(x, x_abs))

x_exp = math.exp(x)
print('e^{} er {}'.format(x, x_exp))

x_cube = math.pow(x, 3)
print('{}^3 er {}'.format(x, x_cube))

x_abs_sqroot = math.sqrt(x_abs)
print('kvadratrot av |{}| er {}'.format(x, x_abs_sqroot))


### Kommandoen help()
For å få dokumentasjon på funksjonene som er tilgjengelige i et bibliotek, kan vi bruke funksjonen `help()`. 

Prøv for eksempel å skrive kommandoen ```help(math)```

En annen nyttig modul i [standardbiblioteket](https://docs.python.org/3/library/index.html) er [random](https://docs.python.org/3/library/random.html). Her er et eksempel hvor vi genererer et tilfeldig tall:

import random

tilfeldig = random.random()
print('Helt tilfeldig valgte jeg tallet {}'.format(tilfeldig))

## Nyttige biblioteker fra PyPI

Biblioteket [numpy](https://docs.scipy.org/doc/numpy/reference/index.html) inneholder mange funksjoner for behandling av [vektorer](https://en.wikipedia.org/wiki/Vector_space) og [matriser](https://en.wikipedia.org/wiki/Matrix_(mathematics). Du kan også bruke funksjoner i numpy for å generere lister, slik som i dette eksemplet hvor vi genererer 10 tall mellom 0 og 4.:


import numpy as np

minliste = np.linspace(0, 4, num=10)
print(minliste)

Nå kan vi for eksempel regne ut sinus til alle verdiene i lista vi genrerte

mineverdier = np.sin(minliste)
print(mineverdier)

Vi vil ofte ha behov for å visualisere data. Da er biblioteket [Matplotlib](http://matplotlib.org/) kjekt å bruke. Her skal vi bruke modulen [pyplot](https://matplotlib.org/users/pyplot_tutorial.html) (som er en del av biblioteket Matplotlib) for å tegne en graf av tallene vi genererte ovenfor.

import matplotlib.pyplot as plt
plt.plot(minliste, mineverdier)
plt.show()

Med biblioteket [SymPy](http://www.sympy.org) kan du gjøre symbolske utregninger. Her er noen eksempler:

import sympy

print("Finne eksakt svar: sqr(8) = ", sympy.sqrt(8))

x, y = sympy.symbols('x y')
expr_1 = x**2 + 2*x*y 
print("Faktorisere: x^2 + 2xy = ", sympy.factor(expr_1))

print("Løse likninger: x^2 + 2xy = 0 => ", sympy.solve(sympy.Eq(expr_1, 0), x))

expr_2 = x**2 + 2*x - 3
print("Derivere: d/dx (x^2 + 2*x - 3) = ", sympy.diff(expr_2, x))

# Integrere
expr_3 = 2*x + 2
# - ubestemt 
print("Ubestemt integral: int(2x + 2) = ", sympy.integrate(expr_3, x))
# - bestemt 
print("Bestemt integral: int(2x + 2) x:[0, 2] = ", sympy.integrate(expr_3, (x, 0, 2)))


## Oppgaver
1. Bruk modulen random, og lag et program som simulerer [Lotto](https://no.wikipedia.org/wiki/Lotto_(Norge&#41;). Du skal trekke 7 tilfeldige heltall mellom 1 og 34, uten tilbakelegging.
2. Lag et program der brukeren kan taste inn a, b og c i funksjonen: $ f(x)=ax^2+bx+c $. Programmet skal så skrive ut nullpunktene til funksjonen. Hint: Disse kan finnes ved hjelp av formelen: $$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$
3. Lag et program der brukeren kan taste inn a, b og c i funksjonen: $ f(x)=ax^2+bx+c $. Programmet skal så plotte funksjonsverdiene for $ x \epsilon [0,10] $ se også: [Plotting i python](https://github.com/fagstoff/ProgMod/blob/a8e819bc251175ce6cf81122326d24c20a8ee3b4/Fagstoff/enkel-graf.ipynb)
4. Ekstrautfordring: Lag et program der brukeren kan taste inn amplitude og frekvens. Programmet skal så tegne den tilsvarende sinusfunksjonen for to hele perioder. Det skal være navn og verdi på aksene og rutenett som bakgrunn på plottet.


