import json

filename='favorite_number.json'

with open(filename) as file_object:
    number=json.load(file_object)
    print(f'Conozco tu número favorito. Es: {number}')