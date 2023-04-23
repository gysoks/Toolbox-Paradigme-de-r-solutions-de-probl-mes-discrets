##########################################################################
                # Algorithmes d'approximation on-line
##########################################################################

#Next fit

def nextfit(weight, c):
    """On suppose que weight[i]<c pour tout i dans [0,len(weight)]"""
    if (len(weight)==0):
        return 0
    res = 1
    rem = c
    for i in range(len(weight)):
        if rem >= weight[i]:
            rem = rem - weight[i]
        else:
            res+= 1
            rem = c -weight[i]
    return res

"""La complexité de cet algorithme est de O(n). """

#First Fit

def firstfit(weight,c):
    n=len(weight)
    esp_box=[c]
    i=0
    j=0
    while i<=n-1:
        if weight[i]<esp_box[j]: # L'objet i rentre dans la boite j
            esp_box[j]-=weight[i]
            print('On remplit esp_box: ',esp_box)
            i+=1 #On examine l'objet suivant
            j=0  #On repart du début de l'ensemble des boites pour les réexaminer une par une
        else:
            j+=1
            if j==len(esp_box): # On a parcouru toutes les boites ouvertes sans en trouver une pouvant loger l'objet i
                esp_box.append(c-weight[i]) #On ouvre une boite supplémentaire et on y loge l'objet i
                print('On ajoute une boîte à esp_box: ',esp_box)
                i+=1
                j=0
    return len(esp_box)

"""La compléxité de cet algorithme est de O(n**2)"""

#Best_Fit

def bestfit(weight,c):
    n=len(weight)
    esp_box=[c]
    i=0
    j=0
    while i<=n-1:
        for j in range (len(esp_box)):
            if weight[i]<esp_box[j]: # L'objet i rentre dans la boite j 
                esp_box[j]-=weight[i] #On remplit la boite d'espace résiduel minimal
                print('On remplit esp_box: ',esp_box)
                esp_box=tri_rapide(esp_box) #On retrie esp_box pour toujours avoir son premier élément correspondant à l'espace résiduel minimal
                i+=1 #On examine l'objet suivant
                
        # On a désormais parcouru toutes les boites ouvertes sans en trouver une pouvant loger l'objet i
        esp_box.append(c-weight[i]) #On ouvre une boite supplémentaire et on y loge l'objet i
        print('On ajoute une boîte à esp_box: ',esp_box)
        esp_box=tri_rapide(esp_box)
        i+=1
    return len(esp_box)

"""La compléxité de cet algorithme (dans le pire des cas) est O(n**2*ln(n))"""

def tri_rapide(L) :
    pivot = L[0]
    htdessus = []
    dessous = []
    equal = [pivot]
    for val in L :
        if val>pivot :
            dessous.append(val)
        elif val< pivot :
            htdessus.append(val)
        else :
            equal.append(val)
    return tri_decr_rapide(htdessus) + equal + tri_decr_rapide(dessous)

    
#Worst Fit

def worstfit(weight,c):
    n=len(weight)
    esp_box=[c]
    i=0
    j=0
    while i<=n-1:
        for j in range (len(esp_box)):
            if weight[i]<esp_box[j]: # L'objet i rentre dans la boite j 
                esp_box[j]-=weight[i] #On remplit la boite d'espace résiduel maximal
                print('On remplit esp_box: ',esp_box)
                esp_box=tri_decr_rapide(esp_box) #On retrie esp_box pour toujours avoir son premier élément correspondant à l'espace résiduel maximal
                i+=1 #On examine l'objet suivant
                
        # On a désormais parcouru toutes les boites ouvertes sans en trouver une pouvant loger l'objet i
        esp_box.append(c-weight[i]) #On ouvre une boite supplémentaire et on y loge l'objet i
        print('On ajoute une boîte à esp_box: ',esp_box)
        esp_box=tri_decr_rapide(esp_box)
        i+=1
    return len(esp_box)

"""La compléxité de cet algorithme (dans le pire des cas) est O(n**2*ln(n))"""

def tri_decr_rapide(L) :
    pivot = L[0]
    htdessus = []
    dessous = []
    equal = [pivot]
    for val in L :
        if val<pivot :
            dessous.append(val)
        elif val> pivot :
            htdessus.append(val)
        else :
            equal.append(val)
    return tri_decr_rapide(htdessus) + equal + tri_decr_rapide(dessous)

##########################################################################
                # Algorithmes d'approximation off-line
##########################################################################

#First Fit Decreasing

def FF_decreasing(weight,c):
    weight=tri_decr_rapide(weight)
    return firstfit(weight,c)

"""La complexité est la même que pour FirstFit. """

#Best Fit Decreasing

def BF_decreasing(weight,c):
    weight=tri_decr_rapide(weight)
    return bestfit(weight,c)

"""La complexité est la même que pour Best Fit."""


import os


def import_config(nom_fichier):
    fichier = open(nom_fichier, "r")
    l = fichier.readline()
    n = int(l)
    l = fichier.readline()
    c = int(l)
    weight=[]
    for i in range(n):
        l = fichier.readline()
        weight.append(int(l))
    fichier.close()
    return (n, c, weight)
            

def main():
    #print("Entrer la liste d'objets: ")
    #weight= input()
    
    weight = [2, 5, 4, 7, 1, 3, 8]
    c = 10
    #print(os.getcwd())
    #[_, c, weight] = import_config("binpack_001.in")
    #print("Our data == capacity :", c, "weights :", weight, "\n\n")
    print("Choisissez une méthode: nextfit, firstfit, bestfit, worstfit, BF_decreasing,FF_decreasing")
    x=input()
    if x=="nextfit":
        print("Number of bins required in Next Fit :",
                               nextfit(weight, c))
    elif x=="bestfit":
        print("Number of bins required in Best Fit :",
                               bestfit(weight, c))
    elif x=="firstfit":
        print("Number of bins required in First fit :",
                               firstfit(weight, c))
    elif x=="worstfit":
        print("Number of bins required in Worst Fit :",
                               worstfit(weight, c))
    elif x=="BF_decreasing":
        print("Number of bins required in BF_decreasing :",
                               BF_decreasing(weight, c))
    elif x=="FF_decreasing":
        print("Number of bins required in FF_decreasing :",
                               FF_decreasing(weight, c))






if __name__ == "__main__":
    main()


    
    



