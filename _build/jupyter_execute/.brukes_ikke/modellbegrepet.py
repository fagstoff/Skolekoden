#!/usr/bin/env python
# coding: utf-8

# # Introduksjon til modellbegrepet
# __Creative Commons BY-SA : bitjungle (Rune Mathisen) og fuzzbin (Tom Jarle Christiansen)__
# 
# <hr/>
# <img alt="Tavle. Lisens: CC0" style="float: right; margin-left: 10px;" src="img/maxpixel.freegreatpicture.com-Mathematics-Physics-Mathematical-School-Formula-1509559.jpg">
# 
# **Hva menes egentlig med en "matematisk modell", og hva er hensikten med dem? Det skal vi se nærmere på her.**
# 
# > Denne siden dekker helt eller delvis kompetansemålene: [Modellering 1 og 2](https://github.com/fagstoff/ProgMod/blob/master/L%C3%A6replan/kompetansem%C3%A5l.md#modellering)
# 
# Når vi bruker datamaskiner som hjelpemiddel for å forstå og påvirke omgivelsene våre, må vi kunne beskrive disse omgivelesene med matematikk. I tradisjonelle realfag som fysikk, kjemi og biologi bruker vi ofte denne teknikken. Vi kan for eksempel lage en matematisk funksjon som har en eller flere fysiske målinger som variabler, og som regner ut noe vi ønsker å vite mere om. I andre tilfeller hvor det er vanskelig å lage en matematisk funksjon, kan vi gi datamaskinen massevis av data og la den selv finne en passende funksjon.
# 
# ## En kjent modell
# En kjent matematisk modell som er med på å beskrive omgivelsene våre på en veldig god måte, er Newtons 2. lov. Den sier at dersom vi har et legeme med konstant masse $m$ og akselerasjon $\vec{a}$, så er summen av kreftene $\Sigma \vec{F}$ på legemet gitt ved:
# 
# $$\Sigma \vec{F} = m\vec{a}$$
# 
# Om du faller [fritt](https://snl.no/fritt_fall) mot jorda, er din akselerasjonen tilnærmet lik $g = 9.81 \mathrm{m/s^2}$, og det er *kun* tyngdekraften som virker på deg.
# 
# La oss nå si at du ikke faller, men isteden står trygt med beina på gulvet slik at $\Sigma \vec{F} = 0$. Da kan vi regne ut kraften som virker mellom deg og gulvet på følgende måte:

# In[1]:


g = 9.81 # m/s^2
m = 80 # kg
F = m*g
print("F = {} N".format(round(F, 0)))


# Men hvor høyt er trykket mellom fotsålen og gulvet? Det kan vi også regne ut, fordi vi vet at trykket $P$ er gitt ved en annen modell:
# 
# $$P = \frac{F}{A}$$
# 
# hvor $A$ er arealet. La oss anta at det samlede arealet av skosålene dine er $500 \mathrm{cm^2}$ (forsøk gjerne å finne et bedre estimat selv). Da blir trykket:

# In[2]:


A = 500 / (100*100) # m^2
P = F / A # Pa (trykkenheten Pascal)
print("P = {} Pa".format(round(P, 0)))


# ## Oppgaver
# 1. Lag et program som beregner hastigheten en stuper vil treffer vannflata med. Modellene du trenger for å løse oppgaven, [finner du her](https://ndla.no/nb/node/119499?fag=98361).
# 2. Lag et program som regner ut radiusen til en kule når man får oppgitt volumet. Formel for volumet av en kule [finner du her](https://ndla.no/nb/node/151003?fag=55).
# 3. Lag et program som kan regne ut en [binomisk sannsynlighetsmodell](https://ndla.no/nb/node/103796?fag=57934).

# In[ ]:




