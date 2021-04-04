# API - Programmeringsgrensesnitt
__Creative Commons BY-SA : bitjungle (Rune Mathisen) og fuzzbin (Tom Jarle Christiansen)__

<hr/>

**For å få tilgang til data brukes et programmeringsgrensesnitt. Den vanligste forkortelsen for dette er API som betyr Aplication programming interface. Typiske bruksområder for et API er for å gi brukere og utviklere tilgang til spesifikke data i en organisasjon eller applikasjon.**

Det finnes veldig mange typer data som kan hentes ut ved hjelp av et API. Dataene kommer på litt ulike formater. De vanligste er JSON, CSV og XML. Dette er ulike måter å organisere data på. Python har god støtte for å jobbe med de fleste ulike dataformater.

Følgende eksempel henter data om den internasjonale romstasjonen (ISS) fra tjenesten [opennotify.org](http://open-notify.org/) på dataformatet JSON ved hjelp av pythonbiblioteket requests.


import requests
from pprint import pprint #Prettyprint for penere utskrift av JSON

url = "http://api.open-notify.org/iss-now.json"
r = requests.get(url).json()

pprint(r)

Utskriften viser rådata på JSON-format som i praksis er det vi kjenner som datatypen dictionary i Python. Vi kan når data ved å bruke notasjonen som vist i eksempelet under. Legg merke til at _lengde-_ og _breddegrad_ ligger på nivået under _iss_position_.

print("Tidsmerke:", r["timestamp"]) # Antall milisekunder siden 1.1.1970
print("Lengdegrad:", float(r["iss_position"]["longitude"]))
print("Breddegrad:", float(r["iss_position"]["latitude"]))

Biblioteket [requests](https://requests.readthedocs.io/en/master/) har veldig mange mulgiheter. Det anbefales å lese litt på dokumentasjonen og prøve noen av mulighetene.

## Endepunkter

En vanlig måte å få tilgang til data ved hjelp av et API på er å bruke det som kalles endepunkter. Et endepunkt er en URL der man kan endre parameter for å få ønskede data.


payload = {'results': 10} # API-parameter. Returner 10 resultat

url = 'https://randomuser.me/api/' # Endepunkt med parameter
r = requests.get(url, params=payload).json()

# pprint(r['results'][0]['name'])

for person in r['results']:
    pprint(person['name'])


