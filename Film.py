import requests
from tmdbAuth import get_token, get_headers


class Film:
    def __init__(self, title, year, idx):
        print("Requesting", title)
        self.title = title
        self.year = year
        self.index = idx

        self.id = self.get_tmdb()

    def get_tmdb(self):
        search_url = "https://api.themoviedb.org/3/search/movie?api_key={}&query={}".format(get_token(),
                                                                                            self.title.replace("#", ""))
        r = requests.get(search_url, headers=get_headers())
        data = r.json()['results']
        for film in data:
            try:
                if abs(int(film['release_date'][:4]) - int(self.year)) < 2 and film['title'] == self.title:
                    return film['id']
            except KeyError:
                continue
            except ValueError:
                continue
        while True:
            user_key = input(f"TMDB ID could not be found for {self.title} ({self.year}). Please enter the TMDB "
                             f"manually or type 'None' to move on: ")
            if user_key.isnumeric():
                return int(user_key)
            elif user_key.lower() == "none":
                return None
