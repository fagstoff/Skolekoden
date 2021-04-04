#!/usr/bin/env python
# coding: utf-8

# # Populasjonsmodeller
# 
# 
# __Creative Commons BY-SA : bitjungle (Rune Mathisen) og fuzzbin (Tom Jarle Christiansen)__
# 
# <hr />
# 
# <img alt="Fox Study 6. CC BY Peter Trimming" style="float: right; margin-left: 10px;" src="img/Fox_study_6.jpg">
# 
# **[Populasjonsmodeller](https://en.wikipedia.org/wiki/Population_model) er mye brukt for å kunne forutsi eller simulere hvordan en eller flere [populasjoner](https://no.wikipedia.org/wiki/Populasjon) vil utvikle seg over tid. Populasjonens utvikling vil være avhengig av mange faktorer.**
# 
# På dette temaarket skal vi se på hva som skjer hvis kaniner kan reprodusere seg på et avgrenset område. Vi skal bruke en forenkling av en kjent modell som kalles: [Lotka-Volterra Predator-Prey System](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations). Dette er ganske enkle diferensiallikninger som beskriver dhvordan rovdyr og byttedyr vil påvirke hverandre i et område.
# 
# La oss først se på en modell som beskriver hvordan endringen ($H'(t)$) i harebestanden ($H(t)$) som funksjon av tiden kan uttrykkes.
# 
# $$H'(t) = k \cdot H(t)$$, der $k$ er reproduksjonsraten og $H(t)$ er harebestanden på en gitt tid $t$.

# In[1]:


""" Rovdyr - Lotka/Volterra - rovdyr vs byttedyr """
#
# Lisens: Creative Commons BY-SA fuzzbin (Tom Jarle Christiansen) og bitjungle (Rune Mathisen) 2019
#
# Program simulerer hvordan populasjonen av rovdyr/byttedyr påvirkes over tid

import matplotlib.pyplot as plt

# Definerer initialbetingelser
H_0 = 1000 # Harebestanden ved t = 0;
t_0 = 0 # Starttiden i antall måneder
dt = 1 # Skrittlengden
k = 0.1 # Reproduksjonsraten

# Initiering av lister
t = [t_0] 
H = [H_0]

# Modellen
def H_endring():
    return k * H[-1]

# Euler
def neste_H():
    return H[-1] + H_endring() * dt

# Fyller lister med beregninger
for i in range(0,100):
    t.append(t[-1] + dt)
    H.append(neste_H())

plt.plot(t,H)
plt.grid()
plt.show()


# La oss modifisere modellen slik at vi tenker oss at.....

# In[2]:


b = 20000 # Bærekraft

# Initiering av lister
t = [t_0] 
H = [H_0]

# Modellen
def H_endring():
    return k * H[-1] * (1 - H[-1] / b)

# Euler
def neste_H():
    return H[-1] + H_endring() * dt

# Fyller lister med beregninger
for i in range(0,100):
    t.append(t[-1] + dt)
    H.append(neste_H())

plt.plot(t,H)
plt.grid()
plt.show()


# # Oppgaver
# Søk på nettet, og forsøk å finne en populasjonsmodell som du synes er interessant. Implementer modellen i Python, bruk eksemplet ovenfor som mal.
