import random

from math import exp

from hill_climbing import permutations, conflits, transposition, cbdisplay

def recuit_simule(n,T_limite):
    #n: taille de la permutation
    #T_limite: limite de temps (correspond ici au nombre maximal d'itérations)
    if n<=3:
        return False
    Lambda = 1.380649*10**-23 #constante de Boltzman
    t=1
    L = permutations(n)
    while t<T_limite:
        if conflits(L)==0:
            return L,conflits(L),t,cbdisplay(n,L)
        a=random.randint(0,n-1)
        b=random.randint(0,n-1)
        L2 = transposition(L,a,b)
        delta = conflits(L2)-conflits(L)
        if delta<0:
            L=L2
        else:
            r = random.random()
            if r<exp(-Lambda*t):
                L=L2
        t=t+1
    return L, conflits(L), t, cbdisplay(n,L)

        

