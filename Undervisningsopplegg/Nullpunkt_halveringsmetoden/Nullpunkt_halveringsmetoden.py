def halvering(f, a, b):
    '''Finner nullpunkt med halveringsmetoden, gitt en funksjon f.
    Nullpunktet må ligge mellom startverdiene a og b.'''
    while abs(a - b) > 1E-9: # så lenge avstanden mellom a og b er over en viss størrelse
        x = (a + b)/2        # velg x midt mellom a og b
        print(x)
        if f(a)*f(x) > 0:    # hvis produktet er større enn null
            a = x            # sett a til x-verdien
        else:                # ellers
            b = x            # sett b til x-verdien
                             # gjenta 
    return x

def f(x):
    '''Funksjonen som er gitt i oppgaven.'''
    return (1/4)*x**3 - (3/4)*x**2 - x + 2

a = -1 # startpunkt på venstre side av nullpunktet
b = 3  # startpunkt på høyre side av nullpunktet
nullpunkt = halvering(f, a, b)
print("Løsning er x=", nullpunkt)
