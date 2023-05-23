import pandas as pd

from tp_pandas.chapitre3.df import df

# Étape 1: Copie
df_wide = df.copy()

# Étape 2: Reconstruire le DataFrame au format long et faire la somme par département et secteur
df_long = df_wide.melt(id_vars=['Commune', 'INSEE commune'], var_name='Secteur', value_name='Emissions_CO2')
df_long = df_long.groupby(['INSEE commune', 'Secteur'])['Emissions_CO2'].sum().reset_index()

# Étape 3: Passer au format wide avec une ligne par secteur et une colonne par département
df_wide = df_long.pivot(index='Secteur', columns='INSEE commune', values='Emissions_CO2')

# Étape 4: Calculer la place du département dans la hiérarchie des émissions nationales pour chaque secteur
df_wide['Total_Emissions'] = df_wide.sum(axis=1)  # Calculer les émissions totales par secteur
df_wide['Rank'] = df_wide['Total_Emissions'].rank(ascending=False)  # Calculer le rang des émissions par secteur

# Étape 5: Calculer le rang médian de chaque département dans la hiérarchie des émissions et sélectionne les 10 derniers
df_median_rank = df_wide.median(axis=0).sort_values(ascending=False).reset_index()
top_10_worst_departments = df_median_rank.head(10)
print(top_10_worst_departments)
