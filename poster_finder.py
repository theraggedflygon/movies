import csv
import requests
from tmdbAuth import get_token, get_headers

token = get_token()
headers = get_headers()

titles = []
ids = []
with open("data/tmdb_ids.csv", 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) == 2:
            titles.append(row[0])
            if row[1] != "None":
                ids.append(int(row[1]))
            else:
                ids.append(None)
        else:
            titles.append(",".join(row[:-1]))
            if row[-1] != "None":
                ids.append(int(row[-1]))
            else:
                ids.append(None)

for idx, title in enumerate(titles):
    print("Finding poster for " + title)
    poster_file = "posters/{}_{}_poster.png".format(idx + 1, title.replace(" ", "_").replace(",", "").replace(".", "")
                                                    .replace("/", "_").replace(":", "-"))
    if ids[idx] is not None:
        film_url = "https://api.themoviedb.org/3/movie/{}?api_key={}".format(ids[idx], token)
        r = requests.get(film_url, headers=headers)
        data = r.json()
        poster_url = "http://image.tmdb.org/t/p/w185/{}".format(data['poster_path'])
        image_r = requests.get(poster_url)
        with open(poster_file, 'wb') as poster:
            poster.write(image_r.content)
    else:
        with open(poster_file, 'w') as poster:
            poster.write("placeholder")
