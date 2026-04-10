name=input("Quel est ton nom ? ")
taille=input("Quelle est ta taille ? ")
taille=int(taille)
print(f"Bonjour {name}.")
if taille==160:
    vsnatalie=(taille - 160)
    print("Tu as la même taille que Natalie, c'est incroyable.")
elif taille<160:
    vsutilisateur=(160 - taille)
    print(f"Natalie est {vsutilisateur} cm plus grande que toi.")
elif taille>160:
    vsgeant=(taille - 160)
    print(f"Tu es {vsgeant} cm plus grand(e) que Natalie.")
