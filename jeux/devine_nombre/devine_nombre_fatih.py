import random
import time
s = 1
prompt = -1

score = 0

o = 0
n = 1000
e = 10000

lvl = input("pressez n pour un mode normal ou x pour le mode extreme :")
if lvl == "n":
    a = n
    print("mode normal")
else:
    a = e
    print("mode extreme")

target = random.randint(-a, a)
score = a

# initialisation du temps
start_time = time.time()

while prompt != target:
    prompt = input("Trouvez le nombre entre {} et {} :" .format(-a, a))
    print("Tentative n°", s)

    try:
        prompt = int(prompt)
    except ValueError:
        print("Entrer un nombre entier")
        continue

    if prompt < -a or prompt > a:
        print("ERREUR : Entrer un nombre entre ", -a, "et", a)
    else:
        if prompt > target:
            s += 1
            print("MOINS")
        elif prompt < target:
            s += 1
            print("PLUS")
        else:
            end_time = time.time()
            game_time = round(end_time - start_time, 1)
            score = round(score/s/game_time*100)
            print("Félicitation, votre score est de :", score, "avec un temps de ", round(game_time), " secondes")
            break
