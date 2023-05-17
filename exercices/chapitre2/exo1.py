import math

my_float = float(input("Saisissez un flottant positif"))
if my_float >= 0:
    print("La racine de", my_float, "est", math.sqrt(my_float))
else:
    print("Erreur : le nombre saisit est inférieur négatif")
    