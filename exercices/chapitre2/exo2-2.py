mot_un, mot_deux = "banane", "pomme"
print(f"Premier mot : {mot_un}, second mot : {mot_deux}")
print(f"Le plus court est {mot_un}") if len(mot_un) < len(mot_deux) else print(f"le plus court est {mot_deux}")
