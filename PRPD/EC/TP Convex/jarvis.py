import math
from utils import determinant, scatter_plot


def jarvis(points, show=True, save=False, detailed=True):
    
    """Le point d'origine est choisi comme étant le point avec la + petite ordonnée"""
    O=points[0]
    for p in points[1:]:
        if (p[1]<O[1]) or(p[1]==O[1] and p[0]<O[0]):
            O = p 
    print(O)
    res = [O]
    points.remove(O)
    print(points)
    
    
    P=points[0]
    """On sélectionne le 1er point"""
    for P1 in points[1:]:
        if determinant(res[-1], P, P1)>0:
            P = P1
        if detailed :
            scatter_plot(points,  rays=[[res[-1], P1]],show=show, save=save)
    res.append(P)
    points.remove(P)
    
    """Intégrer le point d'origine à l'ensemble des points permet d'avoir une condition d'arrêt"""
    points.append(O)  
    
    while (P!=res[0]):
        
        P=points[0]
        for P1 in points:
            if determinant(res[-1], P, P1)>0: 
                """Cela revient à vérifier que pi-angle(res[-2], res[-1], P1) < pi -angle(res[-2], res[-1], P), se référer au schéma explicatif"""
                P = P1
            if detailed :
                scatter_plot(points, [res], rays=[[res[-1], P1]],show=show, save=save)
                
        res.append(P)
        points.remove(P)
        scatter_plot(points, [res],show=show, save=save)
        
    """Afin de respecter la condition d'arrêt, on retire le dernier élément de res (soit le 1er élément de l'enveloppe convexe)"""
    res.pop()
    
    return res 
    
    
    