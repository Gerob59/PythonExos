my_number = float(input("Entrez un nombre entre 1 et 10"))
if my_number > 10:
    print(f"{my_number} est trop haut")
elif my_number < 1:
    print(f"{my_number} est trop bas")
else:
    print(f"{my_number} est bon")
