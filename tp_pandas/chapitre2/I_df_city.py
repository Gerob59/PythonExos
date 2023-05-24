import pynsee.download
import pandas as pd
import random
from tp_pandas.chapitre1.data import df_city

# random.choices(data, weights, cum_weights, k)
# data : les elements à tirer
# weights : séquence de poids associés à chaque élément de data
# cum_weights : séquence de poids cumulatifs associés à chaque élément de data
# k : nombre d'éléments à tirer. Par défaut, il est fixé à 1.

if __name__ == "__main__":
    # 1
    print("\n", 40 * "=", "question 1")
    print("10 premieres valeurs :", df_city.head(1))
    print("15 dernières valeurs :", df_city.tail(15))
    print("10 valeurs aléatoire :", df_city.sample(10))

    # 2
    print("\n", 40 * "=", "question 2")
    sample_5_percent = df_city.sample(frac=0.05, replace=False)
    print(sample_5_percent)

    # 3
    print("\n", 40 * "=", "question 3")
    first_10_rows = df_city.head(10)
    sample_100 = first_10_rows.sample(n=100, replace=True)
    print(sample_100)

    # 4
    print("\n", 40 * "=", "question 4")
    first_6_rows = df_city.head(6)
    # Créer une liste des poids pour les tirages
    weights = [0.5] + [0.5 / (len(first_6_rows) - 1)] * (len(first_6_rows) - 1)
    # Effectuer les 100 tirages avec les poids spécifiés
    sample_100_with_weights = random.choices(first_6_rows.index, k=100, weights=weights)
    # Compter combien de fois chaque échantillon a été choisi
    counts = pd.Series(sample_100_with_weights).value_counts()
    print(counts)
