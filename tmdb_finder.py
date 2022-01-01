from Film import Film
import csv
import json


class TMDB_Finder:
    def __init__(self, config_json_filename):
        with open(f"config/{config_json_filename}.json", 'r') as file:
            config = json.load(file)
        self.name = config['Name']
        self.data = config['DataFile']
        self.movies = []
        self.read_movie_file()
        self.write_tmdb_ids()

    def read_movie_file(self):
        with open(f"data/{self.data}", 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for movie in reader:
                self.movies.append(Film(movie[1], movie[2], movie[0]))

    def write_tmdb_ids(self):
        with open(f"data/{self.name}_tmdb_ids.csv", 'w', encoding='utf-8') as file:
            for movie in self.movies:
                if movie.id is None:
                    print(f"{movie.title} TMDB ID Could Not Be Found")
                file.write("{},{}\n".format(movie.title, movie.id))
