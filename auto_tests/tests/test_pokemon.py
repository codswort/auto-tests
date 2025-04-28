import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7d185759f3c6c9d6fab919ba129a3dce'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}
TRAINER_ID = 37214

def test_check_status_code():
    response = requests.get(url = f'{URL}/trainers', headers = HEADER)
    assert response.status_code == 200

def test_trainer_name():
    response_trainer = requests.get(url = f'{URL}/trainers', headers = HEADER,  params = {'trainer_id': TRAINER_ID})

    assert response_trainer.json()['data'][0]['trainer_name'] == 'Auto'
