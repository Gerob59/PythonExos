def combinaisons(chaine1, chaine2):
    return [a+b for a in chaine1 for b in chaine2]


if __name__ == "__main__":
    result = combinaisons("abc", "de")
    print(result)
