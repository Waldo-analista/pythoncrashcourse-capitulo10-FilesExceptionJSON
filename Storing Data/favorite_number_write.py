import json

filename='favorite_number.json'
number=input('Ingresa tu número favorito')
with open(filename,'w') as file_object:
    json.dump(number,file_object)
    print(f'Se ha guardado tu número favorito: {number}')