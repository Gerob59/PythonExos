import parfait_chanceux_m as pc
import easygui

# Initialisation des listes
parfaits = []
chanceux = []

# Parcours de l'intervalle [2,1000] et remplissage des listes
for n in range(2, 1001):
    if pc.est_parfait(n):
        parfaits.append(n)
    if pc.est_chanceux(n):
        chanceux.append(n)

# Affichage des listes dans des boîtes de message
easygui.msgbox("Liste des nombres parfaits : \n\n" + str(parfaits))
easygui.msgbox("Liste des nombres chanceux : \n\n" + str(chanceux))
