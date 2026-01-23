from datetime import datetime
now=datetime.today().year
print ("Bonjour")
nom_1=input ("Quel est ton nom? ")
age_1=input ("Et en quelle année es-tu né(e)? ")
nom_2=input ("Quel est le nom de ta voisinne/ton voisin? ")
age_2=input ("Et en quelle année est-elle (il) né(e)? ")
age_1=int(age_1)
age_2=int(age_2)
print (f"{nom_1} a {now-age_1} ans.")
print (f"{nom_2} a {now-age_2} ans.")
if now-age_1<now-age_2:
    print (f"{nom_2} a {(now-age_2)-(now-age_1)} ans de plus que {nom_1}")
elif now-age_1>now-age_2:
    print (f"{nom_1} a {(now-age_1)-(now-age_2)} ans de plus que {nom_2}")
elif now-age_1==now-age_2:
    print (f"{nom_1} et {nom_2} ont le même age.")
else:
    print ("Erreur ;)")

