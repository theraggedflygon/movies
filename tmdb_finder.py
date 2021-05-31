from Film import Film
import csv
import requests

movies = []
with open("data/films-i-saw-for-the-first-time-in-2020.csv", 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for movie in reader:
        movies.append(Film(movie[1], movie[2], movie[0]))

with open("data/tmdb_ids.csv", 'w', encoding='utf-8') as file:
    for movie in movies:
        if movie.id is None:
            print(movie.title)
        file.write("{},{}\n".format(movie.title, movie.id))
