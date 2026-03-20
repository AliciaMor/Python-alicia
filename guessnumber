import random

recommencer=True
while recommencer :
    nombre_inconnu=random.randint(1,20)
    proposition=int()
    while proposition!= nombre_inconnu:
        proposition=input("Faites une proposition...")
        proposition=int(proposition)
    
        if proposition==nombre_inconnu:
            print("Bravo vous avez gagné uwu!")
            recommencer=input("Voulez-vous recommencer (o/n)?")
            while recommencer not in ["o","n"]:
                 print("Veuillez répondre par oui (o) ou par non (n)")
                 recommencer=input("Voulez vous recommencer (o/n)")
            if recommencer=="o" : recommencer=True
            else : recommencer=False
        elif proposition<nombre_inconnu:
            print("Le nombre recherché est plus grand.")
        elif proposition>nombre_inconnu:
            print("Le nombre recherché est plus petit.")
