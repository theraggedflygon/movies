from Film import Film
import csv
import json
import pandas as pd


class TMDB_Finder:
    def __init__(self, config_json_filename):
        with open(f"config/{config_json_filename}.json", 'r') as file:
            config = json.load(file)
        self.name = config['Name']
        self.data = config['DataFile']
        self.movies = []

        if config['FileType'] == 'List':
            self.read_list_file()
        else:
            start = config['Start']
            end = config['End']
            includes = {'rewatches': config['Rewatches'], 'repeats': config['Repeats'], 'tv': config['TV'],
                        'shorts': config['Shorts']}
            self.read_diary_file(start, end, includes)
        self.write_tmdb_ids()

    def read_list_file(self):
        with open(f"data/{self.data}", 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for movie in reader:
                self.movies.append(Film(movie[1], movie[2], movie[0]))

    def read_diary_file(self, start, end, includes):
        df = pd.read_csv(f"data/{self.data}", encoding='utf-8')
        df.sort_values("Watched Date")
        df = df.loc[(df["Watched Date"] >= start) & (df["Watched Date"] <= end)]
        df.reset_index(drop=True, inplace=True)
        ctr = 0
        repeat_check = []
        for idx, row in df.iterrows():
            if not includes['rewatches'] and row['Rewatch'] == "Yes":
                continue
            check_str = f"{row['Name']}{row['Year']}"
            if not includes['repeats'] and check_str in repeat_check:
                continue
            new_film = Film(row['Name'], row['Year'], ctr)
            if new_film.id is not None:
                if not includes['shorts'] and new_film.short:
                    continue
                self.movies.append(new_film)
                repeat_check.append(check_str)
                ctr += 1

    def write_tmdb_ids(self):
        with open(f"data/{self.name}_tmdb_ids.csv", 'w', encoding='utf-8') as file:
            for movie in self.movies:
                if movie.id is None:
                    print(f"{movie.title} TMDB ID Could Not Be Found")
                file.write("{},{}\n".format(movie.title, movie.id))
