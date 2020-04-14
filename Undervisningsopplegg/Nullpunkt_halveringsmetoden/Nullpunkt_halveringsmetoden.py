def f(x):
    '''Funksjonen som er gitt i oppgaven.'''
    return (1/4)*x**3 - (3/4)*x**2 - x + 2

a = -1 # startpunkt på venstre side av nullpunktet
b = 3  # startpunkt på høyre side av nullpunktet
TOL = 1E-9 # toleranse: hvor nærme svaret skal vi komme før vi er fornøyde?

while abs(a - b) > TOL: # så lenge avstanden mellom a og b stor
    n = (a + b)/2       # velg n midt mellom a og b
    print('Nå er x=', n)
    if f(a)*f(n) > 0:   # hvis produktet er større enn null
        a = n             # sett a til n-verdien
    else:               # ellers
        b = n             # sett b til n-verdien
                        # gjenta 

print("Løsningen er x=", n)
