from utils import *


"""On se sert de la fonction de graham pour réaliser la méthode shamos"""
def graham_shamos(points, all_points, show=True, save=False, detailed=True): 
    
    
    Pmin=points[0]
    for val in points[1:]:
        if (val[1]<Pmin[1]) or(val[1]==Pmin[1] and val[0]<Pmin[0]):
            Pmin = val 
    
    "'""2e étape et 3e étape: tri de la liste en fonction de l'angle polaire par rapport au point de référence"""
    L_polaire = polar_quicksort(points, Pmin)
    
    
    """4e étape: Elimination des points inutils"""
    for i in range (len(L_polaire)-2, -1, -1):
        if polar_angle(L_polaire[i],Pmin)==polar_angle(L_polaire[i+1],Pmin):
            del L_polaire[i]
    
    #Etape 5: 
    i=0
    while (i<len(L_polaire)-2) :  #nécessairement points2[0] points2[1] et points2[-1] appartiennent à l'enveloppe convexe, d'où l'intérêt de la sélection du point d'ancrage
        print([L_polaire[i], L_polaire[i+1], L_polaire[i+2]])
        if determinant(L_polaire[i],L_polaire[i+1],L_polaire[i+2])>0: #On détermine si on a bel et bien un tournant à gauche
            i+=1
        else:
            L_polaire.pop(i+1)
            i-=1
        if detailed :
            scatter_plot(all_points, [L_polaire[:i+1]], rays = [[L_polaire[i],L_polaire[i+1]]],  show=show, save=save)
    scatter_plot(all_points, [L_polaire], show=show, save=save)
    return L_polaire
  
   
def shamos(pts):
    if len(pts)<=6:
        return graham_shamos(pts, pts)
    
    """On réalise, par récursivité, deux sous enveloppes convexes"""
    S1, S2 = shamos(pts[:len(pts)//2]), shamos(pts[len(pts)//2:])
    
    """ On choisit un point interne à S1 (son barycentre)"""
    G= [(S1[0][0] + S1[1][0] + S1[2][0])/3, (S1[0][1] + S1[1][1] + S1[2][1])/3]
    if point_in_polygon(G, S2):
        S = S1+S2
    else : 
        p1, p2 = S2[0], S2[0]
        for p in S2[1:]:
            if determinant(G, p1, p)>0:  
                """Le point P se trouve à gauche du segment [gP1]"""  
                p1= p
            elif determinant(G, p2, p)<0:
                p2 = p
        """On retire les points n'appartenant pas au polygone formé par G, p1 et p2"""
        S=[]
        for p in pts :
            if not point_in_polygon(p, [G, p1, p2]):
                S.append(p)
    
    return graham_shamos(S, pts)
        
    
    
    
    
