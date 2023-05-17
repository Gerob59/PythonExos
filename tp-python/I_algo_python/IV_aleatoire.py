from random import randint, randrange, choice, shuffle

liste = [1, 2, 3, 4, 5]

# randint(a, b): Retourne un entier aléatoire entre a et b inclusivement.
nombre_aleatoire = randint(1, 10)
print("randint(1, 10) :", nombre_aleatoire)

# randrange(start, stop, step):
# Retourne un élément aléatoire de start à stop avec un interval de step.
# Le paramètre start est inclusif, tandis que stop est exclusif
nombre_aleatoire = randrange(1, 10, 2)
print("\nrandrange(1, 10, 2) :", nombre_aleatoire)

# choice(liste): Retourne un élément aléatoire d'une liste.
print("\nliste :", liste)
element_aleatoire = choice(liste)
print("choice(liste) :", element_aleatoire)

# shuffle(liste): Mélange les éléments d'une liste.
print("\nliste :", liste)
shuffle(liste)
print("shuffle(liste) :", liste)
