import json

try: 
    filename='favorite_number.json'
    with open(filename) as file_object:
        number=json.load(file_object)
except FileNotFoundError:
    number=input('Ingresa tu número favorito')
    with open(filename,'w') as file_object:
        json.dump(number,file_object)
        print(f'Se ha guardado tu número favorito: {number}')
else:
    print(f'Conozco tu número favorito. Es: {number}')  