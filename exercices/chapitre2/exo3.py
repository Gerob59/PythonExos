pSeuil: float = 2.3
vSeuil: float = 7.41

pression = float(input("Entrez votre pression : "))
volume = float(input("Entrez votre volume : "))

if pression > pSeuil and volume > vSeuil:
    print("Arret immediat")
elif pression > pSeuil:
    print("Augmentez le volume de l’enceinte")
elif volume > vSeuil:
    print("Diminuez le volume de l’enceinte")
else:
    print("tout va bien")