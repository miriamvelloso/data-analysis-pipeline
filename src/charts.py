import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analysis import *


def visualize(df,song_name,streams):
    title = 'Top 10  '+ song_name + ' with most streams'
    fig, ax = plt.subplots(figsize=(15,8))
    barchart = sns.barplot(data=df, x='Srtist', y='Streams')
    plt.title(title + "\n", fontsize=10)
    return barchart

def save_chart(graph):
    title2 = 'Top 10 songs 2019'
    fig=graph.get_figure()
    fig.savefig(title2 + '.png')