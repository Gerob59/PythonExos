def get_data_from_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            values = line.split(' ')
            if len(values) == 2:
                x = int(values[0])
                y = int(values[1])
                data.append((x, y))
    return data


if __name__ == "__main__":
    filename = 'stats.dat'
    data = get_data_from_file(filename)
    print(data)


def copie(t):
    return t.copy()  # Utilisation de la méthode copy() pour créer une copie du tableau


def inverse(t):
    return t[::-1]  # Utilisation du slicing avec un pas -1 pour inverser l'ordre
