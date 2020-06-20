from argparse import ArgumentParser

def parse():
    parser=ArgumentParser(description="Este programa es para buscar los streams de los artistas cuyas canciones son las más reproducidas en Spotify en el año 2019")
    parser.add_argument("--artist",dest="Artist",help="El artista de la canción")
    parser.add_argument("--trackname",dest="Track Name",help="El nombre del single")
    return parser.parse_args()


def main():
    args=parse()
    year=args.artist
    tour=args.trackname
    print(artist)
    print(trackname)
    data=acquire()
    filtered = filters(data,artist,trackname)
    results = analysis(filtered)
    barchart = visualize(results,artist,trackname)
    save_chart(barchart)
    filtered2 = filters2(data)
    results2 = analysis2(filtered2)
    winners_data = acquire2()
    send_email(results2,winners_data)
    
if __name__ == '__main__':
    main()