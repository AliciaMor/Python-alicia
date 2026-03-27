import math


def menu():
    print("Pour calculer l'aire d'un carré, tapez 1.")
    print("Pour calculer l'aire d'un triangle, tapez 2.")
    print("Pour calculer l'aire d'un cercle, tapez 3.")
    choix=input("Votre choix : ")
    choix=int(choix)

    if choix==1:
        aire_carre()
    elif choix==2:
        aire_triangle()
    elif choix==3:
        aire_cercle()
    elif choix==0:
        quit()


def quit():
    print("Au revoir")
def aire_carre():
    cote=input("Quelle est la longueur du côté de votre carré ?")
    cote=float(cote)
    aire=cote**2
    print(f"L'aire de votre carré vaut : {aire}")
    menu()

def aire_triangle():
    base=input("Quelle est la longueur de la base de votre triangle ?")
    hauteur=input("Quelle est la hauteur de votre triangle ?")
    base=float(base)
    hauteur=float(hauteur)
    aire=(base*hauteur)/2
    print(f"L'aire de votre triangle vaut : {aire}")
    menu()

def aire_cercle():
    rayon=input("Quelle est la valeur du rayon du cercle ?")
    rayon=float(rayon)
    aire=math.pi*rayon**2
    print(f"L'aire du cerlce vaut {aire}")
    menu()

if __name__=="__main__":
    menu()
