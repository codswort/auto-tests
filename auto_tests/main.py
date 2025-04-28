import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7d185759f3c6c9d6fab919ba129a3dce'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}

body_create = {
    "name": "Первый покемон",
    "photo_id": 7
}

body_put = {
    "pokemon_id": "303367",
    "name": "Первый покемон с новым именем",
    "photo_id": 7
}

body_in_pokeball = {
    "pokemon_id": "303367"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)
print(response_put.text)

response_in_pokenall = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_in_pokeball)
print(response_in_pokenall.text)
