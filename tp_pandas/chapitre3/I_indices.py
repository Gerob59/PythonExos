from df import df, df_city

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
