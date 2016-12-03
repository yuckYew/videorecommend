import json
from pprint import pprint as pp

with open('movie_data.json', 'r') as rf:
    movie_data = json.load(rf)

print(type(movie_data))
pp(movie_data)
