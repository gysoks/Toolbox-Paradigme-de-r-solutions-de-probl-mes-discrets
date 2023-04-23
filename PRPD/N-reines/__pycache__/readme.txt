Les algorithmes sont codés avec Python (Spyder 3.9).


Algorithme hill_climbing:

On part d'un situation initiale (permutation initiale) puis on évalue parmi tous ces voisins le meilleur voisin. 
Dans ce cas-ci, on tire au hasard un indice a et on regarde pour quel indice j la transposition(L,a,j) est la plus optimale, 
c'est à dire qu'elle comporte le moins de conflits.
Cette recherche de meilleur voisin est très efficace, mais cette heuristique NE PERMET PAS NECESSAIREMENT DE TOMBER SUR UN MINIMUM GLOBAL.


Algrorithme recuit simulé:

Ici, on ne compare qu'un voisin à la fois. La présence de la probabilité sous la forme exp(-lamba*t) permet dans certain cas de 
tomber sur un MINIMUM GLOBAL.


Algorithme génétique:

On choisit une population initiale de N individus (chaque individu étant une permutation de taille n). Des mécanismes de mutation et de croisement
entrent en jeu dans l'évolution de la population. A la fin, on ne garde que le meilleur individus (celui présentant le moins de conflits).

Petit problème du code génétique:

Les fonctions de mutation et de croisement fonctionnent mais j'ai rencontré quelques problèmes 
concernant la syntaxe python qui m'empêche de retourner le meilleur individus de la population sous forme de liste de taille n 
(la liste sortante est de taille n/2).