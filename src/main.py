from argparse import ArgumentParser
import pandas as pd
from analysis import *
from charts import *
import matplotlib.pyplot as plt
import seaborn as sns


def parse():
    parser=ArgumentParser(description="Este programa es para buscar los 10 mejores cantantes para cada popularidad y streamings seleccionado")
    parser.add_argument("--followers",dest="followers",help="filtras según el número de followers con respecto al resto de artistas. opciones disponibles('very low', 'low', 'medium', 'high')")
    parser.add_argument("--streams",dest="streams",help="filtras según el número de streams con respecto al resto de artistas.Opciones disponibles('very low', 'low', 'medium', 'high')")
    return parser.parse_args()


def main():
    args=parse()
    followers=args.followers
    Streams1=args.streams
    print(followers)
    print(streams)
    data=acquire()
    filtered = filters(data,followers,streams)
    results = analysis(filtered)
    chart = visualize(results,followers,streams)
    save_chart(chart)


if __name__ == '__main__':
    main()




