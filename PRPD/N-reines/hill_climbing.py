import random

import numpy as np

import matplotlib.pyplot as plt

import math

def echiquier(L):
    """Transformation de la permutation en tableau (échiquier)""" 
    n=len(L)
    T=[[0 for i in range(n)]for j in range (n)]
    for i in range(n):
        T[i][L[i]]=1
    return T

def conflits(L):
    """Renvoie le nombre de conflits entre les reines de l'echiquier"""
    # L: liste des reines déjà sur l'échiquier
    # On teste seulement les diagonales, la permutaion permettant d'éviter les conflits sur les lignes et les colonnes
    conf=0
    for i in range (0,len(L)-1):
        for j in range(i+1,len(L)):
            if abs(L[i]-L[j])==abs(i-j):
                conf=conf+1
    return conf

def permutations(n):
    """Renvoie une permutaions de N-reines, sous forme de liste de taille  n 
    où i représente la ligne et L[i] la colonne de l'échiquier"""
    L=[]
    while len(L)<n:
       Nouv=random.randint(0,n-1) #Colonne de la nouvelle reine
       if (Nouv in L)==False:
           L.append(Nouv)
    return L

def transposition(L,i,j):
    """Renvoie la liste L en permutant L[i] et L[j]"""
    c=L[i]
    L[i]=L[j]
    L[j]=c
    return L

def meilleur_voisin(L):
    """Renvoie le meilleur voisin de L (un voisin étant une transposition)
        Pour ce faire, on tire au hasard un indice a et on regarde pour 
        quel indice j la transposition(L,a,j) est la plus optimale, c'est 
        à dire qu'elle comporte le moins de conflits."""
    n=len(L)
    a=random.randint(0,len(L)-1)
    min_conf=math.inf
    ind_min_conf=-1
    for j in range(n):
        if conflits(transposition(L,a,j))<min_conf:
            min_conf=conflits(transposition(L,a,j))
            ind_min_conf=j
    if ind_min_conf!=-1: #On a trouvé une transposition favorable (transposition avec moins de conflits que le nombre de conflits de L)
        return transposition(L,a,ind_min_conf)
    return L # On a pas trouvé de meilleure transposition

def hill_climbing(n,Nb_essais):
    if n<=3:
        return False
    ind=1
    L=permutations(n)
    while ind<Nb_essais:
    # Cette méthode nous permet de trouver un minimum local mais pas 
    # nécessairement global: il faut une condtition d'arrêt comme un nombre 
    # d'essais maximal,inférieur au nombre total de permutations possibles
        if conflits(L)==0:
            return L, cbdisplay(n,L), conflits(L),ind,
        else:
            ind=ind+1
            L=meilleur_voisin(L)
    return L, cbdisplay(n,L), conflits(L), ind

def hill_climbing_bis(n,Nb_essais):
    """ Cet algorithme prend en compte les transpositions précédentes
        en gardant en mémoire les indices correspondant aux transpositions
        déjà effectuées. """
    if n<=3:
        return False
    ind=1
    L_ind_perm=[] #Liste des indices de permutations
    L=permutations(n)
    while ind<Nb_essais:
    # Cette méthode nous permet de trouver un minimum local mais pas 
    # nécessairement global: il faut une condtition d'arrêt comme un nombre 
    # d'essais maximal,inférieur au nombre total de permutations possibles
        if conflits(L)==0:
            return L, cbdisplay(n,L), conflits(L),ind,
        else:
            ind=ind+1
            L=meilleur_voisin_bis(L,L_ind_perm)
    return L, conflits(L), ind, cbdisplay(n,L)

def meilleur_voisin_bis(L,L_ind_perm):
    """Renvoie le meilleur voisin (un voisin étant une transposition)"""
    n=len(L)
    a=random.randint(0,len(L)-1)
    min_conf=math.inf
    ind_min_conf=-1
    for j in range(n):
        if [a,j] not in L_ind_perm or [j,a] not in L_ind_perm:
            if conflits(transposition(L,a,j))<min_conf:
                min_conf=conflits(transposition(L,a,j))
                ind_min_conf=j
    if ind_min_conf!=-1:
        #On a trouvé une transposition favorable (transposition avec moins de conflits que le nombre de conflits de L)
        L_ind_perm.append([a,ind_min_conf])
        return transposition(L,a,ind_min_conf)
    return L # On a pas trouvé de meilleure transposition

def cbdisplay(n, perm): 
    """Affichage sous forme d'échiquier"""
    pos=np.zeros((n,n))
    for i in range (n):
        pos[perm[i], i]=1
    plt.imshow(pos,origin='lower',cmap='gray')
    plt.show()
    

    
    
      
       