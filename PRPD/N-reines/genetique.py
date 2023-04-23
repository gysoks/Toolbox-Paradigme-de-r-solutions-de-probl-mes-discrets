import random

from hill_climbing import permutations, transposition, conflits, cbdisplay

def genetique(N,n,mu,Nb_pas):
    # N: nombre d'individus de la population
    # n: taille de la permutation d'un individus
    # mu: probabilité comprise entre 0,01 et 0,1
    # Nb_pas: nombre d'itérations
    Population=[permutations(n) for i in range(N)]
    Npas=0
    while Npas<Nb_pas:
        selection=paires(int(N/2),Population)
        print('selection', selection)
        croisement(selection,int(n/2))
        print('croisement', croisement)
        for z in selection:
            r=random.random()
            if r<mu:
                mutation(z[0])
                mutation(z[1])
        Population=forme_liste(selection)+Population[int(n/2)+1:]
        Npas=Npas+1
    best_indiv=meilleur(Population)
    print(best_indiv)
    return Population, Npas, best_indiv, conflits(best_indiv), cbdisplay(n,best_indiv) 
    
def forme_liste(L):
    """Transforme une liste de dimension 2 en liste de dimension 1"""
    Lbis=[]
    n1=len(L)
    n2=len(L[0])
    for i in range(n1):
        for j in range(n2):
            Lbis.append(L[i][j])
    return Lbis

def paires(m,L):
    """Constitution en paires des m éléments de L"""
    L2=[]
    for i in range(0,m,2):
        L2.append([L[i],L[i+1]])
    return L2

def croisement(population,k):
    """On croise la poluation en choisissant comme point de croisement la
    position k d'un élement de la liste population"""
    for x in population:
        x[0]=x[0][0:k]+transposition_2(x[0][k+1:])
        x[1]=x[1][0:k]+transposition_2(x[1][k+1:])

def transposition_2(L):
    """Renvoie une permutation des éléments de L"""
    n=len(L)
    L2=[0 for i in range(n)]
    for j in range(n):
        L2[j]=random.choice(L)
        L.remove(L2[j])
    return L2

def mutation(x):
    n=len(x)
    L=permutations(n)
    """On choisit maintenant deux indices aléatoires entre 0 et n"""
    k=random.choice(L)
    L.remove(k)
    m=random.choice(L)
    """On effectue maintenant la mutation"""
    x=transposition(x,k,m)
    
def meilleur(Population):
    """Renvoie le meilleur individus de la population, c'est à dire ici 
    la permutation avec le moins de conflits"""
    min_conf=conflits(Population[0])
    meilleur_indiv=Population[0]
    for x in Population[1:]:
        if conflits(x)<min_conf:
            min_conf= conflits(x)
            meilleur_indiv=x
    return meilleur_indiv
    
    
