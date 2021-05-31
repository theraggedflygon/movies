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
        search_url = "https://api.themoviedb.org/3/search/movie?api_key={}&query={}".format(get_token(), self.title)
        r = requests.get(search_url, headers=get_headers())
        data = r.json()['results']
        for film in data:
            try:
                if film['release_date'][:4] == self.year and film['title'] == self.title:
                    return film['id']
            except KeyError:
                continue
        return None
