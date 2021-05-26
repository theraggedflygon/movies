import requests

with open("token.txt", 'r') as file:
    token = file.read()

headers = {
    "Authorization": "Bearer {}".format(token),
    'Content-Type': 'application/json;charset=utf-8'
}

url = "https://api.themoviedb.org/3/movie/496243"

r = requests.get(url, headers=headers)
data = r.json()
print(data['poster_path'])

poster_url = "http://image.tmdb.org/t/p/w185{}".format(data['poster_path'])