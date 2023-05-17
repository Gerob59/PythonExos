def table(base, debut, fin, inc):
    print(f"Table de multiplication de {base}")
    for i in range(debut, fin+1, inc):
        resultat = base * i
        print(f"{base} x {i} = {resultat}")


if __name__ == "__main__":
    table(5, 1, 20, 1)
