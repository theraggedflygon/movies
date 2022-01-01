import csv
import json
import os
import requests
from tmdbAuth import get_token, get_headers


class Poster_Finder:
    def __init__(self, config_json_filename):
        with open(f"config/{config_json_filename}.json", 'r') as file:
            config = json.load(file)
        self.name = config['Name']
        self.token = get_token()
        self.headers = get_headers()
        self.titles = []
        self.ids = []
        self.read_id_file()
        self.get_posters()

    def read_id_file(self):
        with open(f"data/{self.name}_tmdb_ids.csv", 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    self.titles.append(row[0])
                    if row[1] != "None":
                        self.ids.append(int(row[1]))
                    else:
                        self.ids.append(None)
                else:
                    self.titles.append(",".join(row[:-1]))
                    if row[-1] != "None":
                        self.ids.append(int(row[-1]))
                    else:
                        self.ids.append(None)

    def get_posters(self):
        if not os.path.exists(f"posters/{self.name}"):
            os.mkdir(f"posters/{self.name}")
        for idx, title in enumerate(self.titles):
            print("Finding poster for " + title)
            poster_file = f"posters/{self.name}/{idx + 1}_{self.format_poster_string(title)}_poster.png"

            if self.ids[idx] is not None:
                film_url = "https://api.themoviedb.org/3/movie/{}?api_key={}".format(self.ids[idx], self.token)
                r = requests.get(film_url, headers=self.headers)
                data = r.json()
                poster_url = "http://image.tmdb.org/t/p/w185/{}".format(data['poster_path'])
                image_r = requests.get(poster_url)
                with open(poster_file, 'wb') as poster:
                    poster.write(image_r.content)
            else:
                with open(poster_file, 'w') as poster:
                    poster.write("placeholder")

    @staticmethod
    def format_poster_string(poster_str):
        return poster_str.replace(" ", "_").replace(",", "").replace(".", "").replace("/", "_")\
            .replace(":", "-").replace("?", "").replace("#", "").replace("!", "")
