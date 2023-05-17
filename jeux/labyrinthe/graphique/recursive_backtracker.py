import random


def recursive_backtracker(grid):
    stack = []
    visited = set()

    # Choisir une cellule de départ aléatoire
    row, col = random.randint(0, len(grid) - 1), random.randint(0, len(grid[0]) - 1)

    # Ajouter la cellule de départ à la pile et aux cellules visitées
    stack.append((row, col))
    visited.add((row, col))

    while stack:
        # Récupérer la dernière cellule visitée de la pile
        current = stack[-1]
        row, col = current

        # Trouver les voisins non visités de la cellule actuelle
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        unvisited_neighbors = [n for n in neighbors if
                               n not in visited and 0 <= n[0] < len(grid) and 0 <= n[1] < len(grid[0])]

        if unvisited_neighbors:
            # Choisir un voisin aléatoire et casser le mur entre les deux cellules
            next_row, next_col = random.choice(unvisited_neighbors)
            if next_row < row:
                grid[row][col] &= ~1
                grid[next_row][next_col] &= ~4
            elif next_row > row:
                grid[row][col] &= ~4
                grid[next_row][next_col] &= ~1
            elif next_col < col:
                grid[row][col] &= ~2
                grid[next_row][next_col] &= ~8
            elif next_col > col:
                grid[row][col] &= ~8
                grid[next_row][next_col] &= ~2

            # Ajouter le voisin à la pile et aux cellules visitées
            stack.append((next_row, next_col))
            visited.add((next_row, next_col))
        else:
            # Aucun voisin non visité, retirer la cellule actuelle de la pile
            stack.pop()
