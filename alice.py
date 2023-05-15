filename=r'text_files\alice.txt'
try:
    with open(filename,encoding="utf8") as file_object:
        contenido=file_object.read()
except FileNotFoundError:
    print('El archivo no existe en este directorio')
else:
    palabras=contenido.split()
    numero_words=len(palabras)
    print(f'El archivo {filename} tiene alrededor de {str(numero_words)}')