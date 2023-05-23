import timeit
from tp_pandas.chapitre3.df import df

df.set_index('INSEE commune', inplace=True)
df['dep'] = df.index.str.slice(0, 2)


def compare_execution_times(dataframe):
    sectors = dataframe.columns[1:-1]  # Colonnes correspondant aux secteurs d'activité sans 'dep' et 'Communes'

    execution_times = {}  # Dictionnaire pour stocker les temps d'exécution combinés par secteur

    # Boucle sur les départements
    for dep in dataframe['dep'].unique():
        total_time = 0  # Temps d'exécution combiné pour chaque département

        # Boucle sur les secteurs d'activité
        for sector in sectors:
            # Création de la chaîne de caractères pour le calcul de la somme
            calculation_str = f"df[df['dep'] == '{dep}']['{sector}'].sum()"

            # Calcul du temps d'exécution pour chaque secteur
            execution_time = timeit.timeit(lambda: eval(calculation_str), number=10)

            # Ajout du temps d'exécution au temps total
            total_time += execution_time

            # Stockage du temps d'exécution par secteur dans le dictionnaire
            if dep not in execution_times:
                execution_times[dep] = {}
            execution_times[dep][sector] = execution_time

        # Affichage du temps d'exécution total par département
        print(f"Temps d'exécution total pour le département {dep}: {total_time} secondes")
        print()

    # Affichage du détail des temps d'exécution par département et par secteur
    for dep, times in execution_times.items():
        print(f"Temps d'exécution pour le département {dep}:")
        for sector, time in times.items():
            print(f"- {sector}: {time} secondes")
        print()


# 1
df_copy = df.copy()
df_copy2 = df.copy()

# 2
df_copy = df_copy.set_index('dep')
df_copy2 = df_copy2.reset_index(drop=True)

# 3
print("\n", 40*"=", "question 3")
# print(40*"*", "df_copy")
# compare_execution_times(df_copy)
print(40*"*", "df_copy2")
compare_execution_times(df_copy2)
