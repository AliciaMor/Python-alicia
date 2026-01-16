import random

nombre_1=random.randint(1,10)
nombre_2=random.randint(1,10)

reponse=input(f"Quelle est la somme de {nombre_1} et {nombre_2} ?")
reponse=float(reponse)
if reponse==nombre_1+nombre_2 :
    print("Pour une fois que tu réussis")
else:
    print("Retourne en primaire")
