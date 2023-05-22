def creer_plus(ajout):
    def plus(increment):
        return ajout + increment
    return plus


if __name__ == "__main__":
    p = creer_plus(23)
    q = creer_plus(42)
    print(p(100))  # affiche 123 (23 + 100)
    print(q(100))  # affiche 142 (42 + 100)
