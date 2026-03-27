import string


def compteur_lettres(mot):
    nombre_lettre=0
    for lettre in mot:
        if lettre.lower() in list(string.ascii_lowercase):
        #nombre_lettres=nombre_lettre+1
            nombre_lettre+=1 #sert à augmenter de 1 unité la valeur de la variable nombre_lettre
    return nombre_lettre

phrase="je voudrais un joli chateau"

nombre_lettre=compteur_lettres(phrase)
print("Dans la phrase : ")
print(f"{phrase}")
print(f"Il y a {nombre_lettre} lettres")
