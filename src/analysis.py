import pandas as pd

def acquire():
    data=pd.read_csv('input/spotify_clean.csv')
    return data

def filters(df,song_name,name):
    filtered=df[(df["song_name"]==song_name)&(df["Artist"]==artist_name)]
    print(filtered)
    return filtered

def analysis(df):
    grouped=df.groupby("name").agg({"Streams":"sum"}).reset_index()
    results=grouped.sort_values("Streams",ascending=False).head(10)
    print(results)
    return results