import json
username=input('¿Cuál es tu nombre?')

filename='username.json'
with open(filename,'w') as file_object:
    json.dump(username,file_object)
    print(f'Se recordará tu nombre {username} cuando regreses')
