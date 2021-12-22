import requests

name_search_url = "https://superheroapi.com/api/2619421814940190/search/"
heroes = [{'name' : 'Hulk'}, {'name' : 'Captain America'}, {'name' : 'Thanos'}]

for hero in heroes:
    hero_req = requests.get(name_search_url + hero['name'])
    hero['intelligence'] = int(hero_req.json()['results'][0]['powerstats']['intelligence'])
    
print(sorted(heroes, key=lambda hero: -hero['intelligence'])[0]['name'])
