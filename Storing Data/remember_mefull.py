import json

filename='username.json'
nombre_verificar=input('Ingrese su nombre de usuario')
def ingresar_usuario():
    username=input('¿Cuál es tu nombre completo?')
    with open(filename,'w') as file_object:
        json.dump(username,file_object)
        print(f'Tu nombre {username} se recordará cuando regreses')

        
try:
    with open(filename,'r') as file_object:
        username=json.load(file_object)
except FileNotFoundError:
        ingresar_usuario()
else:
    if username==nombre_verificar:
        print(f'Bienvenido de regreso,{username}')
    else:
        print('Su nombre de usuario no ha sido registrado. Ingrese sus datos')
        ingresar_usuario()




