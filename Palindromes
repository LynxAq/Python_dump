def Algorytm_E(start,limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True
    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i] == True]


def palindromy(a,b):
    lista_liczb = Algorytm_E(a,b)
    lista_palindronow = []
    for e in lista_liczb:
        e = str(e)
        if len(e) < 2:
            pass
        else:
            if e == e[::-1]:
                lista_palindronow.append(e)
            else:
                pass
    return lista_palindronow





