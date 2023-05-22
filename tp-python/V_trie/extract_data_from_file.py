def get_data_from_file(filename):
    data = []
    with open(filename, 'r') as file:  # ouvre le fichier en lecture seul
        for line in file:  # boucle sur toutes les lignes du fichier
            line = line.strip()  # enlève les espaces inutiles avant et après la phrase
            values = line.split(' ')  # créé un tableau grace au séparateur
            if len(values) == 2:
                x = int(values[0])
                y = int(values[1])
                data.append((x, y))
    return data


if __name__ == "__main__":
    # Récupérer de la data depuis un fichier
    my_file = 'stats.dat'
    file_data = get_data_from_file(my_file)
    print(file_data)