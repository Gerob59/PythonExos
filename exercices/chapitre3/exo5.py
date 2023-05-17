def somme(tuple_de_longueur_variable):
    count = 0
    for x in tuple_de_longueur_variable:
        count += x
    return count


if __name__ == "__main__":
    print(somme((12, 15, 12, 15)))
    print(somme((12, 15)))
    