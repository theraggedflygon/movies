import json
import os
import tmdb_finder
import poster_finder
import photogrid


class Movie_List:
    def __init__(self, session_name):
        self.config_name = session_name
        with open(f"config/{session_name}.json", 'r') as file:
            config = json.load(file)
        self.name = config['Name']

        if not os.path.exists(f"data/{self.name}_tmdb_ids.csv"):
            tmdb_finder.TMDB_Finder(self.config_name)

        if not os.path.exists(f"posters/{self.name}"):
            poster_finder.Poster_Finder(self.config_name)

        photogrid.Photogrid(self.config_name)


if __name__ == "__main__":
    run = "mia22diary"
    movies = Movie_List(run)
