#!/usr/bin/env python
# coding: utf-8

# # Rekursiv programmering
# 
# __Creative Commons BY-SA : bitjungle (Rune Mathisen) og fuzzbin (Tom Jarle Christiansen)__
# 
# <hr/>
# <img alt="Opphavsmann: Mestigoit Lisens: Creative Commons BY-SA 3.0 Unported" title="Opphavsmann: Stefan Walkowski Lisens: Creative Commons BY-SA 4.0 Unported" style="width: 200px; float: right; margin-left: 30px;" src="img/Simple_Fractals.png">
# 
# 
# Bilde av <a href="//commons.wikimedia.org/w/index.php?title=User:Saisundar.s&amp;action=edit&amp;redlink=1" class="new" title="User:Saisundar.s (page does not exist)">Saisundar.s</a> - <span class="int-own-work" lang="en">Own work</span>, <a href="https://creativecommons.org/licenses/by-sa/4.0" title="Creative Commons Attribution-Share Alike 4.0">CC BY-SA 4.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=73877448">Link</a>
# 
# **[Rekursjon](https://no.wikipedia.org/wiki/Rekursjon), eller rekursiv funksjon, er i matematikk og informatikk en måte å definere en funksjon på, der funksjonen selv blir anvendt i sin egen definisjon.**
# 
# I programmering og matematikk brukes rekursjon når man skal bygge videre på resultater som er beregnet på samme måte. Dette kan være en tallfølge der hvert nye ledd beregnes med utgangspunkt i det forrige. Dette kan for eksempel være en [aritmetiske tallfølge](https://ndla.no/nb/node/115341?fag=98361):
# 
# $$a_n = a_{n-1} + d$$
# 
# Her vil hvert ledd være lik det forrige pluss en differanse $d$
# 
# La oss si at $a_n=1$ og $d=7$. Vi kan nå beregne neste ledd $a_{n+1} = a_n + d = 1 + 7 = 8$
# 
# Skal vi gjøre dette for hånd kreves det mange regneoperasjoner. (Eller ved bruk av [eksplisitt formel](https://ndla.no/nb/node/115335?fag=98361)). En datamaskin kan fint regne rekursivt.
# 
# ### Eksempel på rekursiv formel
# 
# Vi lar $a_1 = 1$ og $d = 3$, Vi skal nå regne ut $a_{87}$.

# In[1]:


def rekursiv(n, d):
    if n == 1:
        return 1
    else:
        return rekursiv(n-1, d) + d

print(rekursiv(87,3))


# ### Eksempel på beregning av fakultet

# In[2]:


def fakultet(n):
    if n == 1:
        return 1
    else:
        return n * fakultet(n - 1)


# In[3]:


print(fakultet(5))


# ### Eksempel på beregning av Fibonaccitall

# In[4]:


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# In[5]:


print(fibonacci(8))


# In[ ]:




