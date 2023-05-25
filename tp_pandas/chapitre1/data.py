import pandas as pd
import pynsee.download
from pandas import DataFrame

df: DataFrame = pd.read_csv("https://koumoul.com/s/data-fair/api/v1/datasets/igt-pouvoir-de-rechauffement-global/convert", sep=",")
df_city: DataFrame = pynsee.download.download_file("FILOSOFI_COM_2016")

