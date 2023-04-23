
import math
from utils import *

def graham(points, show=True, save=False, detailed=True):
   
    """1ere étape: on trouve le point pivot (point de + petite ordonnée)"""
    Pmin=points[0]
    for val in points[1:]:
        if (val[1]<Pmin[1]) or(val[1]==Pmin[1] and val[0]<Pmin[0]):
            Pmin = val
    
    """2e étape et 3e étape: mise sous forme de coordonnées polaires
                            et tri par corrdonnées polaires croissantes"""
    L_polaire = polar_quicksort(points, Pmin)
    
    
    """4e étape: élimination des points inutiles"""
    for i in range (len(L_polaire)-2, -1, -1):
        if polar_angle(L_polaire[i],Pmin)==polar_angle(L_polaire[i+1],Pmin):
            del L_polaire[i]
    
    """5e étape: on établit l'enveloppe convexe en supprimant tout point
                conduisant à un virage à droite au lieu d'un virage à gauche"""
    k=0
    while (k<len(L_polaire)-2) :
        print([L_polaire[k], L_polaire[k+1], L_polaire[k+2]])
        if determinant(L_polaire[k],L_polaire[k+1],L_polaire[k+2])>0:
            """On a bien un tournant à gauche"""
            k+=1
        else:
            L_polaire.pop(k+1)
            k-=1
        if detailed :
            scatter_plot(points, [L_polaire[:k+1]], rays = [[L_polaire[k],L_polaire[k+1]]],  show=show, save=save)
    scatter_plot(points, [L_polaire], show=show, save=save)
    return L_polaire
    