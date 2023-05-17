# définir les ensembles X et Y
X = {'a', 'b', 'c', 'd'}
Y = {'s', 'b', 'd'}

# afficher les ensembles initiaux
print("\n1/ Les ensembles initiaux")
print("X =", X)
print("Y =", Y)

# tester l'appartenance de 'c' à X
print("\n2/ Le test d’appartenance de l’élément 'c' à X")
if 'c' in X:
    print("'c' appartient à X")
else:
    print("'c' n'appartient pas à X")

# tester l'appartenance de 'a' à Y
print("\n3/ Le test d’appartenance de l’élément 'a' à Y")
if 'a' in Y:
    print("'a' appartient à Y")
else:
    print("'a' n'appartient pas à Y")

# afficher les ensembles X-Y et Y-X
print("\n4/ Les ensembles X - Y et Y - X")
print("X - Y =", X-Y)
print("Y - X =", Y-X)

# afficher l'union de X et Y
print("\n5/ L’ensemble X | Y (union)")
print("X | Y =", X | Y)

# afficher l'intersection de X et Y
print("\n6/ L’ensemble X \ Y (intersection)")
print("X \ Y =", X & Y)
