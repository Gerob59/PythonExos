from matplotlib import pyplot as plt
from tp_pandas.chapitre3.df_formatage import df

df_wide = df.copy()

df_long = df_wide.melt(id_vars=['Commune', 'INSEE commune'], var_name='Secteur', value_name='Emissions_CO2')

df_sum = df_long.groupby('Secteur')['Emissions_CO2'].sum().sort_values(ascending=False)
# df_sum.plot(kind='bar')
# plt.xlabel('Secteur')
# plt.ylabel('Total des émissions de CO2')
# plt.title('Total des émissions de CO2 par secteur')
# plt.show()

df_max_pollution = df_long.loc[df_long.groupby('INSEE commune')['Emissions_CO2'].idxmax()]
print(df_max_pollution)

