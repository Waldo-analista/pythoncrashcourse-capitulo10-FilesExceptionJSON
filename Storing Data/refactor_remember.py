import json


def recibir_usuario():
    username=leer_nombre()
    if username:
        print(f'Bienvenido de regreso,{username}')
    else:
        obtener_nuevo_usuario()


def obtener_nuevo_usuario():
    filename='username.json'
    username=input('¿Cuál es tu nombre completo?')
    with open(filename,'w') as file_object:
        json.dump(username,file_object)
        print(f'Tu nombre {username} se recordará cuando regreses')


def leer_nombre():
    filename='username.json'
    try:
        with open(filename,'r') as file_object:
            username=json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username



recibir_usuario()