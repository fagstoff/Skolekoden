#!/usr/bin/env python
# coding: utf-8

# # Spredningsplott
# 
# __Creative Commons BY-SA : bitjungle (Rune Mathisen) og fuzzbin (Tom Jarle Christiansen)__
# 
# <hr/>
# <img alt="Sammenheng mellom utdanning og inntekt, fra en undersøkelse i Canada i 1971. CC BY Ista Zahn" style="float: right; margin-left: 10px;" src="img/scatterplot_of_education_and_income.png">
# 
# **Et spredningsplott er en type diagram hvor vi viser verdiene til to ulike variabler i et datasett. Hensikten med å lage en slik type plott kan for eksempel være å avdekke samvariasjon mellom variablene.**
# 
# > Denne siden dekker helt eller delvis kompetansemålene: [Grunnleggende programmering 3](https://github.com/fagstoff/ProgMod/blob/master/L%C3%A6replan/kompetansem%C3%A5l.md#grunnleggende-programmering)
# 
# Mer om spredningsplott her...
# 
# En tredje variabel kan vises som fargekode eller størrelse på punktene. Ta med?
# 
# Bruker [pandas](http://pandas.pydata.org/) for å lage (og lagre) datastrukturer.
# Bruker [seaborn](http://seaborn.pydata.org/) til plotting.
# 
# 

# In[1]:


import pandas as pd
import seaborn as sb

df = pd.DataFrame({'Høyde': 
                   [173, 178, 153, 175, 167, 155, 161, 164, 177, 157, 162, 165, 172, 165, 170, 167, 185, 170, 178, 185, 175, 183, 182],
                   'Skonummer': 
                   [42, 45, 37, 39, 40, 37, 39, 38, 40, 36, 38, 38, 40, 39, 39, 39, 42, 40, 43, 43, 43, 45, 43]})


# In[13]:


df.plot.scatter(x='Høyde', y='Skonummer')


# In[14]:


sb.lmplot(x='Høyde',y='Skonummer',data=df,fit_reg=True) 


# In[ ]:




