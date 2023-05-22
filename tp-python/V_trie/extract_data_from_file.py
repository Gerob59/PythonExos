# définis un dictionnaire avec les titres des colonnes et leurs valeurs
def get_data_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()  # Lire toutes les lignes du fichier
        titles = lines[0].strip().split(' ')
        data = [line.strip().split(' ') for line in lines[1:] if len(line.strip().split(' ')) == 2]
        x = [int(values[0]) for values in data]
        y = [float(values[1]) for values in data]
    return {'titre_x': titles[0], 'titre_y': titles[1], 'tableau_x': x, 'tableau_y': y}
