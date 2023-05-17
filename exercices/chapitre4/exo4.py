def add_trois(liste):
    for item in liste:
        if liste[item] >= 2:
            liste[item] += 3
    return liste


if __name__ == "__main__":
    ma_liste = [0, 1, 2, 3, 4, 5]
    print(ma_liste)
    ma_liste = add_trois(ma_liste)
    print(ma_liste)
