from tp_pandas.chapitre1.data import df, df_city
from tp_pandas.chapitre2.II_structure_donnees import df_city_type

df['INSEE commune'] = df['INSEE commune'].str.strip().str.lower()
df['Commune'] = df['Commune'].str.strip().str.lower()

df_city = df_city.astype(df_city_type)
df_city['CODGEO'] = df_city['CODGEO'].str.strip().str.lower()
df_city['LIBGEO'] = df_city['LIBGEO'].str.strip().str.lower()
