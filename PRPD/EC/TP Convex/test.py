from random import seed

""" On importe les différentes méthodes à tester"""
from jarvis import jarvis
from eddy import eddy
from shamos import shamos 
from graham import graham

from utils import create_points, scatter_plot


def main():

    # initialize the random generator seed to always use the same set of points
    seed(0)
    # creates some points
    pts = create_points(15)
    show = True  # to display a frame
    save = False  # to save into .png files in "figs" directory
    scatter_plot(pts, [[]], title="convex hull : initial set", show=show, save=save)
    print("Points:", pts)
    # compute the hull
    
    #Si méthode GRAHAM:
    hull = graham(pts, show=show, save=save)
    
    # Si méthode EDDY:
    #   hull = eddy(pts)
    
    # Si méthode SHAMOS:
    #   hull = shamos(pts)
    
    # Si méthode JARVIS:
    #   hull = jarvis(pts)
    
    print("Hull:", hull)
    scatter_plot(pts, [hull], title="convex hull : final result", show=True, save=save)


if __name__ == "__main__":
    main()
