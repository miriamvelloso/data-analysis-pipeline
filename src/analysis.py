import pandas as pd

def acquire():
    data=pd.read_csv('spotify_clean.csv')
    return data

def filters(df,Artist_follower,Streams1):
    filtered=df[(df["Artist_follower"]==followers)&(df["Streams1"]==streams)]
    print(filtered)
    return filtered

def analysis(df):
    grouped=df.groupby("Artist").agg({"Artist_popularity":"mean"}).reset_index()
    results=grouped.sort_values("Artist_popularity",ascending=False).head(10)
    print(results)
    return results