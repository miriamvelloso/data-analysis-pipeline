from argparse import ArgumentParser
import pandas as pd
import src.analysis as an
import src.charts as ch
import src.segundoanalysis as san
import src.mail as mail
import matplotlib.pyplot as plt
import seaborn as sns


def parse():
    parser=ArgumentParser(description="Este programa es para buscar los 10 mejores cantantes para cada popularidad y streamings seleccionado")
    parser.add_argument("--followers",dest="x",help="filtras según el número de followers con respecto al resto de artistas. opciones disponibles('very low', 'low', 'medium', 'high')")
    parser.add_argument("--streams",dest="y",help="filtras según el número de streams con respecto al resto de artistas.Opciones disponibles('very low', 'low', 'medium', 'high')")
    args=parser.parse_args()
    return args


def main():
    args=parse()
    followers=args.x
    streams=args.y
    print(followers)
    print(streams)
    data=an.acquire()
    filtered = an.filters(data,followers,streams)
    results = an.analysis(filtered)
    chart = ch.visualize(results,followers,streams)
    ch.save_chart(chart)
    filtered2 = san.filters2(data)
    results2 = san.analysis2(filtered2)
    artist_data = san.acquire2()
    mail.send_email(results2,artist_data)


if __name__ == '__main__':
    main()




