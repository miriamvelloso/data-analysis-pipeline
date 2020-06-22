import pandas as pd

def acquire():
    data=pd.read_csv('Input/spotify_clean.csv')
    return data

def filters(data,followers,streams):
    filtered=data[(data["Artist_follower"]==f"{followers}")&(data["Streams1"]==f"{streams}")]
    print(filtered)
    return filtered

def analysis(df):
    grouped=df.groupby("Artist").agg({"Artist_popularity":"mean"}).reset_index()
    results=grouped.sort_values("Artist_popularity",ascending=False).head(10)
    print(results)
    return results