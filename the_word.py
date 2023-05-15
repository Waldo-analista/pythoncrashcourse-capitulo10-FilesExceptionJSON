filenames=[r'text_files\alice.txt',r'text_files\moby_dick.txt',r'text_files\little_women.txt']

filename=r'text_files\alice.txt'
def contar(filename):
    try:
        with open(filename,encoding='UTF-8') as file_object:
            texto=file_object.read().lower()
    except FileNotFoundError:
        print('Un archivo no existe en el directorio')
    else:
        contador=texto.count('the')
        print(contador)

for filename in filenames:
    contar(filename)