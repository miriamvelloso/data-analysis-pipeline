import pandas as pd
from analysis import *

def filters2(df):
    filtered2=df[(df["Top10"]=="1")]
    print(filtered2)
    return filtered2

def analysis2(df):
    grouped2=df.groupby("Artist").agg({"Track Name":"count","Streams":"sum"})
    results2=grouped2.sort_values("Streams",ascending=False)
    print("Estos son los 10 artistas más escuchados en 2019")
    return results2


def acquire2():
    artist_data=pd.read_csv('artists_clean.csv')
    artist_data=artist_data.drop(columns=["Unnamed: 0"])
    print("Además, estos son los datos personales de cada ganador: Nacionalidad, Fecha de Nacimiento, Altura, Ganancias:", artist_data)
    return artist_data
