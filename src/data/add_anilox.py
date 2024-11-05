import requests
from random import choice, randint

url = 'http://127.0.0.1:5000/add_anilox'
roller = randint(10000,99999)
data_list = ['200-11.0', '360-8.0', '400-6.5', '440-6.0', '550-5.0', '600-5.0', '800-3.5','800-2.2', '900-2.2', '1000-2.0']
lpi, bcm = choice(data_list).split('-')

data = {
    'roller' : roller,
    'lpi' : lpi,
    'bcm' : bcm
}

upload = requests.post(url, json=data)
print(upload.status_code)
