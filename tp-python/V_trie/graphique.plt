# Définition du fichier de données
datafile = "stats.dat"

# Configuration du tracé
set title "Points à partir de stats.dat"
set xlabel "Valeur en abscisse"
set ylabel "Valeur en ordonnée"

# Chargement des données
plot datafile using 1:2 with points title "Points"
