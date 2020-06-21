import pandas as pd

def acquire():
    data=pd.read_csv('input/spotify_clean.csv')
    return data

def filters(df,song_name,streams):
    filtered=df[(df["song_name"]==song)&(df["Streams"]==streams)]
    print(filtered)
    return filtered

def analysis(df):
    grouped=df.groupby("song").agg({"Streams":"sum"}).reset_index()
    results=grouped.sort_values("Streams",ascending=False).head(10)
    print(results)
    return results