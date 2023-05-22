# 1
liste_vide = []
liste = ["un", 2, {"trois": "quatre"}]

# 2
print("taille liste vide :", len(liste_vide))
print("taille liste :", len(liste))

# 3
print("liste :", liste)
liste.remove("un")
print("après remove :", liste)
liste.append(5)
print("après append :", liste)
liste[2] = "5"
print("après modif :", liste)

# 4
print("\nboucle for")
for element in liste:
    print(element)

print("\nboucle while")
index = 0
while index < len(liste):
    print(liste[index])
    index += 1
