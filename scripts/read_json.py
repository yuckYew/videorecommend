import json
from pprint import pprint as pp

with open('movie_data.json', 'r') as rf:
    parsed_json = json.load(rf)

print(parsed_json[0]['title'])

for movie in parsed_json:
    parsed_json[0]['title'] = pp(movie['title'])
