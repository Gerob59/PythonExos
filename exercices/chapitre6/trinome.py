def racines(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return 0,
    elif delta == 0:
        x0 = -b / (2*a)
        return 1, x0
    else:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        return 2, x1, x2


if __name__ == "__main__":
    print(racines(1, -3, 2))  # attendu : (2, 1.0, 2.0) car 2 racines
    print(racines(1, -2, 1))  # attendu : (1, 1.0) car 1 racine
    print(racines(1, 1, 1))  # attendu : (0,) car 0 racine
