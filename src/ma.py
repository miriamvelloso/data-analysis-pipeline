from argparse import ArgumentParser
import pandas as pd
from analysis import *

def parse():
    parser=ArgumentParser(description="Este programa es para buscar los streams de los artistas cuyas canciones son las más reproducidas en Spotify en el año 2019")
    parser.add_argument("--artist",dest="artist_name",help="El artista de la canción")
    parser.add_argument("--songname",dest="song_name",help="El nombre del single")
    return parser.parse_args()


def main():
    args=parse()
    Artist=args.artist_name
    song_name=args.song_name
    print(artist)
    print(songname)
    
if __name__ == '__main__':
    main()
