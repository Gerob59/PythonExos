import numpy as np
from matplotlib import pyplot as plt
from df_formatage import df, df_city

# 1
print("\n", 40*"=", "question 1")
print(40*"*", "set_index df")
df.set_index('INSEE commune', inplace=True)
print("DataFrame df avec l'indice sur la variable INSEE commune :")
print(df)
print(40*"*", "set_index df_city")
df_city.set_index('CODGEO', inplace=True)
print("DataFrame df_city avec l'indice sur la variable CODGEO :")
print(df_city)

# 2
print("\n", 40*"=", "question 2")
print(40*"*", "df['dep']=")
df['dep'] = df.index.str.slice(0, 2)
print(df)
print(40*"*", "df_city['dep']")
df_city['dep'] = df_city.index.str.slice(0, 2)
print(df_city)

# 3
print("\n", 40*"=", "question 3")
# Calcul le total d'émission part secteur, par département
df_grouped = df.groupby('dep').sum()
# enlève les colonnes non-numériques
df_log = df_grouped.select_dtypes(include=[np.number]).apply(np.log)
# df_log.sample(5).plot(kind="bar", stacked=True)
# plt.xlabel('Département')
# plt.ylabel('Émissions (log)')
# plt.title('Émissions totales par secteur pour les 5 départements')
# plt.show()

# 4
print("\n", 40*"=", "question 4")
# Calcul de la somme des émissions de CO2 par département
df['Total_CO2'] = df.iloc[:, 1:-1].sum(axis=1)
# Tri des départements par rapport à la nouvelle colonne "Total_CO2"
df_sorted = df.sort_values('Total_CO2', ascending=False)
# Affichage des 10 principaux émetteurs de CO2
top_emitters = df_sorted.head(10)
print("Les 10 principaux émetteurs de CO2 par département :")
print(top_emitters[['dep', 'Total_CO2']])
# Affichage des 5 départements les moins émetteurs de CO2
lowest_emitters = df_sorted.tail(5)
print("Les 5 départements les moins émetteurs de CO2 :")
print(lowest_emitters[['dep', 'Total_CO2']])
