from I_df import df
from I_df_city import df_city

if __name__ == "__main__":

    # -----------------------DF----------------------- #

    print(40*"=", "DF columns")
    print(df.columns)
    # print(40 * "*", "DF INSEE commune")
    # print(df["INSEE commune"])  # --> peut être convertis en int
    # print(40 * "*", "DF Commune")
    # print(df["Commune"])  # --> peut être convertis en string
    # print(40 * "*", "DF Agriculture")
    # print(df["Agriculture"])
    # print(40 * "*", "DF Autres transports")
    # print(df["Autres transports"])
    # print(40*"*", "DF Autres transports international")
    # print(df["Autres transports international"])
    # print(40 * "*", "DF CO2 biomasse hors-total")
    # print(df["CO2 biomasse hors-total"])
    # print(40 * "*", "DF Déchets")
    # print(df["Déchets"])
    # print(40 * "*", "DF Energie")
    # print(df["Energie"])
    # print(40 * "*", "DF Industrie hors-énergie")
    # print(df["Industrie hors-énergie"])
    # print(40 * "*", "DF Résidentiel")
    # print(df["Résidentiel"])
    # print(40 * "*", "DF Routier")
    # print(df["Routier"])
    # print(40 * "*", "DF Tertiaire")
    # print(df["Tertiaire"])

    # --------------------DF_CITY--------------------- #

    # print(40 * "=", "DF_CITY columns")
    # print(df_city.columns)
    # print(40 * "*", "DF_CITY CODGEO")
    # print(df_city["CODGEO"])  #--> int
    # print(40 * "*", "DF_CITY LIBGEO")
    # print(df_city["LIBGEO"])  #--> string
    # print(40 * "*", "DF_CITY NBMENFISC16")
    # print(df_city["NBMENFISC16"])  #--> int
    # print(40 * "*", "DF_CITY NBPERSMENFISC16")
    # print(df_city["NBPERSMENFISC16"])   #--> float
    # print(40 * "*", "DF_CITY MED16")
    # print(df_city["MED16"])  #--> float
    # print(40 * "*", "DF_CITY PIMP16")
    # print(df_city["PIMP16"])  #--> int
    # print(40 * "*", "DF_CITY TP6016")
    # print(df_city["TP6016"])  #--> int
    # print(40 * "*", "DF_CITY TP60AGE116")
    # print(df_city["TP60AGE116"])  #--> int
    # print(40 * "*", "DF_CITY TP60AGE216")
    # print(df_city["TP60AGE216"])  #--> int
    # print(40 * "*", "DF_CITY TP60AGE316")
    # print(df_city["TP60AGE316"])  #--> int
    # print(40 * "*", "DF_CITY TP60AGE416")
    # print(df_city["TP60AGE416"])  #--> int
    # print(40 * "*", "DF_CITY TP60AGE516")
    # print(df_city["TP60AGE516"])  #--> int
    # print(40 * "*", "DF_CITY TP60AGE616")
    # print(df_city["TP60AGE616"])  #--> int
    # print(40 * "*", "DF_CITY TP60TOL116")
    # print(df_city["TP60TOL116"])  #--> int
    # print(40 * "*", "DF_CITY TP60TOL216")
    # print(df_city["TP60TOL216"])  #--> int
    # print(40 * "*", "DF_CITY PACT16")
    # print(df_city["PACT16"])  #--> float
    # print(40 * "*", "DF_CITY PTSA16")
    # print(df_city["PTSA16"])  #--> float
    # print(40 * "*", "DF_CITY PCHO16")
    # print(df_city["PCHO16"])  #--> float
    # print(40 * "*", "DF_CITY PBEN16")
    # print(df_city["PBEN16"])  #--> float
    # print(40 * "*", "DF_CITY PPEN16")
    # print(df_city["PPEN16"])  #--> float
    # print(40 * "*", "DF_CITY PPAT16")
    # print(df_city["PPAT16"])  #--> float
    # print(40 * "*", "DF_CITY PPSOC16")
    # print(df_city["PPSOC16"])  #--> float
    # print(40 * "*", "DF_CITY PPFAM16")
    # print(df_city["PPFAM16"])  #--> float
    # print(40 * "*", "DF_CITY PPMINI16")
    # print(df_city["PPMINI16"])  #--> float
    # print(40 * "*", "DF_CITY PPLOGT16")
    # print(df_city["PPLOGT16"])  #--> float
    # print(40 * "*", "DF_CITY PIMPOT16")
    # print(df_city["PIMPOT16"])  #--> float
    # print(40 * "*", "DF_CITY D116")
    # print(df_city["D116"])  #--> float
    # print(40 * "*", "DF_CITY D916")
    # print(df_city["D916"])  #--> float
    # print(40 * "*", "DF_CITY RD16")
    # print(df_city["RD16"])  #--> float

    # --------------------DF_CITY--------------------- #

    # INSEE commune == CODGEO
    # communes == upper(LIBGEO)
