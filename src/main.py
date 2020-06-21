from argparse import ArgumentParser
import pandas as pd
import analysis 


def parse():
    parser=ArgumentParser(description="Este programa es para buscar los streams de los artistas cuyas canciones son las más reproducidas en Spotify en el año 2019")
    parser.add_argument("--artist",dest="Artist",help="El artista de la canción")
    parser.add_argument("--songname",dest="song_name",help="El nombre del single")
    return parser.parse_args()


def main():
    args=parse()
    Artist=args.artist
    song_name=args.song_name
    print(artist)
    print(songname)
    data=acquire()
    filtered = filters(data,Artist,song_name)
    results = analysis(filtered)


if __name__ == '__main__':
    main()




