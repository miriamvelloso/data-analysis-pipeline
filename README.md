## Project 2 - Data Analysis Pipeline

- Para este proyecto utilizo:

1. Dataset ATP descargado de Kaggle -> https://www.kaggle.com/prasertk/spotify-global-2019-moststreamed-tracks
2. API - Musicbrainz -> http://musicbrainz.org/

- To Do's

- [x] Choose a dataset you like from kaggle.com
- [x] Create a python script and name it main.py. 
- [x] Filter the dataset with the params received from main.py
- [x] Enrich the dataset with external data.

**Cleaning Dataset:**

En primer lugar, realizo la limpieza de datos del dataset descargado Cleaning.ipynb:

Elimino las columnas no necesarias
Limpio contenido de las columnas
Creo nuevas columnas necesarias para el posterior ánalisis
Genero nuevo CSV (spotify_clean.csv) con datos limpios.

**API & Web Scrapping:**

En segundo lugar, tras identificar los artistas más escuchados del año 2019, procedo a obtener los datos personales (Nacionalidad,Fecha de nacimiento, Sexo y ) de estos jugadores a través de la API de TheSportsDB incluyendo los parametros de cada jugador.

Además, realizo un Web Scrapping para obtener el total de ganancias del top 10 de artistas con mayor streaming pero solo consigo dos de ellos.

Tras obtener estos datos a través de la API, creo un nuevo dataframe con ambos datos (artists_clean.csv).

**Script:**

Por último, procedo a crear un programa de python main.py para generar el análisis de los 10 mejores artistas según followers y streams . Para ello, he utilizado argparse para crear dos parametros "streams" y "followers" que van a filtrar el dataset.



