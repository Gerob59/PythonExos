import pandas as pd
import pynsee

df_city_type = {
    'CODGEO': object,
    'LIBGEO': object,
    'NBMENFISC16': float,
    'NBPERSMENFISC16': float,
    'MED16': float,
    'PIMP16': float,
    'TP6016': float,
    'TP60AGE116': float,
    'TP60AGE216': float,
    'TP60AGE316': float,
    'TP60AGE416': float,
    'TP60AGE516': float,
    'TP60AGE616': float,
    'TP60TOL116': float,
    'TP60TOL216': float,
    'PACT16': float,
    'PTSA16': float,
    'PCHO16': float,
    'PBEN16': float,
    'PPEN16': float,
    'PPAT16': float,
    'PPSOC16': float,
    'PPFAM16': float,
    'PPMINI16': float,
    'PPLOGT16': float,
    'PIMPOT16': float,
    'D116': float,
    'D916': float,
    'RD16': float
}

df = pd.read_csv("https://koumoul.com/s/data-fair/api/v1/datasets/igt-pouvoir-de-rechauffement-global/convert", sep=",")
df['INSEE commune'] = df['INSEE commune'].str.strip().str.lower()
df['Commune'] = df['Commune'].str.strip().str.lower()

df_city = pynsee.download.download_file("FILOSOFI_COM_2016")
df_city = df_city.astype(df_city_type)
df_city['CODGEO'] = df_city['CODGEO'].str.strip().str.lower()
df_city['LIBGEO'] = df_city['LIBGEO'].str.strip().str.lower()
