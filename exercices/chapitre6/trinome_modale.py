import easygui as eg
from trinome import racines

# Saisie des coefficients du trinôme
a = float(eg.enterbox(msg='Coefficient a :', title='Trinôme réel', default='1'))
b = float(eg.enterbox(msg='Coefficient b :', title='Trinôme réel', default='-3'))
c = float(eg.enterbox(msg='Coefficient c :', title='Trinôme réel', default='2'))

# Calcul des racines du trinôme
result = racines(a, b, c)

# Affichage des résultats
if result[0] == 0:
    eg.msgbox(msg="Le trinôme n'a pas de racine réelle.", title="Résultats du trinôme réel")
elif result[0] == 1:
    eg.msgbox(msg=f"Le trinôme a une racine réelle : {result[1]}", title="Résultats du trinôme réel")
else:
    eg.msgbox(msg=f"Le trinôme a deux racines réelles : {result[1]} et {result[2]}", title="Résultats du trinôme réel")
