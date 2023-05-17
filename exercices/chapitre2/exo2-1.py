mot_un, mot_deux = "banane", "pomme"
print(f"Premier mot : {mot_un}, second mot : {mot_deux}")
if len(mot_un) < len(mot_deux):
    print(f"Le mot le plus court est {mot_un}")
elif len(mot_un) > len(mot_deux):
    print(f"Le mot le plus court est {mot_deux}")
else:
    print(f"Les mots {mot_un} et {mot_deux} sont de même taille")
