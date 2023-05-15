def count_words(filename):
    try:
        with open(filename,encoding="utf8") as file_object:
            contenido=file_object.read()
    except FileNotFoundError:
        pass
        #print('El archivo no existe en este directorio')
    else:
        palabras=contenido.split()
        numero_words=len(palabras)
        print(f'El archivo {filename} tiene alrededor de {str(numero_words)}')

filenames=[r'text_files\alice.txt',r'text_files\siddhartha.txt',r'text_files\moby_dick.txt',r'text_files\little_women.txt']
for filename in filenames:
    count_words(filename)