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

# 7
df['INSEE commune'] = df['INSEE commune'].str.strip().str.lower()
df['Commune'] = df['Commune'].str.strip().str.lower()
df_city['CODGEO'] = df_city['CODGEO'].str.strip().str.lower()
df_city['LIBGEO'] = df_city['LIBGEO'].str.strip().str.lower()

# 7.1
print("\n", 40*"=", "question 7.1")
merged_df = df.merge(df_city, left_on=['INSEE commune', 'Commune'], right_on=['CODGEO', 'LIBGEO'])
mean_all = merged_df['NBPERSMENFISC16'].mean()
std_all = merged_df['NBPERSMENFISC16'].std()
min_all = merged_df['NBPERSMENFISC16'].min()
max_all = merged_df['NBPERSMENFISC16'].max()
print("merged_df", merged_df)
print(f"mean_all: {mean_all}, std_all: {std_all}, min_all: {min_all}, max_all: {max_all}")

# 7.2
print("\n", 40*"=", "question 7.2")
coinciding_df = merged_df[merged_df['INSEE commune'] == merged_df['CODGEO']]
mean_coinciding = coinciding_df['NBPERSMENFISC16'].mean()
std_coinciding = coinciding_df['NBPERSMENFISC16'].std()
min_coinciding = coinciding_df['NBPERSMENFISC16'].min()
max_coinciding = coinciding_df['NBPERSMENFISC16'].max()
print("coinciding_df:", coinciding_df)
print(f"mean_coinciding: {mean_coinciding}, std_coinciding: {std_coinciding}, min_coinciding: {min_coinciding}, max_coinciding: {max_coinciding}")

# 8
print("\n", 40*"=", "question 8")
# Filtrer les grandes villes (plus de 100 000 personnes)
df_large_cities = df_city[df_city['NBPERSMENFISC16'] > 100000]
# Identifier les villes avec des noms de commune en doublon
duplicate_city_names = df_large_cities['LIBGEO'].duplicated(keep=False)
# Sélectionner les villes avec des noms de commune en doublon
cities_with_duplicate_names = df_large_cities[duplicate_city_names]
# Grouper par nom de commune et calculer le nombre d'habitants et la proportion de villes avec différents codes communes
grouped_cities = cities_with_duplicate_names.groupby('LIBGEO').agg({'NBPERSMENFISC16': 'sum', 'CODGEO': 'nunique'})
# Afficher le résultat avec le nombre d'habitants, la proportion et les codes communes associés
print("Villes avec un même nom associé à différents codes commune parmi les grandes villes :")
for city_name, row in grouped_cities.iterrows():
    population = row['NBPERSMENFISC16']
    num_codes = row['CODGEO']
    proportion = num_codes / len(cities_with_duplicate_names[cities_with_duplicate_names['LIBGEO'] == city_name])
    codgeo_values = ', '.join(cities_with_duplicate_names[cities_with_duplicate_names['LIBGEO'] == city_name]['CODGEO'].unique())
    print(f"Nom de commune : {city_name}, Nombre d'habitants : {population}, Proportion : {proportion:.2f}, Codes communes associés : {codgeo_values}")

# 9
print("\n", 40*"=", "question 9")

# Villes avec le libellé "Montreuil"
print(40*"*", "Montreuil")
cities_montreuil = df_city[df_city['LIBGEO'].str.match('montreuil')]
print("Villes avec le libellé 'Montreuil':")
print(cities_montreuil[['CODGEO', 'LIBGEO']])

# Villes contenant le terme "Saint-Denis"
print(40*"*", "Saint-Denis")
cities_saint_denis = df_city[df_city['LIBGEO'].str.contains('saint-denis')]
print("Villes contenant le terme 'saint-denis':")
print(cities_saint_denis[['CODGEO', 'LIBGEO']])
