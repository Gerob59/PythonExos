import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from tp_pandas.chapitre3.df_formatage import df
from tp_pandas.chapitre3.df_formatage import df_city

# 1. Calcul des émissions totales par commune
df['Emissions_CO2'] = df.select_dtypes(include=[np.number]).sum(axis=1)
emissions = df.groupby('INSEE commune')['Emissions_CO2'].sum().reset_index()

# 2. Jointure à gauche avec les données de cadrage
merged_df = pd.merge(df, df_city, left_on=['INSEE commune', 'Commune'], right_on=['CODGEO', 'LIBGEO'], how='left')

# 3
# Calcul de l'empreinte carbone par commune
merged_df['Empreinte_carbone'] = merged_df['Emissions_CO2'] / merged_df['NBMENFISC16']

# Histogramme en niveau
# merged_df['Empreinte_carbone'].hist()
# plt.xlabel('Empreinte carbone')
# plt.ylabel('Nombre de communes')
# plt.title("Histogramme de l'empreinte carbone")
# plt.show()

# Statistiques descriptives
empreinte_stats = merged_df['Empreinte_carbone'].describe()
print(empreinte_stats)

# 4
# Calcul de la corrélation
correlation = merged_df[['Empreinte_carbone', 'NBPERSMENFISC16', 'MED16', 'PIMP16', 'PPAT16', 'PIMPOT16']].corr()

# Affichage de la corrélation
print(correlation)
