import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_import = pd.read_csv('src/artists_clean.csv',encoding='latin-1')

def visualize(dd,Gender,Country):
    title = 'Top 10 most popularity Artists '
    fig, ax = plt.subplots(figsize=(15,8))
    chart = sns.barplot(data=df_import, x='Name', y='Streams')
    plt.title(title + "\n", fontsize=10)
    return chart

def save_chart(graph):
    title2 = 'Top 10 most popularity Artists'
    fig=graph.get_figure()
    fig.savefig(title2 + '.png')

