import math


def som_div(n):
    """Retourne la somme des diviseurs propres de n."""
    somme = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            somme += i
            if i != n // i and i != 1:
                somme += n // i
    return somme


def est_parfait(n):
    """Retourne True si n est un nombre parfait, False sinon."""
    return som_div(n) == n


def est_premier(n):
    """Retourne True si n est un nombre premier, False sinon."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def est_chanceux(n):
    """Retourne True si n est un nombre chanceux, False sinon."""
    for i in range(2, n):
        if n % i == 0 and not est_premier(i + 1):
            return False
    return True


def test():
    """Teste les fonctions du module."""
    assert som_div(12) == 16
    assert est_parfait(6)
    assert est_premier(31)
    assert est_chanceux(11)
    print("Tous les tests ont réussi.")


if __name__ == '__main__':
    test()
