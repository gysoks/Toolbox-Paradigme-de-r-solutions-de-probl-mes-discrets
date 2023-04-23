import math
from utils import determinant, scatter_plot, distance_from_point_to_line

def partition(points):
    upper =[]
    lower = []
    Xmax, Xmin = points[0], points[0]
    for P in points[1:]:
        if P[0]<Xmin[0]:
            Xmin =P
        elif P[0]>Xmax[0]:
            Xmax = P
    points.remove(Xmin)
    points.remove(Xmax)
    scatter_plot(points, [[Xmin, Xmax]], show = True, save = False)
    for P in points:
        val = determinant(Xmin, Xmax, P)
        if val> 0:
            upper.append(P)
        elif val<0 :
            lower.append(P)
    return Xmin, Xmax, upper, lower
    
def convex_upper(points2, Xmin, Xmax, points):
   
    if len(points2)==0:
        scatter_plot(points,[[Xmin, Xmax]], show=True, save=False)
        return []
    elif len(points2)==1:
        scatter_plot(points, [[Xmin, Xmax]], rays=[[Xmin, Xmax]+points2], show=True, save = False)
        scatter_plot(points,[[Xmin,Xmax]+points2], show=True, save=False)
        return points2
    else :
       
        """Recherche du point le plus éloigné UPmax de la droite (formée par les points Xmin et Xmax)."""
        UPmax = None
        max_high = 0  
        for P in points2 :
            scatter_plot(points, [[Xmin, Xmax]], rays=[[Xmin, Xmax, P]], show=True, save = False)
            high = distance_from_point_to_line(P, [Xmin, Xmax])
            if high>max_high:
                UPmax = P
                max_high = high
        scatter_plot(points, [[Xmin, Xmax, UPmax]], show=True, save = False)
        
        """Partition des points de pts selon qu'ils se situent à gauche ou à droite de la hauteur de (Xmin Xmax) passant par UPmax"""
        upper_left= []
        upper_right = []
        for P in points2 :
            if determinant(Xmin, UPmax, P)>0:
                upper_left.append(P)
            elif determinant(UPmax, Xmax, P)>0 :
                upper_right.append(P)
        
        return convex_upper(upper_right, UPmax, Xmax, points) + [UPmax] + convex_upper(upper_left, Xmin, UPmax, points)

def convex_lower(points2, Xmin, Xmax, points):
   
    if len(points2)==0:
        scatter_plot(points,[[Xmin, Xmax]], show=True, save=False)
        return []
    elif len(points2)==1:
        scatter_plot(points, [[Xmin, Xmax]], rays=[[Xmin, Xmax]+points2], show=True, save = False)
        scatter_plot(points,[[Xmin,Xmax]+points2], show=True, save=False)
        return points2
    else :
        """Recherche du point le plus éloigné de la droite (formée par les points Xmin et Xmax) parmi les points en dessous de la droite"""
        lowest = None
        max_high = 0  
        for P in points2 :
            scatter_plot(points, [[Xmin, Xmax]], rays=[[Xmin, Xmax, P]], show=True, save = False)
            high = distance_from_point_to_line(P, [Xmin, Xmax])
            if high>max_high:
                lowest = P
                max_high= high
        scatter_plot(points, [[Xmin, Xmax, lowest]], show=True, save = False)
        """Partition des points de pts selon qu'ils se situent à gauche ou à droite de la hauteur de (Xmin Xmax) et passant par UPmax."""
        lower_left= []
        lower_right = []
        
        for P in points2 :
            if determinant(Xmin, lowest, P)<0:
                lower_left.append(P)
            elif determinant(lowest, Xmax, P)<0 :
                lower_right.append(P)
        return convex_lower(lower_left,Xmin, lowest, points) + [lowest] + convex_lower(lower_right, lowest, Xmax, points)
    

def eddy(pts):
    """Fonction finale Eddy"""
    Xmin, Xmax, upper, lower = partition(pts)
    hull=[Xmin] + convex_lower(lower, Xmin, Xmax, pts) + [Xmax] + convex_upper(upper, Xmin, Xmax, pts)
    return hull
    


