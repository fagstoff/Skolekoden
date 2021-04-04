# Tegne grafer
__Creative Commons BY-SA : bitjungle (Rune Mathisen) og fuzzbin (Tom Jarle Christiansen)__

<hr/>

**Ofte ønskeler vi å representere matematiske modeller og funskjoner grafisk. I Python kan dette gjøres på flere måter. En veldig vanlig måte å gjøre dette på er å benytte seg av biblioteket [matplotlib](http://matplotlib.org/).**

Prinsippet bak plotting i Python ligner veldig på metoden som brukes når man skal lage en grafisk fremstilling manuelt ved hjelp av en tabell. Før vi kan lage en graf, må dataene organisereres i lister. Vi skal se nærmere på $y=x^2$.

|x|0|1|2|3|4|5|
|-|-|-|-|-|-|-|
|y|0|1|4|9|16|25|

Hvert tallpar representerer ett punkt (x,y) i grafen. Det er derfor viktig at listene er like lange. Vi lager to lister med verdier som skal plottes:

x_verdier = [0, 1, 2, 3, 4, 5]
y_verdier = [0, 1, 4, 9, 16, 25]


Det kan bli veldig arbeidskrevende og tungvindt å taste inn mange x- og y-verdier på denne måten. En enklere måte å gjøre det på, er å bruke det som kalles [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions). Da skriver vi slik:

x_verdier = [i for i in range(6)]
y_verdier = [j**2 for j in x_verdier]

print(x_verdier)
print(y_verdier)

Det er enda et alternativ til å lage x- og y-verdier til grafen, og det er ved å bruke biblioteket [numpy](https://numpy.org/). Da kan det gjøres slik: 

import numpy

def f(x):
    return x**2

x_verdier = numpy.linspace(0, 5, 6) # start, slutt, antall verdier
y_verdier = f(x_verdier)

Vi kan nå bruke biblioteket matplotlib i sin aller enkleste form til å skrive ut punktene vi har lagret i de to listene. Det gjør vi slik:

import matplotlib.pyplot as plt 
plt.plot(x_verdier, y_verdier)
plt.show()

Matplotlib er veldig fleksibelt, og det finnes mange kommandoer og argumenter som gjør at vi kan tilpasse plottet. I eksempelet under er det lagt inn noen fler kommandoer og argumenter. Argumentet `bx` markerer punktene som blå kryss, og med grid-kommandoen kan vi lage et rutenett som bakgrunn.

plt.plot(x_verdier,y_verdier,'bx')
plt.title('Enkelt plott')
plt.grid(color='r', linestyle='-', linewidth=0.5)
plt.xlabel('x-verdier')
plt.ylabel('y-verdier')
plt.show()

## Oppgaver

1. Lag en linær graf med stigningstall 2 og merk aksene.
2. Tegn funksjonen $f(x)=-x^2+10x$ når $ x\epsilon[0,10]$ i et koordinatsystem.
3. Pynt oppgave 2 så fint du kan. Du kan finne inspirasjon i [eksempelgalleriet](https://matplotlib.org/gallery/index.html) til [Matplotlib](http://matplotlib.org/).
4. Plott funksjonen $g(x)=2x-5$ i samme koordinatsystem.

