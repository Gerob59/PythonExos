from I_df import df
from I_df_city import df_city
from df_city_type import df_city_type

# 1
print(40*"=", "question 1")
print(df.dtypes)

print(40*"*", "df_city")
print(df_city.dtypes)
print(40*"*", "df_city updated")
df_city = df_city.astype(df_city_type)
print(df_city.dtypes)

# 2
print("\n", 40*"=", "question 2")
print(df.shape)  # (35798, 12) / (row, column)
print(df_city.shape)  # (34932, 29) / (row, column)

# 3
print("\n", 40*"=", "question 3")
unique_values = df_city["LIBGEO"].nunique()
print("Nombre de valeurs uniques dans df_city['LIBGEO']:", unique_values)

# 4
print("\n", 40*"=", "question 4")
# Identifier les doublons de LIBGEO
duplicates = df_city[df_city.duplicated('LIBGEO', keep=False)]
# Sélectionner les codes correspondant aux doublons de LIBGEO
x = duplicates['CODGEO'].unique()
print(x)

# 5
print("\n", 40*"=", "question 5")
# Compter le nombre de codes communes distincts par libellé
df_city['Count'] = df_city.groupby('LIBGEO')['CODGEO'].transform('nunique')
# Filtrer les observations où le nombre de codes communes distincts est supérieur à 2
filtered_df = df_city[df_city['Count'] > 2]
# Afficher les observations filtrées
print(filtered_df)

# 6
print("\n", 40*"=", "question 6")
# Réordonner la base par ordre alphabétique du libellé de commune
sorted_df = filtered_df.sort_values('LIBGEO')
# Afficher la base réordonnée
print(sorted_df)

# 7.1
print("\n", 40*"=", "question 7.1")
# Calculer les statistiques descriptives pour les données où les libellés et les codes communes coïncident
matching_stats = df_city[df_city['LIBGEO'] == df_city['CODGEO']]['NBPERSMENFISC16'].describe()
# Afficher les statistiques descriptives
print("Statistiques descriptives pour les données où les libellés et les codes communes coïncident:")
print(matching_stats)

# 7.2
print("\n", 40*"=", "question 7.2")
# Calculer les statistiques descriptives pour les données où les libellés et les codes communes ne coïncident pas
non_matching_stats = df_city[df_city['LIBGEO'] != df_city['CODGEO']]['NBPERSMENFISC16'].describe()
# Afficher les statistiques descriptives
print("Statistiques descriptives pour les données où les libellés et les codes communes ne coïncident pas:")
print(non_matching_stats)
